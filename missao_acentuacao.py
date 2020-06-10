# Precisa instalar este módulo. Ex: pip install unidecode
import unidecode

# Lista com palavras acentuadas
palavra_com_acento = 'programação'


def para_ascii(palavra):
    """
    Recebe uma palavra acentuada e retorna sem acentos (em ascii)
    :param palavra:
    :return: palavra_modificada
    """
    palavra_modificada = unidecode.unidecode(palavra)
    return palavra_modificada


print()
print(f"Palavra com acento: {palavra_com_acento}")
print(f"Palavra sem acento: {para_ascii(palavra_com_acento)}")
