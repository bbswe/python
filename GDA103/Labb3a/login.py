def hantera_användare(användarnamn, lösenord):
    rätt_användarnamn = "admin"
    rätt_lösenord = "admin"
    loggedIn = False

    if användarnamn != rätt_användarnamn and lösenord != rätt_lösenord:
        print("Misslyckad inloggning!")
        return False
    else:
        print(f"Du är inloggad som: {användarnamn}")
        return True

def misslyckat_försök(försök, max_försök):
    if försök >= max_försök:
        print("För många misslyckade inloggningar!")
        return False
    return True

def hantera_inloggning(användarnamn, lösenord, misslyckade_försök, max_försök):
    if not misslyckat_försök(misslyckade_försök, max_försök):
        return False

    if hantera_användare(användarnamn, lösenord):
        print(f"Inloggning lyckades, välkommen {användarnamn}!")
        exit()

    misslyckade_försök += 1
    print(f"Inloggningsförsöket misslyckades, du har gjort {misslyckade_försök} av {max_försök} försök!")
    return misslyckade_försök

def frågor():
    print("\nAnge en siffra som motsvarar ett val")
    print("1. Hej")
    print("2. Mönster")
    print("3. Avancerat Mönster")
    print("4. Login")

def meny():
    misslyckade_försök = 0
    max_försök = 3

    while True:
        frågor()
        val = int(input("Ange siffra: "))
        if val == 1:
            namn = input("Ange namn: ")
            print(f"Hej {namn}! Trevligt att ses!")

        elif val == 2:
            for i in range(6, 0, -1): # Vi lägger till +1 stjärna för 6-6=0 +1
                print(f"{i} " + "\t*" * (6-i+1))

        elif val == 3:
            for i in range(6, 0, -1): # Vi lägger till "tabs" för mängden * som saknas medan i minskar
                print("\t" * (i-1) + "*\t" * (6-i+1), i) # samtidigt så lägger vi även till stjärnor medan i minskar

        elif val == 4:
            while misslyckade_försök < max_försök or hantera_användare(användarnamn):
                användarnamn = input("Ange namn: ")
                lösenord = input("Ange lösenord: ")

                misslyckade_försök = hantera_inloggning(användarnamn,lösenord,misslyckade_försök,max_försök)
            break
        else:
            print("Du är ute och cyklar")
            break

if __name__ == "__main__":
    meny()