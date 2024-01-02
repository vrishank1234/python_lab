class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.students_count = 0

    def admit_student(self):
        self.students_count += 1
        print(f"Student admitted to {self.department_name} Department.")

    def get_students_count(self):
        return self.students_count

# Example usage:

# Create Department objects for PGDM and BTech
pgdm_department = Department("PGDM")
btech_department = Department("BTech")

# Admit students to PGDM Department
pgdm_department.admit_student()
pgdm_department.admit_student()

# Admit students to BTech Department
btech_department.admit_student()

# Get and print the students count for each department
pgdm_count = pgdm_department.get_students_count()
btech_count = btech_department.get_students_count()

print("\nStudents Count:")
print(f"PGDM Department: {pgdm_count} students")
print(f"BTech Department: {btech_count} students")
