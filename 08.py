# 8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = (numero1 + numero2) / (numero1 - numero2)

print("O resultado da divisão da soma pela subtração é:", resultado)