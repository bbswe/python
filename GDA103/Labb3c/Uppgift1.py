
def main():
    try:
        # Skapa en lista med namn
        namn = ['Alexander', 'Lisa', 'Fisa', 'Kalle']
        efternamn = ['mpasd', 'jlasdn', 'asdasd', 'asdasda']

        # Skriva ut lista med namn
        print(f"Skriv ut en hel lista: {namn}")

        # Skriv ut lista rad för rad
        print("\nSkriv lista ut rad för rad")
        for förnamn in namn:
            print(förnamn)

        # Be om input och kolla om input finns i lista
        namn_input = input("Skriv ett namn: ")
        for förnamn in namn:
            if namn_input == förnamn:
                print(förnamn, " Finns i listan")
                return  # Vi lägger en return för att stänga for loopen så fort namnet matchar
            else:
                if namn_input == namn[förnamn]:
                    namn.append(namn_input)
                    print(namn)
                    return # Känner av nya namnet i listan och stänger
        print(namn_input, " finns inte med i listan! ")

    except Exception as e:
        print(e)




if __name__ == '__main__':
    main()