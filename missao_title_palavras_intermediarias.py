def upper_intermediarios(frase):
    nao_upper = ["de", "do", "da", "sou", "é", "são", "e", "", "em", "no", "na", "para", "um", "uma"]
    palavras_string = frase.split()

    # junte coisas usando '', que foi removido por split () acima
    # use um ternário para decidir se algo precisa de capitalização usando .title ()
    # se estiver no nao_upper: use como está, caso contrário, use v.title ()
    return ' '.join(pal_int if pal_int in nao_upper else pal_int.title() for pal_int in palavras_string)


cidade = "rio de janeiro."

print(cidade)
print()
print(upper_intermediarios(cidade))
