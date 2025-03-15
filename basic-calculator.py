# Ask user for input a (1st number)
# Ask user for input b (2nd number)
# Ask what they would like to do with the two numbers (a * b, or a + b, blablabla (add as many as possible))

# Make an if statement, based on what action they want to do (modify in place)

# Print the outputted number

num1 = int(input("I can help you calculate whatever you want. Give me your first number: "))
num2 = int(input("Give me your second number: "))

command = input("What basic function would you like to execute on these two numbers (multiply, divide, add, subtract or power)? ")

if command.lower() == "multiply":
    result = num1 * num2
elif command.lower() == "divide":
    result = num1 / num2
elif command.lower() == "add":
    result = num1 + num2
elif command.lower() == "subtract":
    result = num1 - num2
elif command.lower() == "power":
    result = num1 ** num2
else:
    print("Sorry I cannot do that, but I am working on a more advanced version of this calculator!")
    exit()

print(result)

# Done!
