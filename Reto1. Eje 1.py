def operaciones_basicas(num1, operdador, num2):
    
    operacion = str(num1) + operdador + str(num2)
    resultado = eval(operacion)
    return resultado

print(operaciones_basicas(1, '*', 2))