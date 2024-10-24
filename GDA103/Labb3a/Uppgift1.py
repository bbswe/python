# print("Summan är: ", 10+20)
##############################
from traceback import print_tb

a = 1
b = 2

if a**b%2==0:
    print("Jämnt tal")
else:
    print("Ojämnt tal")

if a/b%2 != 0:
    print("Svaret är", a/b)

##############################
nr = input('ange nr: ')
print('nr är en', type(nr))