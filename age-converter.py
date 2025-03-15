# Author: Christina
# Date: 14.03.2025
# create program that asks the user if they want to convert their age into dog years or vice versa

choice = input('Are you trying to convert your age from dog years or human years? Please specify by entering "dog" or "human". ')

years = int(input("What is your age? "))

if choice.lower() == "dog":
    years = years / 7
elif choice.lower() == "human":
    years = years * 7

print("Your converted age is: " + str(int(years)))
