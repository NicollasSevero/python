# cire um algoiritimo que leia um numero e mostre o dobro, triplo e raiz quadrada

n = int(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz_quadrada = n ** (1/2)

print('o dobro de {} vale {}.'.format(n,dobro))
print('o triplo de {} vale {}.'.format(n,triplo))
print('a raiza quadrada de {} vale {:.2f}.'.format(n, raiz_quadrada))