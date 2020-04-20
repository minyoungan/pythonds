'''
1. Reduce the original number to a series of single-digit numbers.
2. Convert the single digit-number to a string using a lookup
3. Concatenate the single-digit strings together to form the final result.
'''


def toStr(n,base):
  convertString = "0123456789ABCDEF"
  # we check for the base case where n is less than the base we are converting to.
  # When we detect the base case, we stop recursing and simply return the string from the convertString sequence.
  if n < base:
    return convertString[n]
  else:
  # We satisfy both the second and third laws- by making the recursive call and by reducing the problem size using division.
    return toStr(n//base,base) + convertString[n%base]
    
print(toStr(1453,10))


# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
from test import testEqual
def reverse(s):
    s = s[::-1]
    return s

testEqual(reverse("hello"),"olleh")
testEqual(reverse("l"),"l")
testEqual(reverse("follow"),"wollof")
testEqual(reverse(""),"")



# Python code to reverse a string 
# using loop 

def reverse(s): 
str = "" 
for i in s: 
	str = i + str
return str

s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 

# Python code to reverse a string 
# using recursion 

def reverse(s): 
	if len(s) == 0: 
		return s 
	else: 
		return reverse(s[1:]) + s[0] 

s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using recursion) is : ",end="") 
print (reverse(s)) 

# Python code to reverse a string 
# using stack 

# Function to create an empty stack. It 
# initializes size of stack as 0 
def createStack(): 
	stack=[] 
	return stack 

# Function to determine the size of the stack 
def size(stack): 
	return len(stack) 

# Stack is empty if the size is 0 
def isEmpty(stack): 
	if size(stack) == 0: 
		return true 

# Function to add an item to stack . It 
# increases size by 1	 
def push(stack,item): 
	stack.append(item) 

# Function to remove an item from stack. 
# It decreases size by 1 
def pop(stack): 
	if isEmpty(stack): return
	return stack.pop() 

# A stack based function to reverse a string 
def reverse(string): 
	n = len(string) 
	
	# Create a empty stack 
	stack = createStack() 

	# Push all characters of string to stack 
	for i in range(0,n,1): 
		push(stack,string[i]) 

	# Making the string empty since all 
	# characters are saved in stack	 
	string="" 

	# Pop all characters of string and put 
	# them back to string 
	for i in range(0,n,1): 
		string+=pop(stack) 
		
	return string 

# Driver code 
s = "Geeksforgeeks"
print ("The original string is : ",end="") 
print (s) 
print ("The reversed string(using stack) is : ",end="") 
print (reverse(s)) 

# Python code to reverse a string 
# using extended slice syntax 

# Function to reverse a string 
def reverse(string): 
	string = string[::-1] 
	return string 

s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using extended slice syntax) is : ",end="") 
print (reverse(s)) 


# Python code to reverse a string 
# using reversed() 

# Function to reverse a string 
def reverse(string): 
	string = "".join(reversed(string)) 
	return string 

s = "Geeksforgeeks"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using reversed) is : ",end="") 
print (reverse(s)) 




