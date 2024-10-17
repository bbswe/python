def main():
    n = float(input("Ange storlek i TB: "))

    kalkylera = n*10**12 # Vi tar vår input och multiplicerar på 10^12 som omvandlar till binärt
    gb = 2**40 # 2**40 eller 2^40
    mb = 2**30 # 2^30
    kb = 2**20 # 2*20
    bytes = 2**10 # 1024 binary, Operativsystemet använder bas av 2, tillverkare gör bas av 10 10^3
    tillverkare = kalkylera/10**12
    operativsystem = kalkylera / gb


    print(f"Tillverkaren säger: {tillverkare} GB")
    print(f"Operativsystemet säger: {operativsystem} GB")

if __name__ == '__main__':
    main()