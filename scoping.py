##GLOBAL SCOPE :: variables defined outside functions : they are accessible anywhere in the
#file
myName = "Joseph"

## LOCAL SCOPE : variables defined within a function
def my_function():
    x = 10
    return f"{myName} defined the variable {x} as a local scope"

print(my_function())
print(myName)

## ENCLOSING SCOPE : SCOPING IN NESTED FUNCTION
def outer():
    y = 20
    def inner():
        nonlocal y
        y += 5
        return y
    inner()
    print(y)

print(outer())






















