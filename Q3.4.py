def is_perfect_number(num):
    # Ensure the input is a positive integer
    if num <= 0 or type(num) != int:
        return False

    # Find the sum of proper divisors
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    # Check if the sum of divisors is equal to the original number
    return divisors_sum == num

# Example usage:
number_to_check = int(input("Enter a number to check if it's perfect: "))

if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
