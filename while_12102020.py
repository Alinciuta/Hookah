#print(2 > 3)
#if 2 != 3:
#    a = True
#else:
#    a = False
#print(a)
#
#a = False
#b= True
#if a is False:
#    print(a)
#
#n = input("Introduceti un numar: ")
#b = None
#if n.isdigit() and int(n) < 100:
#    b = False
#elif n.isdigit:
#    b = True
#print(b)

#nr1 = input('Introdu nr1: ')
#nr2 = input('Introdu nr2: ')
#a = None
#if nr1 > nr2:
#    a = nr1
#else:
#    a = nr2
#print(a)

#nr1 = input('Introdu nr1: ')
#nr2 = input('Introdu nr2: ')
#nr3 = input('Introdu nr3: ')
#if nr1.isdigit() and nr2.isdigit() and nr3.isdigit():
#    print(max(nr1, nr2, nr3))
#else:
#    print('Nu se poate calcula')
#
#while True:
#    print('Ruleaza')
#    break
#
#cel_mai_mare_nr = 999999
#number = input('Introdu nr: ')
#while number != -1:
#    if int(number) > int(cel_mai_mare_nr) or int(cel_mai_mare_nr) > int(number) > -1:
#        number -= 1
#    elif number < -1 and number:
#        number += 1
#        print(cel_mai_mare_nr)
#    print(number)

numar = int(input('Scrie numerele: '))
par = 0
impar = 0
while numar != 0:
    if numar % 2 == 0:
        par+= 1
    else:
        impar+= 1
    numar = int(input('Scrie numerele: '))
print('Numerele pare: {} si nr impare {}'.format(par, impar))
#12 octombrie