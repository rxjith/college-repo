st = input("Enter a string: ").lower()
vowel_count = 0
for i in st:
    if ('a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i):
        vowel_count += 1
print(f"Number of vowels in the given string: {vowel_count}.")