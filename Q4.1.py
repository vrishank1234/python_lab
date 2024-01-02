class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}\nEmployee Name: {self.emp_name}\nEmployee Salary: {self.emp_salary}"

    def print_employee_details(self):
        print(self.get_employee_details())

# Get user input for employee details
emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
emp_salary = float(input("Enter Employee Salary: "))

# Create an Employee object with user input
employee1 = Employee(emp_id, emp_name, emp_salary)

# Call the print_employee_details method
print("\nEmployee Details:")
employee1.print_employee_details()
