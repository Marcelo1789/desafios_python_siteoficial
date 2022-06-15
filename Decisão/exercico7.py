num1= input("digite o 1º numero: ")
num2 = input("digite o 2º numero: ")
num3 = input("digite o 3º numero: ")
if num1 > num2 and num3 < num2:
    print (num1,'-', num3)
elif num2 > num3 and num1 < num3:
    print(num2, '-', num1)
else:
    print(num3,'-', num2)