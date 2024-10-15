"""
Skriv ett program där användaren matar in antal GigaByte (GB).
Omvandla detta sedan till Bytes.
Tänk på att en dators version av kilo som enhet är annorlunda än människors.
"""

def main():
    antal_gigabytes = float(input("Ange antal gigabyte: "))
    antal_bytes = antal_gigabytes * (1*10**+9)
    antal_bytes_binary = antal_gigabytes * (2**30)
    if antal_gigabytes < 1:
        return
    else:
        print(f"{antal_gigabytes} GB blir {antal_bytes} Bytes")
        print(f"{antal_bytes_binary} Bytes i Binärt")
    return

if __name__ == '__main__':
    main()