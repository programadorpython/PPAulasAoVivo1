'''
MISSÃO 03
1.	Escreva uma f-string usando as variáveis nome_completo, endereco_completo e idade. A f-string deverá ter o
seguinte resultado: "O usuário Jefferson Santos reside no endereço Rua Marechal Floriado Peixoto, número 10,
 Curitiba - PR e sua idade é 18 anos."
'''
nome_completo = "jefferson santos"
endereco_completo = "Rua 2, 100, Curitiba - PR"
idade = 18

print(f"O usuário {nome_completo.title()} reside no endereço {endereco_completo} e sua idade é {idade} anos.")
print("O usuário " + nome_completo.title() + " reside no endereço " + endereco_completo + " e sua idade é " + str(idade) + " anos.")
print("O usuário {} reside no endereço {} e sua idade é {} anos.".format(nome_completo, endereco_completo, idade))



