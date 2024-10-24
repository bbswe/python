import requests

def main():
    # Dokumentation om jag behöver klicka mig in :) ska inte finnas i produktion :(
    docs = "https://networkcalc.com/api/docs/subnet-calculator"

    # Fråga efter nätverksadress + prefix från användaren t.ex. 192.168.34.5/28
    nätverksadress = input("Ange nät (med prefix: x.x.x.x/yy): ")

    # API
    api = "https://networkcalc.com/api/ip/" + nätverksadress + "?binary=true"
    response = requests.request("GET", api)
    print("Request URL: ", response.url) # Kollar att vi får rätt URL till API

    lista = response.json() # Spara i en lista (behövs inte)

    # Hämta följande fält från det svaret, skriv ut och formatera det lite snyggt i tabellen
    cidr_notation = lista['address']['cidr_notation']
    network_address = lista['address']['network_address']
    broadcast_address = lista['address']['broadcast_address']
    assignable_hosts = lista['address']['assignable_hosts']
    binary = lista['address']['binary']['address']

    print(f"Binary: {binary}")
    print(f"CIDR: {cidr_notation}")
    print(f"Network address: {network_address}")
    print(f"Broadcast address: {broadcast_address}")
    print(f"{nätverksadress} har max {assignable_hosts} hostar")

if __name__ == '__main__':
    main()