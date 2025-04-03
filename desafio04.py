#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivéis sobre ele.

a = input('digite algo: ')
print('o tipo primitivo desse valor é: ', type(a))
print('só tem espaços? ', a.isspace())
print('só tem letras? ', a.isalpha())
print('só tem números? ', a.isnumeric())
print('é alfanumérico? ', a.isalnum())
print('é todo maiusculo? ', a.isupper())
print('é todo minusculo? ', a.islower())
print('é capitalizada?(letras minusculas e maiuscula)? ', a.istitle())