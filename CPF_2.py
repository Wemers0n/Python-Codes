cpf = input('digite o numero do seu cpf: \n>>>')

lista = [int(cpf[0]), int(cpf[1]), int(cpf[2]), int(cpf[3]), int(cpf[4]), int(cpf[5]), int(cpf[6]), int(cpf[7]), int(cpf[8])]

def cpf(cpf):
    soma1 = cpf[0] * 10 + cpf[1] * 9 + cpf[2] * 8 + cpf[3] * 7 + cpf[4] * 6 + cpf[5] * 5 + cpf[6] * 4 + cpf[7] * 3 + cpf[8] * 2 
    dig1 = 11 - (soma1 % 11)
    if dig1 > 9:
        dig1 = 0
    else:
        dig1
        
    soma2 = cpf[0] * 11 + cpf[1] * 10 + cpf[2] * 9 + cpf[3] * 8 + cpf[4] * 7 + cpf[5] * 6 + cpf[6] * 5 + cpf[7] * 4 + cpf[8] * 3 + dig1 * 2
    dig2 = 11 - (soma2 % 11)
    if dig2 > 9:
        dig2 = 0     
    else:
        dig2
    
    print('O cpf digitado termina em:')
    print('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(cpf[0], cpf[1], cpf[2], cpf[3], cpf[4], cpf[5], cpf[6], cpf[7], cpf[8], dig1, dig2))

cpf(lista)