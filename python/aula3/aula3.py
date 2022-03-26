#a = int(input('primeiro valor: '))
#b = int(input('segundo valor: '))
#c = int(input('terceiro valor: '))

# if a > b and a > c:
#    print('o maior número é {}' .format(a))
# elif b > a and b > c:
#    print('o maior número é {}' .format(b))
# else:
#    print('o maior número é {}' .format(c))
#print('final do programa')

#a = int(input('Insira o primeiro valor: '))
#b = int(input('Insira o segundo valor: '))
#resto_a = a % 2
#resto_b = b % 2;
#
# if resto_a == 0 or resto_b == 0:
#    print('pelo menos um dos valores é par')
# else:
#    print('nenhum valor digitado é par')

print('Insira as notas do aluno de acordo com o bimestre:\n')
nota1 = int(input('Primeiro bimestre: '))
if nota1 > 10 or nota1 < 0:
    print('Valor inserido invalido, tente novamente')
    nota1 = int(input('Primeiro bimestre: '))
nota2 = int(input('Segundo bimestre: '))
if nota2 > 10 or nota2 < 0:
    print('Valor inserido invalido, tente novamente')
    nota2 = int(input('Segundo bimestre: '))
nota3 = int(input('Terceiro bimestre: '))
if nota3 > 10 or nota3 < 0:
    print('Valor inserido invalido, tente novamente')
    nota3 = int(input('Terceiro bimestre: '))
nota4 = int(input('Quato bimestre: '))
if nota4 > 10 or nota4 < 0:
    print('Valor inserido invalido, tente novamente')
    nota4 = int(input('Quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7 and media <= 10:
    print('Aluno aprovado por nota com media de: {}' .format(media))
elif media >= 4 and media < 7:
    print('Aluno de recuperação, sua media é {}' .format(media))
elif media < 4 and media >= 0:
    print('Aluno reprovado, sua media é {}' .format(media))
else:
    print('Algum valor digitado é invalido, tente novamente')
