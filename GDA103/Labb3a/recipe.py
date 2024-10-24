def total_ordering():
    amount = int(input("How many cakes do you want? "))
    return amount

def recipe_spongecake():
    name = 'Sponge Cake'
    butter = 75  # gr
    milk = 1  # dl
    eggs = 2  # st
    powdered_sugar = 2  # dl
    vanilla_sugar = 2  # tsk
    flour = 3  # dl
    baking_powder = 1.5  # tsk

    return name, butter, milk, eggs, powdered_sugar, vanilla_sugar, flour, baking_powder

def ingredients_amount(cake_count):
    name, butter, milk, eggs, powdered_sugar, vanilla_sugar, flour, baking_powder = recipe_spongecake()
    cake_name = name
    butter_amount = butter * cake_count
    milk_amount = milk * cake_count
    eggs_amount = eggs * cake_count
    powdered_sugar_amount = powdered_sugar * cake_count
    vanilla_sugar_amount = vanilla_sugar * cake_count
    flour_amount = flour * cake_count
    baking_amount = baking_powder * cake_count

    return cake_name, butter_amount, milk_amount, eggs_amount, powdered_sugar_amount, vanilla_sugar_amount, flour_amount, baking_amount

def menu():
    cake_count = total_ordering()  # kan lika gärna be om input här direkt to be honest...

    if cake_count < 1:
        print("You must order at least one cake")
        return

    cake_name,butter_amount, milk_amount, eggs_amount, powdered_sugar_amount, vanilla_sugar_amount, flour_amount, baking_powder_amount = ingredients_amount(cake_count)
    print(f"Ingredients for your {cake_name}: ")
    print(f"For {cake_count} cake(s), you need: ")
    print(f"Butter: {butter_amount} grams")
    print(f"Milk: {milk_amount} dl")
    print(f"Eggs: {eggs_amount} eggs")
    print(f"Powdered Sugar: {powdered_sugar_amount} dl")
    print(f"Vanilla Sugar: {vanilla_sugar_amount} tsk")
    print(f"Flour: {flour_amount} dl")
    print(f"Baking Powder: {baking_powder_amount} tsk")


if __name__ == "__main__":  # Run menu and bake me a cake
    menu()