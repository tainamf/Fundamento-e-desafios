#crie um algoritmo que leia um valor em metros e exiba convertido em centímetros e milimetros
metros = float(input('qual o valor em metros você quer converter? '))
centimetro = metros * 100
milimetros = metros * 1000
print(f'o valor de {metros}M em centímetros é: {centimetro} \nE em milímetros é: {milimetros}')