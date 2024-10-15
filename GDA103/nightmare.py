def konvertera_enheter(värde, från_värde, till_värde):
    # Enhetsskalor i Bytes
    enheter = {
        'B': 1,
        'KB': 10**3,
        'MB': 10**6,
        'GB': 10**9,
        'TB': 10**12
    }

    # Konverterar till bitar så att vi kan konverta till nytt värde baserat på enheternas exponent
    till_bytes = värde * enheter[från_värde]

    #
    konverterat_värde = till_bytes / enheter[till_värde]

    # Rundar upp till decimaler
    return round(konverterat_värde, 2)


def main():
    print("Ange vilken enhet du vill konvertera från och till, B, KB, MB, GB, TB")
    från_v = input("Ange värde du vill konverta från: ").upper()
    till_v = input("Ange värde du vill konverta till: ").upper()
    n = int(input("Ange storlek: "))

    print(konvertera_enheter(värde=n, från_värde=från_v, till_värde=till_v), till_v)

if __name__ == "__main__":
    main()
