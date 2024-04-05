#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input("Informe a temperatura em ºC: "))
fire = ((9*temp)/5) + 32
        
print('A temperatura de {}ºC corresponde a {} F!'.format(temp, fire))