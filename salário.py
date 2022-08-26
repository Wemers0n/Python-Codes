def programa():
	salario = float(input('Salário: '))
	
	reajuste = calcular_aumento(salario)
	
	novo_salario = salario + reajuste
	
	print('Novo_Salario = R$ %.2f' % novo_salario)
	
	
def calcular_aumento(salario):
	if salario <= 280:
			return salario * (220/100)
	elif salario > 280 and salario <= 700:
			return salario * (15/100)
	elif salario > 700 and salario <= 1500:
			return salario * (10/100)
	else:
			return salario * (5/100)
		

programa()