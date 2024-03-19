# Faça um programa que leia a largura e a altura de uma parede em metros, cacule a sua area e quantidade de tinta necessario para pinta-lo, sabendo que cada litro de tinta, pinta uma area de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
tinta = area/2

print('a dimensão da parede é de {}X{} e a sua àrea é de {}m²3.\n Portanto vai ser gasto um total de {}lts de tinta.'.format(larg,alt,area,tinta))