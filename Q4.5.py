class Adder:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_input(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def display_result(self):
        result = self.num1 + self.num2
        print(f"The sum of {self.num1} and {self.num2} is: {result}")

# Example usage:

# Create an Adder object
my_adder = Adder()

# Get user input
my_adder.get_input()

# Display the result
my_adder.display_result()
