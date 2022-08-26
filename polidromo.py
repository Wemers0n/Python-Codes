frase = input('Digite um frase: ')

def inverter(frase):
    resultado = ""
    for caracter in frase:
            resultado = caracter + resultado
    return resultado

def eh_polidromo(frase):
    return frase.upper() == inverter(frase).upper()


if eh_polidromo(frase):
    print(frase, 'é um polidromo.')
else:
    print(frase, 'Não é polidromo.')