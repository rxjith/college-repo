# WAP to check whether a number say num1 is a factor of another number say num2.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if (num1 % num2 == 0):
    print(f"{num1} is a factor of {num2}.")
else:
    print(f"{num1} is not a factor of {num2}.")