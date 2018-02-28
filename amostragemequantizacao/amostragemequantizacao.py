#!/usr/bin/python
#-*-coding: utf-8 -*-
#Criado por GleisonJSilva
#Criado em : 24/10/2017, 15:12:34
#Gustavo Lupercino


import numpy as np
import cv2
from matplotlib import pyplot as plt 
import sys


def menu():
    print 'OPÇÕES:'
    print ''
    print '0 - SAIR'
    print '1 - AMOSTRAGEM E QUANTIZAÇÃO'
    print '2 - RESOLUÇÃO ESPACIAL'
    print '3 - RESOLUÇÃO DE INTENSIDADE'
    print '4 - EQUALIZAÇÃO E HISTOGRAMA'
    print '5 - HISTOGRAMA'
    print '6 - FILTRO DE MÉDIA'
    print '7 - FILTRO DE MEDIANA'
    print ''

#Recebe a imagem e imprime na tela
def geraImagem(img):
    while True:
        ch=0xFF & cv2.waitKey()
        if ch==27: # ESC key
            break
        cv2.imshow('Processamento de Imagens', img)   
    cv2.destroyAllWindows()
    
#Recebe duas imagens e imprime na tela, uma original e uma trabalhada   
def geraImagens(img, resultado):
    while True:
        ch=0xFF & cv2.waitKey()
        if ch==27: # ESC key
            break
        cv2.imshow('Imagem Original', img)
        cv2.imshow('Imagem Processada', resultado)    
    cv2.destroyAllWindows()
    
#Recebe quatro imagens e imprime na tela uma original e 3 processadas
def gera4Imagens(img, resultado1, resultado2, resultado3):
    while True:
        ch=0xFF & cv2.waitKey()
        if ch==27: # ESC key
            break
        cv2.imshow('Imagem Original', img)
        cv2.imshow('Imagem com Filtro 3x3', resultado1)    
        cv2.imshow('Imagem com Filtro 5x5', resultado2)    
        cv2.imshow('Imagem com Filtro 9x9', resultado3)    
    cv2.destroyAllWindows()
 
 
#Recebe img, e quantiza img usando K cores
def quantizacao(img, K):
    a = np.float32(img)
    bucket = 256 / K
    quantizado = (a / (256 / K))
    return np.uint8(quantizado) * bucket

#Recebe a imagem e gera o gráfico de amostragem 
def geraGraficos(img, resultado):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist1 = cv2.calcHist([resultado],[0],None,[256],[0,256])
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title("Grafico de Amostragem")
    plt.xlabel("Tons de Cinza")
    plt.ylabel("Numeros de Pixels")
    plt.xlim([0, 256])
    plt.plot(hist)
    plt.subplot(2,1,2)
    plt.title("Grafico de Quantizacao")
    plt.xlabel("Tons de Cinza")
    plt.ylabel("Numeros de Pixels")
    plt.xlim([0, 256])
    plt.plot(hist1)
    plt.show()
    
#Recebe a imagem e gera o histograma 
def geraHistograma(img):

    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.title("Histograma")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.plot(hist)
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

#Recebe duas imagens e gera dois histogramas
def geraHistogramas(img, resultado):
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title("Histograma Original")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.hist(img.ravel(), 256, [0,256])
    plt.subplot(2,1,2)
    plt.title("Histograma Equalizado")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.hist(resultado.ravel(), 256, [0,256])
    plt.show() 
    
#Recebe 4 imagens e gera 4 histogramas
def gera4Histogramas(img, resultado1, resultado2, resultado3):
    plt.figure(1)
    plt.subplot(4,1,1)
    plt.title("Histograma Original")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.hist(img.ravel(), 256, [0,256])
    plt.subplot(4,1,2)
    plt.title("Histograma Filtro 3X3")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.hist(resultado1.ravel(), 256, [0,256])
    plt.subplot(4,1,3)
    plt.title("Histograma Filtro 5X5")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.hist(resultado2.ravel(), 256, [0,256])
    plt.subplot(4,1,4)
    plt.title("Histograma Filtro 9X9")
    plt.xlabel("Intensidade")
    plt.ylabel("Frequencia")
    plt.hist(resultado3.ravel(), 256, [0,256])
    plt.show()

