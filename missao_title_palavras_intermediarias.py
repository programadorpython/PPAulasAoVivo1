def upper_intermediarios(frase):
    """
    Junta palavras usando ' ', que foi removido por split() abaixo
    Usa um if e else para decidir se algo precisa de capitalização usando .title()
    :param frase: Uma string qualquer
    :return: Se estiver na lista nao_upper: use como está, caso contrário, use pal_int.title()
    """
    nao_upper = ["de", "do", "da", "sou", "é", "são", "e", "em", "no", "na", "para", "um", "uma"]
    palavras_string = frase.split()
    return ' '.join(pal_int if pal_int in nao_upper else pal_int.title() for pal_int in palavras_string)


cidade = "rio de janeiro"

print()
print(f"String original acima: \t\t\t\t\t\t\t{cidade}")
print(f"String modificada, mantendo o 'de' minúsculo: \t{upper_intermediarios(cidade)}")
