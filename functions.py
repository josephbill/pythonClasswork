"""
In built group ]===
"""
# String functions
text = "Hello world"
print(len(text)) # the method len it returns the length of the string
print(text.upper()) # the upper method converts the string into caps letters
print(text.lower()) # the lower method converts the string into lowercase letters
text = text.lower().replace("hello", "Joseph")
print(text) # replace replace's text/
print(text.split()) # deconstructs a string and returns a list version of the words in
# the string

## NUMBERS GROUP
pos_num = 10
neg_num = -10
float_num = 10.33
print(abs(neg_num)) # returns the positive version of the number
print(pow(2,3)) # 2^3 =  2 * 2 * 2 = 8
print(divmod(10,3)) # (3,1) quotient and reminder are returned as a tuple
print(round(float_num,1)) # 10.3
print(sum([pos_num, float_num])) # 10.33 and 10

### LISTS
nums = [3,1,2,4,5]
print(len(nums)) # return the number of items in the list
print(list(reversed(nums))) # reverses the list
print(min(nums)) # min number in the list is returned
print(max(nums)) # returns maximum number
nums.append(10)# adds an item to the end of the list
print(nums)
print(nums.pop()) # removes and returns the last item in the list














