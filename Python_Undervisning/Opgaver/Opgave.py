# opgave 2 lektion

# 1 print "a" 10 times
# 2 print "hej"
# 3 print valgfrit
# 4 quit


print("1: a")
print("2: Hej")
print("3: Fuck")
print("4: quit")
print("5: Read file content")
print("6: Write to file")




while True:

    a = input("Indast en af valgmulighederne: ")
    if a == "1": print("a")
    elif a == "2":
        print("Hej")
    elif a == "3": 
        print("Fuck")
    elif a == "4":
        print("Quit")
        break
    elif a == "5":
        file_handle = open("Read_TextFile.txt")
        for line in file_handle:
            print(line)
    elif a == "6":
        file_handle = open("Read_TextFile.txt", "a")
        file_handle.write("hoho besked")

    else: break







