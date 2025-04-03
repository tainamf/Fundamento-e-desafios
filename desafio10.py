#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar (considere que 1 dólar = 5,76)-> na data de hoje: 29/03/2025
real = float(input('Digite o valor em REAIS(R$): '))
print(f'o valor de R$ {real} em dólares(US$) será: {real/5.76:.2f}')
