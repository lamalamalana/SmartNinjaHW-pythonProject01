import sys

print("Hi! This is a unit converter from kilometers to miles.")
decision = input("Would you like to convert some kilometers into miles? (Y/N) ")

if decision == "N":
    print("Have a nice day!")
    sys.exit()

while decision == "Y":
    km = input("Write the number of kilometers: ")
    miles = float(km) * 0.621371
    print(str(km) + " kilometers equates to " + str(miles) + " miles.")
    decision = input("Would you like to convert some more? (Y/N) ")

print("Have a nice day!")
