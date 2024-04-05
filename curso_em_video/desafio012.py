# faça um algoritimo que leia o preço de um produtoe mostre seu novo preço com 5%, 7% e 10% de desconto

num = float(input('Digite o valor do produto: '))
desc1 = num - (num*0.05)
desc2 = num - (num*0.07)
desc3  = num - (num*0.1)

print('O valor do produto de R${:.2f}, com 5% de desconto fica no valor de R${:.2f}'.format(num,desc1))
print('O valor do produto de R${:.2f}, com 7% de desconto fica no valor de R${:.2f}'.format(num,desc2))
print('O valor do produto de R${:.2f}, com 10% de desconto fica no valor de R${:.2f}'.format(num,desc3))