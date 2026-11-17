
# with argument without returntype
"""def sub(a,b):
    print(a - b)
    
sub(15,5)    """


# without argument with return type
"""
def addition():
    a = 5
    b = 3
    sum = a+b
    return sum
print(addition())

"""

# with argument with return type

"""def mul(a,b):
    a = 5
    b = 5
    result = a*b
    return result

print(mul(5,15))
"""

# without argument without return type
"""
def add():
    a = 5
    b = 10
    print(a + b)

add()    

"""


# even odd
# without argument without return type
"""def check():
    n = [1,2,3,4,5,6,7,8,9]

    for i in n:
        if i % 2 == 0:
           print("Even")

        else:
           print("odd") 

check()           """


# with argument without return type
"""
def check(n):
    
    for i in n:
        if i % 2 == 0:
            print("Even")

        else:
            print("Odd")

check([1,2,3,4,5,6,7,8,9])               
 """

# without argument with return type
"""
def check():
    n = [10,20,30,40,50]

    result = []

    for i in n:
        if i % 2 == 0:
            result.append("even")

        else:
            result.append("odd")

    return result        

print(check())        

       """
"""
def check():
    n = 40

    if n % 2 == 0:
        return "even"

    else:
        return "odd"

print(check())    

"""

# with argument with return type
"""
def check(n):
    if n % 2 == 0:
        return "Even"

    else:
        return "odd"

print(check(5))    
"""
   # using for loop
"""
def check(n):

    result = []

    for i in n:
        if i % 2 == 0:
            result.append("even")
        else :
            result.append("odd")

    return result        

print(check([2,30,1,56,89,33]))  

"""

# prime numbers
# without argument without return type
"""
def prime():
    n = 5

    if n <= 1:
       print("not prime")

    else:
       for i in range(2,n):
           if n % i == 0:
              print("not prime")
              break
          
       else:
        print("prime")        

prime()
"""

# with argument without return type
"""
def prime(n):
    if n <= 1:
        print("not prime")

    else:
        for i in range(2,n):
            if n % i == 0:
                print("not prime")
                break

        else:
            print("prime")

prime(24)    
"""

# without argument with return type

"""
def prime():
    n = 11

    if n <= 1:
        return "not prime"

    else:
        for i in range(2,n):
            if n % i == 0:
                return "not prime"
                break
            
        else:
            return "prime number"

print(prime())
        
"""

# with argument with return type
"""
def prime(n):
    if n <= 1:
        return "not prime"

    else:
        for i in range(2,n):
            if n % i == 0:
                return "not prime"

        else:
            return "prime"

print(prime(11))            
"""

# reverse number
# without argument without return type
"""
def num():
    n = 12345678
    rev = 0

    for i in range(len(str(n))):
        digit = n % 10       # it gives last digit
        rev = rev * 10 + digit     # it remove last digit
        n = n // 10   # it converts string in reverse
    print(rev)

num()
"""

# with argument without return type
"""
def num(n):

    rev = 0

    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    print(rev)

num(12345678)        
"""

# without argument with return type
"""
def num():
    n = 12345678
    rev = 0

    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev

print(num())
    """

# with argument with return type
"""
def num(n):
    rev = 0
    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev

print(num(12345678))  
  """

# pallindrome
# without argument without return type
"""
def pal():
    n = 121
    orignal = n
    rev = 0

    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if orignal == rev:
        print("Palindrome",rev)

    else:
        print("not palindrome")

pal()                
"""

# with argument without return type
"""
def pal(n):
    orignal = n
    rev = 0

    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        
    if orignal == rev:
            print("Palindrome",rev)
        
    else:
        print("not palindrome")

pal(171)           """

# without arugument with return type
"""
def pal():
    n = 121
    orignal = n
    rev = 0

    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        
    if orignal == rev:
        return "Palindrome",rev
        
    else:
        return "not palindrome"

print(pal())    
 """

# with argument with return type
"""
def pal(n):
    orignal = n
    rev = 0

    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        
    if orignal == rev:
        return"Palindrome",rev
        
    else:
        return"not palindrome"

print(pal(172))     """