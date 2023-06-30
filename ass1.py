# Python program to interchange first and last elements in a list
input_list =[1,2,3,4]
x = input_list[0]
y = input_list[-1]
input_list[0]=y
input_list[-1]=x
print(input_list)

# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
 

# How To Find the Length of a List in Python

input_list = [1, 5, 3, 4, 2,'a','b']
count=0
for i in input_list:
    if i in input_list:
        count= count+1
print(count)


# Given two numbers, write a Python code to find the Maximum of these two numbers.

# Examples: 

# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1
    
def max(a,b):
    if a>b:
        return a
    return b
a = int(input('enter the firat number:'))
b = int(input('enter the second number:'))

x = max(a,b)
print(x)
    
    
# Given two numbers, write a Python code to find the Minimum of these two numbers. Examples:

# Input: a = 2, b = 4
# Output: 2

# Input: a = -1, b = -4
# Output: -4

def min(a,b):
    if a<b:
        return a
    return b
a = int(input('enter the firat number:'))
b = int(input('enter the second number:'))

x = min(a,b)
print(x)
    
# Python program to check whether the string is Symmetrical or Palindrome

input_str= input('enter the string:')
k = len(input_str)
m = int(k/2)
l = input_str[:m]
n = input_str[m:]
b = input_str[::-1]
if input_str ==b and l==n:

    print('The entered string is palindrome and symmetrical')
else:
    print('The entered string is not palindrome and not symmetricial')

# We are given a string and we need to reverse words of a given string
input_str= input('enter the str:')
split_str = input_str.split( )
print(split_str)
reverse_str = []

for i in range(len(split_str),0,-1):
    k = split_str[i-1]
    reverse_str.append(k)
print(' '. join(reverse_str))
# Given a string. The task is to print all words with even length in the given string.
input_str = input('enter the string:').split()
join_str =[]
for i in input_str:
    l = len(i)
    if l % 2 == 0:
        join_str.append(i)
print(' '.join(join_str))
