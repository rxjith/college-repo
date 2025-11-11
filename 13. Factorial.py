n = int(input("Enter the number whose factorial is to be found: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"Factorial of {n}: {factorial}.")