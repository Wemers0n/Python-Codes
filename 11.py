# 11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

numero = input("Digite um número inteiro de 3 dígitos: ")

inverso = int(numero[::-1]) # ::-1 -->> fatiamento em sequencia, escrever em ordem inversa

print(f"O inverso de {numero} é {inverso}.")