# escreva um progama que leoa o valor em metros e o exiba convertido em centimetros e milimetros

m = float(input('Digite a metragem da casa: '))

km = m / 1000
hm = m / 100
dam = m / 10

dm =  m * 10
cm =  m * 100
mm = m * 1000

print('a metragem {} equivale a: \n {}km\n {}hm\n {}dam\n {}dm\n {}cm1\n {:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))