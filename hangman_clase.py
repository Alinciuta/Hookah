import random
from words import word_list


class Spanzuratoarea:

    def __init__(self):
        self.litere = ""
        self.incercari = 7
        self.cuvant = ""
        self.status_cuvant = ""
        self.status_cuvant1 = ""
        self.status_cuvant2 = ""
        self.cuvant_listat = ""
        self.indices = None
        self.litere_ok = []
        self.ghicit = None

    def get_word(self):
        self.cuvant = random.choice(word_list)
        return self.cuvant

    def play(self):
        self.status_cuvant1 = "_" * len(self.cuvant)
        self.status_cuvant = ""
        self.status_cuvant2 = list(self.status_cuvant1)
        self.status_cuvant2[0] = self.cuvant[0]
        self.status_cuvant2[-1] = self.cuvant[-1]
        self.status_cuvant = self.status_cuvant.join(self.status_cuvant2)
        self.cuvant_listat = list(self.status_cuvant)
        self.indices = [i for i, letter in enumerate(self.cuvant) if letter == self.cuvant[0]]
        for index in self.indices:
            self.cuvant_listat[index] = self.cuvant[0]
        status_cuvant = "".join(self.cuvant_listat)
        cuvant_listat = list(status_cuvant)
        indices = [i for i, letter in enumerate(self.cuvant) if letter == self.cuvant[-1]]
        for index in indices:
            cuvant_listat[index] = self.cuvant[-1]
        self.status_cuvant = "".join(cuvant_listat)
        self.ghicit = False
        self.litere_ok = [self.cuvant[0], self.cuvant[-1]]
        print('Sa incepem jocul! Ai 7 incercari pentru a ghici cuvantul')
        print(self.status_cuvant)
        while not self.ghicit and self.incercari > 0:
            print()
            print('Mai ai ', self.incercari, 'incercari')
            incearca = input("Introdu o litera: ")
            if len(incearca) == 1 and incearca.isalpha():
                if incearca in self.litere_ok:
                    print('Litera', incearca, 'a fost deja introdusa')
                elif incearca not in self.cuvant:
                    print('Litera', incearca.upper(), "nu se afla in cuvant")
                    self.incercari -= 1
                    self.litere_ok.append(incearca)
                else:
                    print("Felicitari,", incearca, "se afla in cuvant!")
                    self.litere_ok.append(incearca)
                    self.cuvant_listat = list(status_cuvant)
                    indices = [i for i, letter in enumerate(self.cuvant) if letter == incearca]
                    for index in indices:
                        cuvant_listat[index] = incearca
                    status_cuvant = "".join(cuvant_listat)
                    if "_" not in status_cuvant:
                        self.ghicit = True
            else:
                print("Incercarea nu este valida.")
            print(status_cuvant)
        if self.ghicit:
            print("Felicitari! Ai ghicit cuvantul!")
        else:
            print("GRESIT! Cuvantul tau a fost: " + self.cuvant + ". Mai mult noroc data viitoare!")

    def main(self):
        self.__init__()
        self.cuvant = self.get_word()
        self.play()
        while input("Vrei sa joci din nou? (Y / N) ").upper() == "Y":
            self.incercari = 7
            self.cuvant = self.get_word()
            self.play()


cos = Spanzuratoarea()
cos.main()
