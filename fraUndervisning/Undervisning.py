name = "Daniel"
for nr in range(len(name)):
    print(name[nr])
for letter in name:
    print(letter)

name = "Daniel"
for nr in range(len(name)):
    print(name[nr])


c = 0
running = True
while running != False:
    if c == 50000:
        running = False
    print("hej", c)
    c += 1

name = "joanna"
if name == "bob":
    print("ja 1")
elif name == "joanna":
    print("ja 2")
elif name == "byggemand bob":
    print("ja 3")
else:
    print("næææ...")


z = 10.1
# str int float bool DATA TYPER
# tuple list dict set DATA STRUCTURE
print( type(z) == float )

a = 1
b = 2
a,b = b,a
a,b,c = 1,2,3

name = "Daniel"
name = 1
name = 1.0
print( type(name) )

print ("hej" , "igen", sep="              ", end="\n")
print("goddag")