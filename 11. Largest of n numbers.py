n = int(input("Enter a value for n: "))
largest = 0
for i in range(n):
    num = int(input("Enter a number: "))
    if (num > largest):
        largest = num
print(f"Largest number is {largest}.")