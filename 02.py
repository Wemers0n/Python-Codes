# 2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

v_horas = int(input("Horas: "))
v_min = int(input("Minutos: "))

minutos = (v_horas * 60) + v_min

print(f"Equivalente em minutos {minutos}")