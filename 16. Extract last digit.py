# Write a function to extract the last digit of a given number
def last_digit(num):
    print(f"The last digit of the {num} is {str(num)[-1]}")

num = int(input("Enter a number: "))
last_digit(num)