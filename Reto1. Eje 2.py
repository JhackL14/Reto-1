def palindromo(palabra):
    i = -1
    prueba_palindromo = 0 
    for n in palabra:
        if palabra[i] == n:
            i -= 1
            prueba_palindromo += 1
        else: 
            print('no es un palindromo')
            break
        if prueba_palindromo == len(palabra):
            print('Es un palindromo')
    

