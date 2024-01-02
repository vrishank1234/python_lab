char = input("Enter a character: ")

char = char.lower()

if char in 'aeiou':
    print(f"The character '{char}' is a vowel.")
else:
    print(f"The character '{char}' is not a vowel.")
