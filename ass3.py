# Let’s learn about list comprehension! You are given three integers x, y, and z representi
# ng the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates 
# given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 

# Please use list comprehensions rather than multiple loops, as a learning exercise.
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))


# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up n score. You are given scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Constraints
# 2 <= n <= 10 -100 <= A[i] <= 100


# l = [1,2,3,4,5,6,6]
# set1 = set(l)
# list1 = list(set1)
# k = max(list1)
# second = list1.remove(k)
# print(list1)
# max = list1[0]

# for i in list1:
#     if i> max:
#         max = i
# print(max)

# Task
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records  = [[ “chi”, 20.0]], [“beta”, 50.0], [“alpha”, 50.0]

# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: [“beta”, “alpha”]. Ordered alphabetically, the names are printed as:

# alpha

# beta
# dict1 ={}

# for i in range(int(input('emter the row no:'))):
#         name = input('enter the name')
#         score = float(input('enter the score'))
#         dict1.update({name:score})
# sort_name =[]
# k = min(dict1.items())
# sort_name.append(k[0])
# l = dict1.pop(k[0])


# list2 = []
# for i in dict1.keys():
#     list2.append(i)
# min = list2[0]

# for i in list2:
#     if i > min:
#         min = i

        
# sort_name.append(min)  
# sorted_by= sorted(sort_name)
# for i in sorted_by:
#     print(i)  



dict1 ={'rani':22,'raja':34,'karol':67,'raju':23}
# for i in range(int(input())):
#     name = input()
#     score = float(input())
# dict1.update({name:score})
sort_name =[]
k = min(dict1.items())
sort_name.append(k[0])
l = dict1.pop(k[0])
l = min(dict1.items())
sec = l[0]

sort_name.append(sec)  
sorted_by= sorted(sort_name)
for i in sorted_by:
    print(i)  


