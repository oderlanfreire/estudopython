# Primeiro codigo

#a = int(input('Insira um número: '))

#cont = 0

# for x in range(1, a + 1):
#    resto = a % x
#    print('{a} / {x} = {resto}' .format(a=a, x=x, resto=resto))
#    if resto == 0:
#        cont = cont + 1

# if cont == 2:
#    print('O número {} é primo' .format(a))
# elif cont > 2:
#    print('O númeo {} não é primo' .format(a))

# Segundo codigo

#n = int(input("Insira um número: "))

# for num in range(n+1):
#    cont = 0
#    for x in range(1, num + 1):
#        resto = num % x
#        if resto == 0:
#            cont = cont + 1
#    if cont > 0 and cont <= 2:
#        print(num)


# Terceiro codigo

#k = 0

# while (k < 10):
#    print(k)
#    k = k + 1

nota1 = int(input("Insira a primeira nota do aluno: "))
while nota1 > 10:
    nota1 = int(input("Nota invalida, insira a primeira nota correta: "))

while nota1 < 0:
    nota1 = int(input("Nota invalida, insira a primeira nota correta: "))

nota2 = int(input("Insira a segunda nota do aluno: "))
while nota2 > 10:
    nota2 = int(input("Nota invalida, insira a segunda nota correta: "))

while nota2 < 0:
    nota2 = int(input("Nota invalida, insira a segunda nota correta: "))

nota3 = int(input("Insira a terceira nota do aluno: "))
while nota3 > 10:
    nota3 = int(input("Nota invalida, insira a terceira nota correta: "))

while nota3 < 0:
    nota3 = int(input("Nota invalida, insira a terceira nota correta: "))

nota4 = int(input("Insira a quarta nota do aluno: "))
while nota4 > 10:
    nota4 = int(input("Nota invalida, insira a quarta nota correta: "))

while nota4 < 0:
    nota4 = int(input("Nota invalida, insira a quarta nota correta: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A media do aluno é: {}" .format(media))
