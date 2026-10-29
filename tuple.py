"""

A = ("ram",)
print(type(A))"""   # Comma seprated

 # A = (12,34,56,78,True,"ram",34)
"""for j in range(len(A)):
    print(A[j])
"""

"""for i in A:
    print(i)    """
"""
i = 0

while i < len(A):
    print(A[i])
    i += 1
    """

#c1 = ("Ram",12,45,[87,90],True,80,"Shyam")

"""f,*m,l = c1

print(f)
print(m)
print(l)

"""

# covert Tuple into list and vise versa
# Here we using constructor

"""L1 = list(c1)
print(L1)

T1 = tuple(L1)
print(T1)"""


"""
# we can add number inside a list which is already place in tuple. 

c1 = ("Ram",12,45,[87,90],True,80,"Shyam")

c1[3].append(94)

print(c1)
"""

"""
# Create a tuple containing five integers and print it.

A = (20,30,50,60,80)
print(A)
"""

"""
# Create a tuple containing a string, integer, float, and Boolean value.

B = ("Ram",12,34,5,23.78,True,)
print(B)

"""

"""
# Create a single-element tuple and verify its datatype.

C = ("Ram",)

print(type(C))"""

"""
#  Print the first, middle, and last elements of a tuple.

B = ("Ram",12,34,23.78,True,"shyam")

first , *middle , last = B

print(first)
print(middle)
print(last)

"""

"""
#  Reverse a tuple using slicing.

B = ("Ram",12,34,5,23.78,True,"shyam")

print(B[::-1])
"""

"""
# Print every second element using slicing.

B = ("Ram",12,34,5,23.78,True,"shyam")

print(B[0:7:2])
"""


"""
# Count how many times 25 occurs in a tuple.

B = ("Ram",12,34,25,23.78,25,True,"shyam",25)

print(B.count(25))
"""

"""
# Find the index of a given element.

B = ("Ram",12,34,5,23.78,True,"shyam")

print(B.index(True))"""

#A = (20,30,50,60,80)
 # print(sum(A))

"""
# Calculate the sum and average of numeric tuple elements.

Total = sum(A) / len(A)
print(Total)"""
"""
#  Count even and odd numbers in a tuple.

A = (20,30,50,60,80,1,5,7)

even = 0
odd = 0

for i in A:
    if i % 2 == 0:
        even += 1

    else:
        odd += 1

print("Total even No",even)
print("Total odd No",odd)
"""

#A = (20,30,50,60,80,1,5,7)

"""
# Find the maximum and minimum values.

print(max(A))
print(min(A))
"""
"""
# Check whether a particular value exists in a tuple.
 print(30 in A)
"""

"""
# Convert a tuple into a list.
L = list(A)

print(L)

"""
"""
# Unpack a tuple into four variables.

A = ("Dog","Honest","Husky","Kashmir")

animal , emotions , breed , city = A

print(animal)
print(emotions)
print(breed)
print(city)

"""
"""
# Extended unpacking

A = ("Dog","Honest","Husky","Kashmir")

f , *m , l = A
print(f)
print(m)
print(l)
"""

"""
# Swap two variables using tuple unpacking.

A = ("Dog","Honest","Husky","Kashmir")

B = A

animal , emotions , breed , city = B

print(animal)
print(emotions)
print(breed)
print(city)

"""

"""
# Access a specific value from a nested tuple.
A = (("Ram","Sita"),("Bharat","Laxman"),("Ayodya","Himmalaya"))

print(A[0])
print(A[1][1])
print(A[0:3:2])
"""

"""
#  Remove duplicate values while preserving order.

A = (20,30,40,50,20,40,90,100,30,50)

L = []

for i in A:
    if i not in L:
        L.append(i)

    T = tuple(L)   

print(T)     
"""

"""
# Find the second-largest distinct number.

A = (20,80,30,70,60,40,50)

print(sorted(A)[5])
"""


"""
# Sort a tuple in ascending order and convert the result back into a tuple.

A = (20,80,30,70,60,40,50)

S = sorted(A)

T = tuple(S)

print(T)
"""


"""

# Create a tuple of student names and marks, then print each student's details.

Students = (("ram",80),("shaym",70),("don",45),("om",90))

for i in Students:
    print("Name : ",i[0])
    print("Marks : ",i[1])
    print("------------------")
    """