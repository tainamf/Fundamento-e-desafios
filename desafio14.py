# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.CALCULO -> F = (C * 1,8) + 32
celsius = float(input('Informe a temperatura em °C: '))
f = (celsius * 1.8) + 32
print(f'A temperatura de {celsius}°C convertida em Fahrenheit é: {f}°F. ')
