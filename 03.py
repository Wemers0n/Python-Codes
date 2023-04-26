# 3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

v_min = int(input("Minutos: "))

horas = v_min // 60
minutos = v_min % 60

print(f"{horas} Horas e {minutos} minutos")