#Recebe uma imagem, Transforma e Gera dois gráficos, da original e da transfomada
def mostraImagensEgraficos():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)
    qntd = int(raw_input('Quantidade de tons de cores: '))
    resultado = quantizacao(img, qntd)
    geraImagens(img,resultado)
    geraGraficos(img,resultado)#Amostragem e Quantização
    opcao()
    
#Recebe a imagem e realiza o ajuste de Resolução Espacial, alterando o seu tamanho    
def ajusteResEspacial():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)
    largura = int(raw_input('Entre com a largura de pixels: '))
    altura = int(raw_input('Entre com a altura de pixels: '))
    img_redimensionada = cv2.resize(img, (largura,altura), interpolation = cv2.INTER_AREA)
    geraImagens(img, img_redimensionada)
    geraHistogramas(img, img_redimensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    opcao()
    
#Recebe a imagem, a quantidade de tons de cores e realiza o ajuste de Resolução de Intensidade, alterando a quantidade de tons da imagem    
def ajusteResIntensidade():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)
    qntd = int(raw_input('Quantidade de tons de cores: '))
    #novaImagem = str(raw_input('Digite o nome da nova imagem: '))
    resultado = quantizacao(img, qntd)
    #cv2.imwrite(novaImagem, resultado)    
    geraImagens(img,resultado) 
    geraHistogramas(img, resultado)
    opcao()

#recebe uma imagem, realiza a equalização e printa os histogramas das imagens original e equalizada 
def equalizaImagem():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)
    h_eq = cv2.equalizeHist(img)
    cv2.imwrite('imagem5.png',img)
    cv2.imwrite('imagemeq.png',h_eq)
    geraImagens(img, h_eq)
    geraHistogramas(img, h_eq)
    cv2.waitKey(0)
    opcao()

#Recebe uma imagem e gera o seu histograma
def histogramaImagem():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)
    geraImagem(img)
    geraHistograma(img)
    opcao()

#Recebe uma imagem e gera o filtro de média
def filtrodeMedia():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)    
    media3X3 = np.vstack([cv2.blur(img, (3,3))])
    media5X5 = np.vstack([cv2.blur(img, (5,5))])
    media9X9 = np.vstack([cv2.blur(img, (9,9))])
    gera4Imagens(img, media3X3, media5X5, media9X9)
    gera4Histogramas(img, media3X3, media5X5, media9X9)
    opcao()

#Recebe uma imagem e gera o filtro de mediana
def filtrodeMediana():
    imagem = str(raw_input('Imagem que deseja inserir: '))
    img = cv2.imread(imagem, 0)
    mediana3x3 = np.vstack([np.hstack([cv2.medianBlur(img,3)])])
    mediana5x5 = np.vstack([np.hstack([cv2.medianBlur(img,3)])])
    mediana9x9 = np.vstack([np.hstack([cv2.medianBlur(img,3)])])
    gera4Imagens(img, mediana3x3, mediana5x5, mediana9x9)
    gera4Histogramas(img, mediana3x3, mediana5x5, mediana9x9)
    opcao()
 
    
#Meunu de Opções
def opcao():   
    menu()
    op = int(raw_input('Digite a opção desejada: '))    
    if op == 1:
        mostraImagensEgraficos()
    elif op==2:
        ajusteResEspacial()
    elif op==3:
        ajusteResIntensidade()
    elif op==4:
        equalizaImagem()
    elif op==5:
        histogramaImagem()
    elif op==6:
        filtrodeMedia()
    elif op==7:
        filtrodeMediana()
    elif op==0:
        sys.exit(0)

if __name__ == '__main__':
   opcao()