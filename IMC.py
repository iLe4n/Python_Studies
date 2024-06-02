peso = int(input(f'Por favor digite seu peso: \n'))
while peso == 0:
    print(f'Por favor, digite o peso da forma correta:')
    peso = int(input(f'Por favor digite seu peso: \n'))
else:
    print(f'Seu peso é {peso}kg')

altura = float(input(f'Agora, digite sua altura: \n'))
while altura == 0:
    print(f'Por favor, digite a altura da forma correta:')
    altura = int(input(f'Agora, digite sua altura: \n'))
else:
    print(f'Sua altura é {altura}')

IMC = altura**2 / peso
print(f'Seu IMC é {IMC}')