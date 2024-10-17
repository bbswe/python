def nätverk():
    # Konverta adress med prefix till bitar
        # Kanske konvera till subnät mask istället?
    bytes = 32
    binary = bin(bytes)[2:]
    print(binary)

    # Vi kan använda oss av << och >> för att flytta binära bitar
    # << Zero fill left shift = x << 2
    # >> Signed right shift	= x >> 2

    # Konverta bitar till nät-bitar
    # Använd resterande bitar som host-bitar

    # Har man för få adresser kalkylera resterande subnät
    optimal_prefix: any
    adresser: int


    return optimal_prefix, adresser

def main():
    bitar = 32
    binärt = 32/4
    oktet = 32*8-1
    print(binärt)
    print(oktet)

    """
    print("Vi utgår från nätverk 192.168.10.0/24")
    antal_adresser = int(input("Hur många adresser behöver du? "))
    användarbara_adresser = antal_adresser - nätverk()

    print(f"För {antal_adresser} är prefixet: {nätverk()}")
    print(f"Detta ger {användarbara_adresser} användarbara adresser")
    print(f"Reserverade adresser: {nätverk()}")
    """


if __name__ == "__main__":
    main()