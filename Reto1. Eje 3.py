import math as mt
def primo(lista):
    for n in lista:
       si =  mt.factorial(n-1)
       primo = si + 1
       if primo % n == 0:
        print('es primo')
       else: 
        print('no es primo')
    

lista_numeros = (6,7,9,11)

primo(lista_numeros)