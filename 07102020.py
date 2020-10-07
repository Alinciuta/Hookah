print('Primul mesaj')
a = input('apasa tasta r')
print(a)
print('Elevul "X" nu are tema')
print("Elevul 'x' nu are tema")
print('Ana are mere \n ion')
print("""
\tAna are mere
Petre e acasa
""")
variabila1 = 1
variabila2 = 2
variabila3 = f"Ana are {variabila1} mar si {variabila2} pere"
print(variabila3)
variabila4 = "Ana are {1} mar si {0} prune".format(variabila1, variabila2)
print(variabila4)
variabila5 = "Ana are {1} mar si {1} prune".format(variabila1, variabila2)
print(variabila5)
variabila2 = 3
print("variabila4 =>>", type(variabila4))
print("variabila2 =>>", type(variabila2))
variabila6 = "Ana are " + str(variabila2) + "mere"
print(type(variabila6))
print(variabila1 + variabila2)
print(str(variabila1) + str(variabila2))

print(variabila1 - variabila2)

variable_nr_1 = 3 - 2j
print(variable_nr_1.real)
print(variable_nr_1.imag)
print(variable_nr_1.conjugate())
