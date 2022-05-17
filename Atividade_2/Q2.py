# ATENÇÃO COM AS ENTRADAS DE DADOS COM O COMANDO input()
# ATENÇÃO COM AS SAÍDAS DE DADOS COM O COMANDO print()
# Não esquecer de importar as bibliotecas, por exemplo:
import numpy as np
import cv2


def readImage():
    """ Função para ler uma imagem de tamanho genérico a partir do input """
    f = []
    inputLine = input()
    while inputLine:
        f.append([int(i) for i in inputLine.split(' ') if i])
        inputLine = input()
    return np.array(f).astype('uint8')


def printImage(img):
    """ Função para imprimir uma imagem a partir da matriz dada como argumento """
    [l, c] = img.shape
    st = ''
    for i in range(l):
        for j in range(c):
            st += str(img[i][j]) + ' '
        st += '\n'
    return st


def closing(img, kernel):
    """ Função que realiza o closing de uma imagem utilizando os métodos de erosão e dilatação do opencv """
    img_closing = cv2.dilate(img, kernel)
    img_closing = cv2.erode(img_closing, kernel)

    return img_closing


def main():
    # Lendo kernel
    kernel = readImage()
    
    # Lendo a imagem
    img = readImage()

    # Realizando o filtro de fechamento e imprimindo a imagem
    closing_img = closing(img, kernel)
    print(printImage(closing_img))


if __name__ == '__main__':
    main()
