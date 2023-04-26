# 4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

dol = float(input("Cotação do Dólar: "))
val = float(input("Valor em dólar para conversão: "))

conv = dol * val

print(f"Valor em Reais: R${conv}")