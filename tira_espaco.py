frase = input('digite uma frase: ')

def remove_espaco(frase):
    resultado = ""
    for caracter in frase:
        if caracter != ' ':
            resultado += caracter
    return resultado
print(remove_espaco(frase))

