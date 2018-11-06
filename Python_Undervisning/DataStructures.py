# data structures

# list, tuple, dict, set

# Converting tuple to list and list to tuple

# List


Lnames = list()

Lnames.append("Luis")
Lnames.append("Fred")
Lnames.append(1234)

print(Lnames)




# Tuple
names = ("Daniel", "Bob", "Rasmus", "Jørgen", "Ditte")


def addToTuple(ele):


    tmp = list(names)
    tmp.append(ele)
    return tuple(tmp)

names = addToTuple("luis")

print(names)


# dict

ports = { 80:"HTTP", 443:"HTTPS", 21:"FTP" }

ports.update({40:"My service"})

print(ports[80])


# set

Snames = set()

Snames.add("daniel")
Snames.add("Bob")
Snames.add(123)



print(Snames)
