### HOW TO OUTPUT RESULTS IN PYTHON 
1. print statement : output to terminal/console.
2. to run a python file use the command : python <filename> 
                                          python3 <filename>


## FUNDAMENTALS OF PROGRAMMING 
1. variables : storage reference for data or info. 
2. Data Types
3. Operators 
4. Conditional Statements 

PRIMITIVE DATA TYPES : SINGLE VALUES 
       - String : anything in quotes " ...  " sequence of chr.
       - Number : integer : 42, 50 ,1000000
                  float : 3.14,1.0,0.1
                  complex : when number is large > 10000000000000
      - boolean : evaluates to True or False   

NON PRIMITIVES (SEQUENCES IN PYTHON)
1. List : ordered mutable collection 
variablename = ["Apple","Banana","Orange"]
2. Tuple : ordered , immutable collection
variablename = (10.04,30.50)
3. Range : sequence of numbers
variablename = range(5)
4. Set : collection of unique items
variablename = {1,2,3,4,5,6}
5. dictionary : key and value pairs 
variablename = {
                   key:value
               }

- The None datatype 
variablename = None

### PYTHON OPERATORS 
special symbols that perform operations on our variables 
- Arithmetic Operators
  ( +.-.*./.%)
- Comparison Operators : usually evaluate to True or False 
   a. == Equal to e.g. a == b 
-  b. != not equal to  a != b 
-  c. > greater than  a > b
-  d. < less than  a < b
-  e. >= greater than or equal to  a >= b 
-  f. <= less than or equal to  a <= b 

- Logical Operators : combine conditional statements 
  a. and :: & :: returns true if both conditions are true
- b. or :: ||  :: returns true if one condition is met 
- c. not :: !  :: reverses the result e.g a != b 

Assignment Operators : used to assign values to variables 
a. =  : assign x = 4, y = "Joseph"
b. += : add and assign , x += 2  ( x = x + 2)
c. -= : subtracts and assigns , x -= 2 (x = x - 2)
d. *= : multiply and assigns , x *= 2 (x = x * 2)
e. /= : divides and assigns , x /= 2 (x = x / 2)
f. %= : modulus and assigns , x %= 2 (x  = x % 2) 


Identity Operators 
a. is : returns true if both comparisons refer to the same object 
b. is not : returns true if they refer to different objects


### CONDITIONAL STATEMENTS 
Make decisions in code based off conditions 

1. if, elif, else statement

Scenario:
A club has entry rules:

Below 18 → ❌ No entry.
18 to 24 → ✅ Entry granted, but no free drink.
25 and above → ✅ Entry granted, and they get a free drink.
VIP members (any age) get exclusive access and a free drink.


### TYPE CASTING 
This is the process of converting one data type into another 
Explicit Type Casting (Manually)

TO Convert to 
Integer = int(value to be converted)
float = float(value to be converted)
string = str(value to be converted)
boolean  = bool(value to be converted)
list = list(value to be converted)
tuple = tuple(value to be converted)
set = set(value to be converted)

2. Ternary Operator/ Conditional 
   shorthand way of writing an if, else statement
   age = 18 
   variableresult = (what to be evaluated if true) if (condition) else (result if false)

3. Nested IF 
   an if statement with an if statement inside
   if condition:
      code to execute 
      if condition:
        code to execute 

4. match-case (python 3.10+)
   matches a code logic as per selection.
     variable = ""
     match variable:
        case selection:
           code to execute 

### LOOPS 
Loops are used for repeating an execution of a block of code X number times 

1. for loop : iterates(loop) over sequences \; list , dictionary , tuple , string and range
2. while loop : repeats the block code as long as the condition is True 

### FUNCTIONS 
- block of code logic or a series of code logic that can return a value or be void. 
- functions in python are defined using the def keyword 

def functionName():
     code logic 

- for a function to be executed it has to be invoked / called/ 
python has two groups of functions 
1. In built functions : normally associated with data types 
2. Custom functions 


### VARIABLE SCOPING
Reference to where a variable can be accessed in a program. 
1. lOCAL SCOPE 
    variables declared in a local scope will only be accessible within that
    function. 
2. GLOBAL SCOPE 
   variables defined in this scope can be accessed anywhere within the file. 
3. ENCLOSING SCOPE 
   when a function is defined within another function , the inner function 
   can access variables of the outer function.

















































































