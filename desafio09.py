#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Informe um número inteiro: '))
print(f'TABUADA DO NÚMERO {numero}')
for i in range(1,11):
    print(numero, '*',i,'=', (numero*i))