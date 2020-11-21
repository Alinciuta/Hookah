class Joc:
    def __init__(self):
        self.tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.cond_castig = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6))
        self.nr_mutari = 0

    def tabla_joc(self):
        print()
        print(self.tabla[0], self.tabla[1], self.tabla[2])
        print(self.tabla[3], self.tabla[4], self.tabla[5])
        print(self.tabla[6], self.tabla[7], self.tabla[8])
        print()


    def jucator_1(self):
        try:
            print("Jucatorul X")
            move = int(input("Alegeti pozitia dvs: "))
            if self.tabla[move] != 'X' and self.tabla[move] in range(9):
                self.tabla[move] = 'X'
                self.tabla_joc()
                self.nr_mutari += 1
            else:
                print("Pozitia este ocupata!" )
                self.jucator_1()
            self.check_win()
        except ValueError:
            print('Alegeti un numar de la 0 la 8')
            self.jucator_1()
        except IndexError:
            print('Alege un o pozitie valida!')
            self.jucator_1()

    def jucator_2(self):
        try:
            print("Jucatorul O")
            move = int(input("Alegeti pozitia dvs: "))
            if self.tabla[move] != 'O' and self.tabla[move] in range(9):
                self.tabla[move] = 'O'
                self.tabla_joc()
                self.nr_mutari += 1
            else:
                print("Pozitia este ocupata!" )
                self.jucator_2()
            self.check_win()
        except ValueError:
            print('Alegeti un numar de la 0 la 8')
            self.jucator_2()
        except IndexError:
            print('Alege un o pozitie valida!')
            self.jucator_2()

    def check_win(self):
        for a in self.cond_castig:
            if self.tabla[a[0]] == self.tabla[a[1]] == self.tabla[a[2]] == 'X':
                print('Jucatoul_1 a castigat!')
                self.joaca_din_nou()
            elif self.tabla[a[0]] == self.tabla[a[1]] == self.tabla[a[2]] == 'O':
                print('Jucatoul_2 a castigat!')
                self.joaca_din_nou()
            elif self.nr_mutari == 9:
                print("Egalitate!")
                self.joaca_din_nou()


    def set_joc(self):
        while True:
            self.jucator_1()
            self.jucator_2()


    def incepe_jocul(self):
        self.tabla_joc()
        self.set_joc()

    def reset(self):
        for i in range(8):
            self.tabla[i] = i

    def joaca_din_nou(self):
        self.reset()
        while True:
            ask = input("Vrei sa joci din nou?  Y or N \n")
            if ask == 'Y':
                self.incepe_jocul()
            elif ask == 'N':
                quit()
            else:
                print('Raspuns invalid')
                quit()

cos = Joc()
cos.incepe_jocul()
