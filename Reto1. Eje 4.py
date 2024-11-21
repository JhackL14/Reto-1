def may_suma(lista):
    i = 1
    lista_sumas = []  
    for n in lista:
        try:                  
            lista_sumas.append(n + lista[i])
        except: IndexError       
        i += 1

    lista_organizada = sorted(lista_sumas)
    print(f'suma mayor de numeros consecutivos {lista_organizada[-1]}')
    #print(lista_sumas)

lista_numeros=[5,4,7,1]
may_suma(lista_numeros)