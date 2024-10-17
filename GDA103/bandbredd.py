def start():
    data_bandbredd = 2  # Mbps
    kamera_bandbredd = 4  # Mbps
    telefon_bandbredd = 0.5  # Mbps

    dator = 5  # stycken
    kamera = 7  # stycken
    voip_telefon = 15  # stycken

    n = int(input("Ange antal installationer: ")) # Input

    if n <= 0:
        print("Måste göra minst en installation!")

    else:
        print(f"\nNätverksutrustning, {n} kit")
        total_dator_bandbredd = data_bandbredd * (dator * n)
        total_kamera_bandbredd = kamera_bandbredd * (kamera * n)
        total_telefon_bandbredd = voip_telefon * (telefon_bandbredd * n)

        bandbredd = (total_dator_bandbredd + total_kamera_bandbredd + total_telefon_bandbredd)

        print(dator*n, f'st PC - {total_dator_bandbredd} Mbps')
        print(kamera*n, f'st IP Kamera - {total_kamera_bandbredd} Mbps')
        print(voip_telefon*n, f'st VoIP Telefon - {total_telefon_bandbredd} Mbps')

        print("\nTotal bandbreddsförbrukning i Mbps: ", bandbredd)

        if 1000 <= bandbredd < 10000:
            print("Rekommenderad uplänk hastighet: 10000 Mbps")
        elif 100 <= bandbredd < 1000:
            print("Rekommenderad uplänk hastighet: 1000 Mbps")
        elif 50 <= bandbredd < 100:
            print("Rekommenderad uplänk hastighet: 100 Mbps")
        elif bandbredd < 50:
            print("Rekommenderad uplänk hastighet: 50 Mbps")
        else:
            print("Max installationer som kan göras är 219 av värde 9964.5")

if __name__ == '__main__':
    start()