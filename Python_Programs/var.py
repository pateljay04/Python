print("variables!")

## Crearing Variables

# x = "John"
# y = 5

# print(x)
# print(y)


## Casting 

# A = str(3)     # A = "3"
# B = int(2)     # B = "2"
# C = float(3)   # C = "3.0"
# print(A,B,C)


## Type function

# print(type(x))  # String
# print(type(y))  # int
# print(type(C))  # float

# same varaible But Different Numbers
#J = 10
#J = 25

#print(J) # The output is 25 It update 10 to 25 

# A="Patel Jay Kumar"
# print("My Name is",A)


# Global variables 

# a = "Good"

# def function():
#     a = "Excellent"
#     print("you are " + a)

# function()

# print("you are " + a)

def print_student_info(name, roll_number, class_section):
  """Prints student information in a formatted way."""
  print(f"Name: {name}")
  print(f"Roll Number: {roll_number}")
  print(f"Class: {class_section}")

def main():
  """Prompts the user for student information and prints it."""
  name = input("Enter student name: ")
  roll_number = int(input("Enter roll number: "))
  class_section = input("Enter class section: ")

  print_student_info(name, roll_number, class_section)

if __name__ == "__main__":
  main()







