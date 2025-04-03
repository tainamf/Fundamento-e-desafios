#faça um algoritmo que leia o preço de um produto e mostre seu novo valor. com 5% de desconto
valor_antigo = float(input('Informe o valor em reais que irá receber o desconto: '))
valor_novo = valor_antigo - (valor_antigo * 5 / 100)
print(f'O novo valor com desconto de 5% é : R$ {valor_novo}')
