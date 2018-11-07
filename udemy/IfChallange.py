# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("What is your name? ")

age = int(input("Hi {} how old are you? ".format(name)))

if age < 18:
    print("Sorry, {0}, you are too young for this holiday! You must wait {1} years to get a pass".format(name, 18-age))

elif age > 30:
        print("Sorry, {0}, you are to old for this holiday".format(name))
else:
    print("Welcome to the holiday")