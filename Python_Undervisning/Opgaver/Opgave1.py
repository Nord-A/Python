# Opgave



print("1: Pick a file")
print("2: Write to a file")
print("3: Read to file")
print("4: quit")





while True:

    a = input("Indast en af valgmulighederne: ")
    if a == "1":
        file_handle = open("Read_TextFile.txt", "a+")
        for line in file_handle:
            print(line)
    elif a == "2":
        file_handle = open("Read_TextFile.txt", "a")
        file_handle.write("hoho besked")
    elif a == "3":
        file_handle = open("Read_TextFile.txt")
        for line in file_handle:
            print(line)
    elif a == "4":
        print("Quit")
        break
    else:
        break


