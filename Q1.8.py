# Input: Get the number of rows from the user
#i)
num_rows = int(input("Enter the number of rows: "))

# Print the pattern
for i in range(1, num_rows + 1):
    print('* ' * i)

#ii)
# Input: Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Print the pattern
for i in range(1, num_rows + 1):
    print((str(i) + ' ') * i)

#iii)
# Input: Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Print the pattern
for i in range(1, num_rows * 2, 2):
    print('* ' * i)
