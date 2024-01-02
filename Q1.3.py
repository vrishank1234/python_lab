#Q3 Write a program to find whether a given no is even & odd.
num1 = input("Enter a number: ")

if num1.isdigit():
    num = int(num1)
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
else:
    print("Please enter a valid integer.")
