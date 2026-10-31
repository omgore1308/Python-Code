"""
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")

else:
    print("Odd")
    """


"""
number = int(input("Enter a number: "))

if number < 0:
    print("Negative")

elif number > 0:
    print("Positive")

else:
    print("Zero")        

    """

"""
a = 12345
rev = 0

for i in range(len(str(a))):
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10
print(rev)     
"""

"""
a = 121
orignal = a
rev = 0

for i in range(len(str(a))):
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

if orignal == rev:
    print("Palindrome",rev)

else:
    print("Not Pallindrome")    

    """

"""
num = 3

if num <= 1:
    print("Not Prime")

else :
    for i in range(2,num):
        if num % i == 0:
             print("Not Prime")

    else:
        print("Prime")         
            """




"""
num = int(input("Enter a number: "))

S = num ** 2
print(S)

C = num ** 3
print(C)

  """   



"""
a = 4
fact = 1

for i in range(1,a + 1):
    fact = fact * i
print("Factorial",fact)
    
"""


"""
S = "Animal"
rev = ""

for i in range(len(S)-1,-1,-1):
    rev = rev + S[i]

print(rev)    

    """


"""
numbers = [1,2,3,4,5,6]

for i in numbers:
    if i % 2 == 0:
        print("Even")

    else:
        print("Odd")    

"""


"""
numbers = [1,2,3,4,5,6]
even = 0
odd = 0


for i in numbers:
    if i % 2 == 0:
        even += 1

    else:
        odd += 1    

print("Even",even)
print("Odd",odd)

  """ 

"""
numbers = [1,2,3,4,5,6]

print(numbers[::-1])

"""


"""
L = [1,2,3,4,5,6]

for num in L:
    count = 0

    if num > 1:
        for j in range(2,num):
            if num % j == 0:
                count += 1

        if count == 0:
            print(num)        

"""



"""
A = [20,30,40,"number",34,69,"City"]


for i in A:
    if (type(i)) == str:
        print(i)

    else:
        print()    
    """

"""
A = [20,30,40,"number",34,69,"City"]


for i in A:
    if (type(i)) == int:
        print(i)

    else:
        print()    
     
"""


"""
A = (23,45,78,90)

print("Maximum value", max(A))
print("Minimum value", min(A))
print("sum is ", sum(A))
"""

"""
A = (23,45,78,90)

count = 0

for i in A:
    i > 0
    count += 1

print(count)    
"""

"""
A = (2,3,4,5,6)

for i in A:
    if i % 2 == 0:
        print("Even")

    else:
        print("odd")    """

"""
A = {"Stu_id" : 121, "Name" : "Om", "Age" : 23, "city" : "Nsk"}

print(A.keys())
"""



"""
students = {"python" : 50, "java" : 40, "c++" : 30}

total = 0

for i in students.values():
    total = total + i

print(total) 
   """

"""
students = {"python" : 50, "java" : 80, "c++" : 90}

for i in students.values():
    if i > 60:
        print(i)

"""
"""
students = {"python" : 50, "java" : 80, "c++" : 90}

count = 0

for i in students.values():
    i > 35
    count += 1
print(count)
    
"""

"""
students = {"python" : 50, "java" : 80, "c++" : 90}

print(max(students.values()))
"""