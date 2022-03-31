lista = [1, 10]

try:
    divi = 255 / 0
    #numero = lista[3]
    #x = y
except ZeroDivisionError:
    print('Erro: Impossível realizar divisão por 0')
except IndexError:
    print("Erro: indice invalido")
except BaseException as ex:
    print("Erro desconhecido. Erro: {}" .format(ex))
else:
    print('Executado quando não ocorre excessão')
