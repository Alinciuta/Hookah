import datetime
import math

iterator = 0
caractere = 0
count = ""
total = None
cuvant = str(input('Sir de caractere:\t'))
for i in cuvant.replace(' ', ''):
    caractere += 1
    count += i
print('\t', caractere, "caractere sunt in acest sir\n")

email = str(input('Introdu adresa ta de email:\t'))
print('Adresa introdusa este:\t{}'.format(email))
if ('@' and '.') in email and email.count('@') == 1 and email.count('.') == 1:
    print('Adresa este VALIDA!')
else:
    print('Adresa GRESITA!')

telefon = str(input('Introdu numarul de telefon:\t'))
tada = [int(i) for i in str(telefon)]
if telefon.isdigit() == True and len(telefon) == 10 and tada[0] == 0:
    print('Numarul este valid')
else:
    print('Numarul introdus nu exista')

numar_control = None
cnp1 = str(input('Introduceti Codul Numeric Personal:\t'))
cnp = [int(i) for i in str(cnp1)]
cod = [int(i) for i in str(cnp1)]
gresit = 'CNP-ul introdus este GRESIT'
control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
an = None
an1 = cnp1[1:3]
if int(an1) in range(25):
    an = '20'+an1
else:
    an = '19'+an1
luna = cnp1[3:5]
zi = cnp1[5:7]
data = an+'-'+luna+'-'+zi
print(' Data nasterii tale este:\t', data)
format = '%Y-%m-%d'
try:
    datetime.datetime.strptime(data, format)
    print('Data nasteriitale este corecta')
except ValueError:
    print('Data nasterii tale este GRESITA')
if cnp1.isdigit() == False or len(cnp) != 13 or int(cnp[0]) < 1 or int(cnp[0]) > 9:
    print(gresit)
elif int(cnp[7]) not in range(0, 5):
    print(gresit)
elif int(cnp[7]) == 4 and int(cnp[8]) not in range(0, 6):
    print(gresit)
elif int(cnp[7]) == 5 and int(cnp[8]) not in range(1, 2):
    print(gresit)
else:
    cod.pop()
    final_cod = [cod[i] * control[i] for i in range(len(cod))]
    adunare = sum(final_cod)
    rezultat = adunare / 11
    #rezultat = round(rezultat, 2)
    rest = str(rezultat)
    numar_control = rest[1:]
    k = float(numar_control)
    def round_up(n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier
    numar_control2 = round_up(k, 1)
    numar_control_3_3 = str(numar_control2)
    cifra_control_ok = numar_control_3_3[2:]
    print('Cifra de control este: ', cifra_control_ok)
    raspunsul = None
if cifra_control_ok == cnp1[12]:
    print('CNP-ul este VALID')
else:
    print('CNP-ul NU este valid!')
