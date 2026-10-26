"""
i = 1

while i <= 10:
    print(i)
    i += 1
    """

"""
i = 10

while i >= 1:
    print(i)
    i -= 1
"""


"""
i = 0

while i <= 50:
      print(i)
      i += 2
      """

"""
i = 1

while i <= 50:
    print(i)
    i += 2
    """

"""
i = 5

while i <= 100:
    print(i)
    i += 5
"""

"""
i = 1

sum = 0

while i <= 10:
    sum += i
    i += 1
print(sum)
  """

"""
n = int(input("enter a number: "))
i = 1
while i <= 10:
    mul = n * i
    i += 1
    print(mul)
    """

"""
i = 3

while i <= 100:
    print(i)
    i += 3
    """

"""
i = 1

while i <= 10:
    s = i ** 2
    i += 1
    print(s)

"""

"""
n = int(input("Enter a number: "))

fact = 1

i = 1

while i <= n:
    fact *= i
    i += 1
print(fact)
  """

"""
n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1
print(count)

"""



"""
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print ("sum is",sum)

"""

# Reverse number

"""
n = int(input("Enter a number: "))

rev = 0 

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)

    """


# Fibonacci series

"""
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

"""

"""
# Prime Numbers

n = int(input("Enter the number: "))

if n <= 1:
    print("Not Prime number")

else:    
    i = 2    

    while i < n:
       if n % i == 0:
        print("Not Prime number")
        break
       i += 1
    else:
        print("Prime number")

    """





