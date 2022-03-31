from multiprocessing.spawn import _main
from tkinter.tix import MAIN
from unicodedata import name

from pip import main


def cont_letras(palavras):

    cont = []

    for x in palavras:
        qtd = len(x)
        cont.append(qtd)

    return cont


if __name__ == '__main__':
    lista = ('paralelepipedo', 'pedra')
    print(cont_letras(lista))
