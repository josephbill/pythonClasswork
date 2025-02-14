"""
THIS PROGRAM FILE TAKES IN TWO INPUTS I.E NAME OF A USER < AGE , and RETURNS A
STRING THAT OUTPUTS THE BIRTHYEAR
"""

def calculate_birth_year(name,age):
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year - age
    return f"Hello {name} , you were born in this year {birth_year}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
result = calculate_birth_year(user_name,user_age)
print(result)