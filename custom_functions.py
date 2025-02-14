"""
  CUSTOM FUNCTIONS IN PYTHON ARE OF TWO MAIN TYPES
  - Simple functions : a function with no parameters
  - Functions with parameters : information that a function is supposed to use
  - return is a keyword in python for returning the final output of a function
  """
def greet():
    # function body
    # print("Hello World!")
    return "Hello World!"
# CALLING A FUNCTION OR INVOKING A FUNCTION
print(greet())

# function with parameters
name = "Joseph Mbugua"
school = "emobilis academy"
def welcomeFunction(x):
    # print("Welcome " + x)
    return "Welcome " + x
print(welcomeFunction(school))











