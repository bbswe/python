"""
def inloggnings_funktion(användarnamn, lösenord, misslyckade_försök, max_misslyckade_försök):
    försök = misslyckade_försök
    max_försök = max_misslyckade_försök
    rätt_användarnamn = "admin"
    rätt_lösenord = "admin"

    if försök < max_misslyckade_försök:
        if användarnamn is None:
            användarnamn = input("Ange ditt namn: ")
            if användarnamn == rätt_användarnamn:
                if lösenord != rätt_lösenord and försök < max_försök:
                    print("Fel lösenord")
                    försök = försök + 1
                    print(f"Du har {försök} av {max_försök} kvar")
                    return försök
                else:
                    print(f"Välkommen in {användarnamn}")
                    return True
            else:
                if försök < max_försök:
                    print("Fel användarnamn")
                    försök = försök + 1
                    print(f"Du har {försök} av {max_försök} kvar")
                    return försök
                exit()"""

def main():
    print("Ange siffra för att välja ett alternativ")
    print("1. Hej \n2. Mönster \n3. Avancerat mönster \n4. Login")

    rätt_användarnamn = "admin"
    rätt_lösenord = "admin"

    # Meny val
    val = int(input("Ange en siffra: "))

    # kalkylera misslyckade försök med hjälp av följande variabler
    försök = 0
    max_försök = 3

    while försök < max_försök:
        if val == 1:
            namn = input("Ange ditt namn: ")
            print(f"Hej {namn}! Trevligt att ses")
            break

        elif val == 2:
            for i in range(6, 0, -1):
                print(f"{i}" + "\t*" * (6-i+1))
            break

        elif val == 3:
            for i in range(6,0,-1):
                print(f"\t"*(i-1) + "\t* " * (6-i+1), i)
            break

        elif val == 4:
            användarnamn = ""
            lösenord = ""
            while försök < max_försök:
                if användarnamn == rätt_användarnamn and lösenord == rätt_lösenord:
                    print(f"{användarnamn} ditt hemliga meddelande är 'kaktus'")
                    exit()
                else:
                    if användarnamn == "":

                        användarnamn = input("Ange ditt namn: ")

                        if användarnamn != rätt_användarnamn:
                            print("Felaktigt användarnamn!")

                    if användarnamn == rätt_användarnamn:
                        lösenord = input("Ange ditt lösenord: ")

                        if lösenord != rätt_lösenord:
                            försök = försök + 1
                            försök_kvar = max_försök - försök
                            if(försök < max_försök):
                                print(f"Felaktigt lösenord! Du har {försök_kvar} försök kvar")
                            else:
                                print(f"Felaktigt lösenord! Du har {försök_kvar} kvar ")

                        else:
                            print(f"Välkommen {användarnamn}")
                    else:
                        print("Programmet kommer att avslutas!")
                        return True

            print("Programmet kommer att avlutas!")
            break

        else:
            print("Du har valt ett alternativ som inte finns, avslutar progammet!")
            break

if __name__ == '__main__':
    main()