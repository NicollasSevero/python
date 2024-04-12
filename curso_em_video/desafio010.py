#  Crie um programa que leia quanto uma pessoa tem na carteira em mostre quantos dolares ela pode comprar. Considere US$ 1,00 = R$ 3,27

carteira = float(input('Quanto você tem na carteira? R$'))

dolar = carteira / 3.27

print('Você pode comprar U${:.2} em dolar.'.format(dolar))