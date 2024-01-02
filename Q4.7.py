# Grandfather class
class Grandfather:
    def __init__(self, grandfather_property):
        self.grandfather_property = grandfather_property

    def display_grandfather_property(self):
        print(f"Grandfather Property: {self.grandfather_property}")

# Father class inheriting from Grandfather
class Father(Grandfather):
    def __init__(self, grandfather_property, father_property):
        # Call the constructor of the Grandfather class
        super().__init__(grandfather_property)
        self.father_property = father_property

    def display_father_property(self):
        print(f"Father Property: {self.father_property}")

# Child class inheriting from Father
class Child(Father):
    def __init__(self, grandfather_property, father_property, child_property):
        # Call the constructor of the Father class
        super().__init__(grandfather_property, father_property)
        self.child_property = child_property

    def display_child_property(self):
        print(f"Child Property: {self.child_property}")

# Example usage:

# Create a Child object
child_obj = Child("Grandfather's Property", "Father's Property", "Child's Property")

# Display the inherited properties
child_obj.display_grandfather_property()
child_obj.display_father_property()
child_obj.display_child_property()
