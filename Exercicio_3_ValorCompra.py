
#Implementar uma solução em Python que resolva a seguinte questão: 

#Calcular o valor de uma compra, sendo que o preço unitário é de R$10,00
#Se for feita uma compra de até 10 unidades, não há descontos. 
#Para compras entre 11 e 20 unidades é dado um desconto de 10%. 
#Acima de 20 unidades, é dado um desconto de 20%. 


ComprasAoTodo = int(input(f'Por favor, digite qual foi a quantidade de produtos comprados: '))

if (ComprasAoTodo <= 10): 
    valorTotal = ComprasAoTodo*10 
    print(f'Não existe desconto, e o seu valor total foi de {valorTotal}')
     
elif (ComprasAoTodo <=20 ):
    valorTotal = ComprasAoTodo*10
    PorcentualDoDesconto = 10 
    desconto = (PorcentualDoDesconto / 100 ) *valorTotal
    ValorComDesconto = valorTotal - desconto
    
    print(f'Pela realização da compra de {ComprasAoTodo} produtos, você terá direito a um desconto de 10%. O valor da sua compra 
          foi de {ValorComDesconto} reais. ')
    
else: 
    valorTotal = ComprasAoTodo*10 
    PorcentualDoDesconto = 20 
    desconto = (PorcentualDoDesconto / 200) *valorTotal
    ValorComDesconto = valorTotal - desconto
    print(f'Pela realização da compra de {ComprasAoTodo} produtos, você terá direito a um desconto de 20%. O valor da sua compra foi de {ValorComDesconto} reais.')
    
