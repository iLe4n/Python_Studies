ListaNumero = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

somarPares = 0 

for numero in ListaNumero: 
    if (numero % 2 == 0):
        somarPares += numero 

print(f'A soma de todos os números pares são de {somarPares}')