# 10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))

quociente = a // b
resto = a % b

if resto == 0:
    print(f"O quociente da divisão de {a} por {b} é {quociente} e o resto é igual a 0.")
else:
    print(f"O quociente da divisão de {a} por {b} é {quociente} e o resto é {resto}.")


