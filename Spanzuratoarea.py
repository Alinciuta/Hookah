import random
from words import word_list


def get_word():
    cuvant = random.choice(word_list)
    return cuvant


def play(cuvant):
    status_cuvant1 = '_' * len(cuvant)
    status_cuvant = ""
    status_cuvant2 = list(status_cuvant1)
    status_cuvant2[0] = cuvant[0]
    status_cuvant2[-1] = cuvant[-1]
    status_cuvant = status_cuvant.join(status_cuvant2)

    cuvant_listat = list(status_cuvant)
    indices = [i for i, letter in enumerate(cuvant) if letter == cuvant[0]]
    for index in indices:
        cuvant_listat[index] = cuvant[0]
    status_cuvant = "".join(cuvant_listat)
    cuvant_listat = list(status_cuvant)
    indices = [i for i, letter in enumerate(cuvant) if letter == cuvant[-1]]
    for index in indices:
        cuvant_listat[index] = cuvant[-1]
    status_cuvant = "".join(cuvant_listat)

    ghicit = False
    litere_ok = [cuvant[0]]
    cuvinte_ok = []
    incercari = 7
    print('Sa incepem jocul! Ai 7 incercari pentru a ghici cuvantul')
    print(display_hangman(incercari))
    print(status_cuvant)
    while not ghicit and incercari > 0:
        incearca = input("Introdu o litera: ")
        if len(incearca) == 1 and incearca.isalpha():
            if incearca in litere_ok:
                print('Litera', incearca, 'a fost deja introdusa')
            elif incearca not in cuvant:
                print('Litera', incearca.upper(), "nu se afla in cuvant")
                incercari -= 1
                litere_ok.append(incearca)
            else:
                print("Felicitari,", incearca, "se afla in cuvant!")
                litere_ok.append(incearca)
                cuvant_listat = list(status_cuvant)
                indices = [i for i, letter in enumerate(cuvant) if letter == incearca]
                for index in indices:
                    cuvant_listat[index] = incearca
                status_cuvant = "".join(cuvant_listat)
                if "_" not in status_cuvant:
                    ghicit = True
        # elif len(incearca) == len(cuvant) and incearca.isalpha():
        #     if incearca in cuvinte_ok:
        #         print("Deja ai ghicit cuvantul", incearca)
        #     elif incearca != cuvant:
        #         print(incearca, "Nu este cuvantul tau.")
        #         incercari -= 1
        #         cuvinte_ok.append(incearca)
        #     else:
        #         ghicit = True
        #         status_cuvant = cuvant
        else:
            print("Incercarea nu este valida.")
        print(display_hangman(incercari))
        print(status_cuvant)
    if ghicit:
        print("Felicitari! Ai ghicit cuvantul!")
    else:
        print("GRESIT! Cuvantul tau a fost" + cuvant + ". Mai mult noroc data viitoare!")


def display_hangman(incercari):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        """,

                """
        - -------
        | 
        |
        |
        |
        |
        """
]
    return stages[incercari]


def main():
    cuvant = get_word()
    play(cuvant)
    while input("Vrei sa joci din nou? (Y / N) ").upper() == "Y":
        cuvant = get_word()
        play(cuvant)


if __name__ == "__main__":
    main()
