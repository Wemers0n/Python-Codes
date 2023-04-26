# 6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. 
# (Vm/s = Vkm/h / 3.6)

a = int(input("Velocidade em Km/h: "))

conv = a // 3.6

print(f"{conv} m/s")