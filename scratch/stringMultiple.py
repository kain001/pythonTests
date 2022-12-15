x = "*"
num1 = 1
num2 = input("Introduce el tamanio ")
for y in range(num1, int(num2)):
    print(x * y)
for j in range(int(num2), num1-1, -1):
    print(x * j)
