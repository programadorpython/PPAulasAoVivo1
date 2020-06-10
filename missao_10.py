'''
MISSÃO 10
1.	Mostre com print uma lista de números de 1 a 50.
'''

numeros_50 = list(range(1, 51))

for num in numeros_50:
    print(num)

'''
2. Mostre com print uma lista de números de 1 a 1000.
'''
numeros_1000 = list(range(1, 1001))

# for num in numeros_1000:
#     print(num)

'''
3. Nesta lista até 1000, use as funções min, max e sum e print os seus valores para ter certeza que a lista esta certa.
'''
print()
print(min(numeros_1000))
print(max(numeros_1000))
print(sum(numeros_50))  # Função de somar na lista

'''
4. Crie uma lista de números pares numa sequência de 1 a 40.
'''
print()
lista_pares = list(range(1, 41))

for par in lista_pares:
    if par % 2 == 0:
        print(par)
    else:
        continue

# for par in lista_pares:
#     print(par)


'''
5. Crie uma lista de números ao quadrado de 1 ate 10.
'''
print()
lista_quadrados = []

INICIAL = 3
FINAL = 15

for numero in range(INICIAL, FINAL):
    quadrado = numero ** 3
    lista_quadrados.append(quadrado)

for num in lista_quadrados:
    print(num)







