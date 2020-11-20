# def message():
#     print('Numarul introdus este 2')
#
#
# message()
# message = 1
# print(message)
#
# def message(numar_1, numar_2): #sau message(numar2=3, numar_1=50)
#     print(f'Numarul introdus este {numar_1} si celalalt nr este {numar_2}')
#
#
# message(3, 50) #sau message(numar2=3, numar_1=50)

# def suma(a: int, c: int, b: int = 2) -> (list, int):
#     """
#
#     :param a:
#     :param c:
#     :param b:
#     :return: lista de suma, diferenta
#     """
#     return [a + b + c], a - b - c
#
# valoare_suma, valoare_dif = suma(1, 2)
# print(valoare_suma, valoare_dif)

# def inmultire(a: int, b: int) -> (bool, int):
#     rezultat = a * b
#     return True, rezultat
#
# print(inmultire(1, 2))

def listare(a: bool, b: bool) -> bool:
    if a is True:
        return True
    if b is False:
        return False

print(listare(False, False))

def printare(a, b):
    listare(a, b)
    return 'Executat cu succes'

print(printare(True, False))
