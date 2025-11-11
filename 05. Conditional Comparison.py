num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


# Simple if
if (num1 > num2):
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num2} is greater than {num1}.")


# if-else
if (num1 > num2):
    print(f"{num1} is greater than {num2}.")
elif (num2 > num1):
    print(f"{num2} is greater than {num1}.")
else:
    print(f"{num1} is equal to {num2}.")

# if-elif-else
if (num1 > num2):
    print(f"{num1} is greater than {num2}.")
elif (num2 > num1):
    print(f"{num2} is greater than {num1}.")
else: 
    print(f"The numbers are the same.")