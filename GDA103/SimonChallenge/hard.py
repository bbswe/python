def main():
    gb = float(input("Ange gigabyte startenhet : "))
    mb = 2**10 # 1024, Operativsystemet använder bas av 2
    megabyte = gb * mb
    print(gb, " GigaByte")
    print(megabyte, " MegaByte")

    usb = int(input("Hur stor USB stickor har du? (GB): "))
    print(int(gb // usb + 1))
    """if usb < 1:
        print("Du måste ha minst 1 USB-sticka")
    else:
        print(usb)"""

if __name__ == '__main__':
    main()