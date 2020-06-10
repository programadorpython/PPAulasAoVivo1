'''
MISSÃO 14
1.	Crie uma lista de 5 nomes de fruta:
'''
lista_frutas = ['pera', 'limão', 'maça', 'laranja', 'banana']

'''
a. Se a fruta for limão, escreva a mensagem: "Vamos fazer uma limonada?"
b. Se não for, escreva: "Vamos ficar sem suco hoje"
'''
for fruta in lista_frutas:
    if fruta == 'limão':
        print("Vamos fazer uma limonada?")
    else:
        print("Vamos ficar sem suco hoje")

'''
1.	Da mesma lista, adicione um if pra garantir que não esteja vazia
a. Se estiver vazia mostre a mensagem "Vamos a feira!"
b. Remova todas as frutas e faça a mensagem acima ser exibida.
'''
print()
# lista_frutas = []

if lista_frutas:
    for fruta in lista_frutas:
        if fruta == 'limão':
            print("Vamos fazer uma limonada?")
        else:
            print("Vamos ficar sem suco hoje")
else:
    print("Vamos a feira!")


'''
1.	Crie 2 listas. Primeira com estoque_frutas e adicione 5 frutas e crie outra com o nome lista_de_compras
e adicione 3 frutas sendo que 1 não tem no estoque_frutas
a. Percorra a lista lista_de_compras e verifique se tem no estoque_frutas. Se tiver, mostre a mensagem
"Comprando a fruta x", se não "Vamos comprar na proxima vez"
'''
print()
estoque_frutas = ['Limão', 'pera', 'maça', 'laranja', 'banana']
lista_de_compras = ['limão', 'abacate', 'pera']

estoque_frutas_lower = [fruta.lower() for fruta in estoque_frutas]

print(estoque_frutas_lower)

for fruta in lista_de_compras:
    if fruta.lower() in estoque_frutas_lower:
        print(f"Comprando a fruta {fruta.title()}.")
    else:
        print(f"Vamos comprar {fruta.title()} na próxima vez.")


'''
1.	Crie uma lista de números usando função range() de 70 a 100
2.	numbers = list(range(70,101))
3.	
4.	Percorra a lista usando for loop
5.	for number in numbers:
6.	
6. Use if-elif-else para quem tirar nota abaixo de 70 receba a mensgem "Sua nota é F",
se tirar abaixo de 80 "Sua nota é C", se tirar menor que 90 "Sua nota é B" e se nenhuma delas, "sua nota é A"
'''
print()
notas = list(range(69, 101))

for nota in notas:
    if nota < 70:
        print(f"Sua nota {nota} é F.")
    elif nota < 80:
        print(f"Sua nota {nota} é C.")
    elif nota < 90:
        print(f"Sua nota {nota} é B.")
    else:
        print(f"Sua nota {nota} é A.")






