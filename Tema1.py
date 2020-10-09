iterator = 0
Cuvant = input('Scrie un cuvant:\t')
print('Cuvantul tau este {}\n'.format(Cuvant))
for c in Cuvant:
    print('cuvantul', Cuvant, 'are', len(Cuvant), 'caractere\n')
    break

email = str(input('Introdu adresa ta de email:\t'))
print('Adresa introdusa este:\t{}'.format(email))
if ('@' and '.') in email:
    print('Adresa este VALIDA!')
else:
    print('Adresa GRESITA!')

telefon = input('Introdu numarul de telefon:\t')

if len(telefon) == 10:
    print('Numarul este valid')
else:
    print('Numarul introdus nu exista')

CNP = str(input('Introduceti Codul Numeric Personal:\t'))
control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
print('CNP-ul {}'.format(CNP), 'a fost introdus\n')
if len(CNP) == 13 and ('1' or '2') in CNP[0] and ('0' or '1') in CNP[3] and ('0' or '1' or '2'or '3') in CNP[5]:
    print('CNP-ul este in curs de validare...')
else:
    print('CNP gresit!')
cod = [int(i) for i in str(CNP)]
cod.pop()
final_cod = [cod[i] * control[i] for i in range(len(cod))]

adunare = sum(final_cod)
rezultat = adunare / 11
print("Se calculeaza cifra de control...")
rezultat = round(rezultat, 1)
rest = str(rezultat)
cifra_control = rest[3:]
print('Cifra de control este: ', cifra_control)
raspunsul = None
if rezultat == 10:
    raspunsul = 1
else:
    raspunsul = cifra_control

if raspunsul == CNP[12]:
    print('Felicitari! CNP-ul este corect!')
else:
    print('CNP-ul NU este valid!')
