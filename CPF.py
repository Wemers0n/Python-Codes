def programa():
    pass
    print('digite seu cpf.')
    
    n1 = int(input('digite: '))
    n2 = int(input('digite: '))
    n3 = int(input('digite: '))
    n4 = int(input('digite: '))
    n5 = int(input('digite: '))
    n6 = int(input('digite: '))
    n7 = int(input('digite: '))
    n8 = int(input('digite: '))
    n9 = int(input('digite: '))
    
    cpf(n1, n2, n3, n4, n5, n6, n7, n8, n9)
        
def cpf(n1, n2, n3, n4, n5, n6, n7, n8, n9):
    d1 = n1 * 10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 * 3 + n9 * 2
    resultado1 = d1 % 11
    soma1 = 11 - resultado1
    
    if soma1 > 9:
        soma1 = 0
        print(soma1)
    else: 
         print(soma1)
    
    d2 = n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + soma1 * 2 
    resultado2 = d2 % 11
    soma2 = 11 - resultado2
    
    if soma2 > 9:
        soma2 = 0
        print(soma2)
    else: 
        print(soma2)
    
programa()