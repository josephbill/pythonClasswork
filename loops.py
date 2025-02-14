"""
for loop : loops over sequences
syntax
for item in variablerefforsequence:
    code executed repeatedly

"""
# looping a list
fruits = ["Mango", "Banana", "Apple"]
for fruit in fruits:
    print(f"My favourite fruit is {fruit}")

# looping using range
# the loop will execute the code logic according to the stipulated range size
# i.e. range(5) = equal to five loops
#  print the number 0 to 4
for item in range(5):
    print(item)
for item in range(1,5):
    print(item)
for item in range(1,10,2):
    print(item)
"""
range(x) :start from and excludes x 
range(start,stop) : start from start and excludes stop 
range(start,stop,step) : start from start and exclude step,
but skip using step 
"""

# WHile loop : as long as the condition remains True
"""
 While condition:
      code to repeated 
      stop

Rules of using a while loop 
1. Initializer variable
2. Condition to check the variable 
3. A process to break the loop :: increment the value of 
initializer +=
"""
# sample program to print 0 to 4 using while
x = 0
while x < 5:
    print(x)
    x += 1

"""
LOOP CONTROL STATEMENTS 
1. BREAK : EXITS A LOOP EARLY
2. CONTINUE : SKIP THE CURRENT ITERATION (LOOP) AND 
MOVES TO NEXT 
3. PASS : IS SIMPLY A PLACEHOLDER 
"""
for i in fruits:
    pass
# break
for i in fruits:
    if i == "Apple":
        break
    print(i)
# continue
for i in fruits:
    if i == "Banana":
        continue
    print(i)













































