
class FileReader:
    """Reads a file"""
    fileSplit = " "
    f = " "
    choice = " "

    # Shows menu

    def __init__(self):
        print("Starting..")
        while True:
            try:
                choice = int(input("\nMenu: \n1) See CSV column options\n2) Choose a column to count\n3) Quit\n"))
            except:
                ValueError: \
                    print("Please input a number")
            if choice == 1:
                indexOfcsv()
            elif choice == 2:
                printColumnContent()
            elif choice == 3:
                break

def csvFile():

    while True:
        try:
            file = open(input("please enter csv file name: "))
            return file
            break
        except FileNotFoundError:
            print("File not found. Try again.")


f = csvFile()


    # Sorts file from user, with a split of ",". Returns a new sorted list, fullFile[]
def csvSort(file):
    fullFile = []
    for i in file:
        splitFile = i.split(",")
        fullFile.append(splitFile)

    return fullFile

        # Puts the sorted and split csv file in a new variable called fileSplit,
        # and puts the traversing pointer at index 0 with f.seek()
fileSplit = csvSort(f)
f.seek(0,0)



        # Function used in the menu: Allows for a indexed output of the first row in the csv file to be printed
def indexOfcsv():

    numberedOutput = fileSplit[0]
    count = 0
    for i in numberedOutput:
        print(count,i)
        count+=1



        # Function used in the menu: Prints counts of reference and specifications of the chosen columns content
def printColumnContent():
    content = []

    columnNumber = input("Please enter column number from column options: ")
    for i in f:
        a = i.split(",")

        content.append(a[int(columnNumber)])

    contentCount = set(content)
    for r in contentCount:
        print(r, content.count(r),)


