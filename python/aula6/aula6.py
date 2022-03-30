conjunto = {1, 3, 5, 7, 9}

conjunto2 = {1, 2, 4, 6, 8}

conjuncao = conjunto.union(conjunto2)
print('conjução: {}' .format(conjuncao))

intercecaoConju = conjunto.intersection(conjunto2)
print('Interseção: {}' .format(intercecaoConju))

diferenca = conjunto.difference(conjunto2)
print('diferenca entre 1 e 2: {}' .format(diferenca))
diferenca2 = conjunto2.difference(conjunto)
print('diferenca entre 2 e 1: {}' .format(diferenca2))

difSimet = conjunto.symmetric_difference(conjunto2)
print('Diferença simetrica entre 1 e 2: {}' .format(difSimet))


conjunto_A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
conjunto_B = {2, 4, 6, 8}
sub_conj = conjunto_B.issubset(conjunto_A)

print('O conjunto B é um subconjunto do conjunto A? {}' .format(sub_conj))

super_conj = conjunto_A.issuperset(conjunto_B)

print('O conjunto A é um super conjunto do conjunto B? {}' .format(super_conj))


lista = {'FFVII', 'FFVII', 'Ocarina of Time',
         'Ocarina of Time', 'Kingdom Hearts'}
conj_games = set(lista)
print(conj_games)

lista_games = list(conj_games)
print(lista_games)

# conjunto.add(11)
# conjunto.discard(1)
# print(conjunto)
