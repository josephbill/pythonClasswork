"""
Creating a class : we use the keyword 'class' i.e.
class classname:
"""
from numpy.testing.print_coercion_tables import print_new_cast_table


class User:
    # here I can now define my class properties
    fullname = "Joseph Mbugua"
    role_id = "Lecturer"
    staff_id = 34983498
    is_verified = True

"""
to create an object e use the name of the class followed by a 
parentheses () i.e. variable = User()
"""
person1 = User() # this creates an object of the user class
print(person1)
print(person1.fullname)#to access a property use the dot notation
"""
1.the __init__() method : this method is always executed on an 
object creation 
2. the __str__() method : this method returns the string representation of an object 
"""
class Person:
    def __init__(self, fullname, role_id, staff_id, is_verified):
        self.fullname = fullname
        self.role_id = role_id
        self.staff_id = staff_id
        self.is_verified = is_verified
    def __str__(self):
        return f"{self.fullname}, {self.role_id}, {self.staff_id}, {self.is_verified}"

    # custom object methods
    def transform_word(self, msg):
        newword = self.fullname.upper()
        roleup = self.role_id.upper()
        print(msg)
        result = f"{newword} , {roleup}"
        return result

# create object
p1 = Person("joseph","lecturer",893849384, True)
p2 = Person("Alice","Student",0, True)
print(p1)
print(p1.fullname)
print(p2.fullname)
# how to print object methods
print(p1.transform_word("TRANSFORM SUCCESS"))
print(p2.transform_word("TRANSFORM SUCCESS"))
# MODIFYING AN OBJECTS PROPERTIES
p1.fullname = "John"
print(p1)
p2.role_id = "admin"
print(p2)
# adding a new property to objects
p1.nationality = "Kenyan"
print(p1.nationality)
# delete an object
del p2
print(p2)
# delete object properties : use the del keyword
del p1.staff_id
print(p1)





























