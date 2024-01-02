# Base class LU (Life Sciences)
class LU:
    def __init__(self, student_name, lu_course):
        self.student_name = student_name
        self.lu_course = lu_course

    def display_lu_info(self):
        print(f"LU Student: {self.student_name}\nCourse: {self.lu_course}")

# Base class ITM (Information Technology Management)
class ITM:
    def __init__(self, student_name, itm_course):
        self.student_name = student_name
        self.itm_course = itm_course

    def display_itm_info(self):
        print(f"ITM Student: {self.student_name}\nCourse: {self.itm_course}")

# Derived class combining both LU and ITM (Multiple Inheritance)
class LU_ITMStudent(LU, ITM):
    def __init__(self, student_name, lu_course, itm_course):
        # Call the constructors of both base classes
        LU.__init__(self, student_name, lu_course)
        ITM.__init__(self, student_name, itm_course)

    def display_info(self):
        # Call display methods of both base classes
        self.display_lu_info()
        print()  # Adding an empty line for better separation
        self.display_itm_info()

# Example usage:

# Get user input for LU_ITMStudent details
student_name = input("Enter student name: ")
lu_course = input("Enter LU course: ")
itm_course = input("Enter ITM course: ")

# Create a LU_ITMStudent object with user input
student1 = LU_ITMStudent(student_name, lu_course, itm_course)

# Display the information
student1.display_info()
