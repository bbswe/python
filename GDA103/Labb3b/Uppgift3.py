def main():
    # Räknar upp
    for my_var in range(5):
        print("* * * * *", my_var)
    print("klar")

    # Räknar ner
    for my_var in range(15, 10, -1):
        print("* * * * *", my_var)
    print("klar")

    text='python'
    textLength = len(text)
    for x in range(0, textLength):
        print("Position", x, "innehåller tecken", text[x])

if __name__ == "__main__":
    main()