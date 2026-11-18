# Write a function student() that accepts three arguments: name, age, and city. Print all three details using positional arguments.
"""
def info(Name ,Age ,city):
    print("Name",Name)
    print("Age",Age)
    print("city",city)

info("Om","23","Nsk")    
"""
# Write a function addition() that accepts two numbers and returns their sum. Call the function using positional arguments.
"""
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    print(sum)
        
add(3,5)    

"""

# Write a function employee() that accepts name, salary, and department. Display employee details by passing arguments in the correct positional order.
"""
def employee(Name, salary, department):
    print("Name",Name )
    print("salary",salary )
    print("Dept", department )

employee("om",45000,"software")    
"""

# Write a function calculate() that accepts three numbers and returns their multiplication. Call the function with different positional values.
"""
def calculate(a,b,c):
    return a*b*c
print(calculate(2,2,2))

    """

# Write a function student() that accepts name, age, and marks. Call the function using keyword arguments.
"""
def student(**kwargs):
    print(kwargs)

student(Name = "Om",Age = 23,city = "Nsk")    

"""

# Write a function outer() that contains an inner function inner(). The inner function should print "Welcome to Python".
"""
def state():
    
    def city():
        print("welcome to python")

    city()
state() 
   
"""

# # Write a function calculate() that contains two inner functions:
# - addition() – returns the sum of two numbers.
# - subtraction() – returns the difference between two numbers.    

# def cal():

#   def add(a,b):
#     print(a + b)  
    
#   def sub(a,b):
#     print(a - b)

#   add(8,4)

#   sub(8,4)

# cal() 

# Write a function student() that contains an inner function result().
# - The outer function should accept student name and marks.
# - The inner function should check whether marks are greater than or equal to 40.
# - If yes, print "Pass", otherwise print "Fail".
"""
def student(Name,Marks):
    print("Name",Name)
    print("Marks",Marks)
    def result(Marks):
        if Marks > 40:
            print("Pass")

        else:
            print("Fail")

    result(Marks)  

student("Om",35) 

"""

# Write a function calculate() that accepts three numbers as positional arguments and prints their sum, subtraction, and multiplication.

"""
def cal(a,b,c):
    print("sum :",a + b + c)
    print("sub :",a - b - c)
    print("mul :",a * b * c)

cal(18,4,2)"""

# Write a function student() that accepts student name, roll number, and marks. Call the function using keyword arguments in a different order.
"""
def student(Name, RollNo, marks):
    print("Name",Name)
    print("RollNo",RollNo)
    print("Marks", marks)

student( RollNo = 13, marks = 89,Name = "Ram")"""

# Write a function employee() that accepts name, salary, and department. Calculate and display the employee's annual salary.
"""
def employee(Name ,salary, dept):
    print("Name",Name)
    print("salary",salary)
    print("dept",dept)
    print("Annual_salary",salary * 12)

employee("mohan" , 45000 , "software")
"""

# Write a function product() that accepts product name, price, and quantity. Calculate the total bill and display all product details using keyword arguments.
"""
def product( name, price , quantity):
   print("P_Name",name)
   print("Price",price)
   print("Quantity",quantity)

   total = price * quantity
   print("total bill",total)

product("shirt",800,2)
"""
# Write a function rectangle() that accepts length and width. Calculate and return the area and perimeter. Call the function using positional arguments and keyword arguments separately.
"""
def rec(length, width):
    area_rect = length * width
    P = 2 * (length + width)
    print("peri_rect",P)
    print("area_rect",area_rect)
    

rec(6,6)  
rec(length = 6, width = 6)
"""