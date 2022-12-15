num1 = input("introduce el primer número")


def check_interval(x):
    if x in range(0, 11):
        return print("El valor dado esta entre 0 y 10")
    else:
        return print("El valor dado no esta entre 0 y 10")


check_interval(int(num1))
