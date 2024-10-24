def main():

    svar = input("Skriv ett positivt tal: ")
    if int(svar) <= 0:
        print("Måste vara ett positivt!")
    elif int(svar) % 2 == 0:
        print(f"Talet {svar} är positivt")
    else:
        print("Du skrev talet ", svar)

if __name__ == "__main__":
    main()