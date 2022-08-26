def  programa ():
    qtd_elementos =  int ( input ( ' Qtd elementos na seq.FB? ' ))

    penultimo =  0
    ultimo =  1
    contador =  2

    print (penúltimo, final = '  ' )
    print (último, fim = '  ' )

    while contador < qtd_elementos:
        # trabalhos do WHILE
        atual = penúltimo + último
        print (atual, fim = '  ' )
        penúltimo = último
        ultimo = atual

        # convergencia
        contador = contador +  1

    print ()


programa ()