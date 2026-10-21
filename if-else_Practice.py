"""
Q.1  Write a program to check a username first and then check the password only if the username is correct

Username = "rohan@13gmail.com"
password = "Pass@123"

if Username == "rohan@13gmail.com":
    print("correct username")

    if password == "Pass123" :
        print("Login SuccessFully")

    else:
        print("Invalid Password")

else:
    print("Invalid Username")        
    
"""


"""Q.2  Write a program to check whether a person is at least 18 years old and then check whether they are
registered to vote.


age = 23
Register = "Ketan Wagh"

if age >= 18:
    print("You are Eligible For voting")

    if( Register == "Ketan Wagh"):
        print("Registration Successfully")

    else:
        print("invalid credentials")

else:
    print("You are not eligible for voting")            

"""


"""

Q.3  Write a program to check whether a student has passed; if passed, check whether the student has scored at
least 75 marks for distinction

Result = input("Enter the Result: ")
marks = int(input("Enter your marks: "))

if Result == "Pass":
    print("You are pass in exam")

    if marks >= 75:
        print("Pass in Distinction")

    else:
        print("Pass in Higher Second Class")

else:
    print == "Fail" 
                  """



"""
Q.4 Write a program to check whether a number is positive; if positive, check whether it is even or odd


Number = int(input("Enter the Number: "))

if Number > 0:
    print("Number is Positive")

    if Number % 2 == 0:
        print("Number is Even")

    else:
        print("number is Odd")  

else:
    print("Number is Negative")          

"""

"""
Q.5  Write a program to check whether an applicant meets the minimum age requirement; if so, check whether
their salary is sufficient for a loan


age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age >= 18:
    print("you are Applicable for Loan")

    if salary >= 15000:
        print("salary is sufficient for loan")

    else:
        print("your salary not match with criteria")  

else:
    print("You are not applicable for Loan")          

"""    


"""
Q.6  Write a login program that checks the username, then password, and finally whether the account is active

U = input("Enter the username: ")
P = input("Enter the password:")


if U == "sumitnajan@gmail.com":
    print("Username is correct")

    if P == "Pass@123":
        print("Account is active")

    else:
        print("invalid password")   

else:
    print("invalid username")    

    """


"""
LOGICAL OPERATORS WITH IF ELSE

Q.1 Write a program to check whether a number is between 10 and 50 inclusive

number = int(input("Enter the number: "))

if number >= 10 and number <=50:
    print("Number is between 10 to 50")

else:
    print("Number is not between 10 to 50")
        """

"""

Q.2  Write a program to check whether a number is between 10 and 50 inclusive

number = int(input("Enter the number: "))

if number % 3 == 0 or number % 7 == 0:
    print("Numbers are divisible")

else:
    print("numbers are not divisible by 3 or 7")    
    
"""

"""
Q.3. Write a program to check job eligibility: age must be from 21 to 35 inclusive and the candidate must have the
required qualification.

age = int(input("Enter your age :  "))
qualification = input("Enter your qualification: ")


if age > 21 and age < 35:
    print("your age is eligible ") 

    if qualification == "B.E" or qualification == "B.Tech" or qualification == "BCA" or qualification == "MCA":
        print("your qualification is eligible")

    else:
        print("your qualification is not eligible")    

else:
    print("your age is not eligible")        
"""

"""
Q.4 Write a program to check whether a character is a vowel using the or operator

C = input("Enter the character: ")

if C == "a" or C == "e" or C == "i" or C == "o" or C == "u":
    print("character is a vowel")

else:
    print("Character is not vowel")    

"""


"""
Q.5.  Write a program to check whether a number is not between 100 and 200

number = int(input("Enter the number: "))

if number > 100 and number < 200:
    print("number is between 100 and 200")

else:
    print("number is not between in 100 and 200")    
    """

"""
Q.6 Write a program to display Pass only if a student passes both theory and practical exams

result_theory = input("Enter your theory result: ")

result_practical = input("Enter your practical result: ")

if result_theory == "pass" and result_practical == "pass":
    print("Pass")

else:
    print("Fail")    
    
"""

"""
Q.7. Write a program to provide free delivery if the order amount is at least n500 or the customer has premium
membership

amt = int(input("Enter the amount : "))
membership = input("Enter membership level : ")

if amt >= 500 or membership == "premium":
    print("Free delivery possible")

else:
    print("Free delivery is not possible")    
    """

"""
 Advanced Conditional Practice

Q.1 Write a program to find the greatest of four numbers

No1 = int(input("Enter the No1: "))
No2 = int(input("Enter the No2: "))
No3 = int(input("Enter the No3: "))
No4 = int(input("Enter the No4: "))

if No1 >= No2 and No1 >= No3 and No1 >= No4:
    print("No1 is greatest")

elif No2 >= No1 and No2 >= No3 and No2 >= No4:
    print("No2 is greatest")

elif No3 >= No1 and No3 >= No2 and No3 >= No4:
    print("No3 is greatest")    

else:
    print("No4 is greatest")
"""

"""Q.2 . Write a program to calculate an electricity bill using these slabs: first 100 units at n2/unit, next 100 units at
n3/unit, and units above 200 at n5/unit. Apply each rate only to the units in that slab

units = int(input("Enter your units: "))

if units >= 0 and units <= 100:
    bill = units * 2

elif units >= 100 and units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)

else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)


print("Eletricity bill -",bill)    


"""

"""Q.3 Write a program to calculate an employee bonus based on years of service: 10 or more years = 15%, 5–9
years = 10%, fewer than 5 years = 5%

exp = int(input("Enter your Experience: "))
salary = int(input("Enter your salary: "))


if exp >= 10:
    Bonus = salary * 15 / 100

elif  exp >= 5:
    Bonus = salary * 10 / 100 

else :
    Bonus = salary * 5 / 100  

print("Your Bonus is =",Bonus)          

"""

"""Q.4 Write a program to check whether three angles form a valid triangle (sum must be 180 and each angle must
be positive); if valid, classify it as acute, right, or obtuse

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:

    print("Valid Triangle")

    if a == 90 or b == 90 or c == 90:
        print("Right-angled Triangle")

    elif a > 90 or b > 90 or c > 90:
        print("Obtuse-angled Triangle")

    else:
        print("Acute-angled Triangle")

else:
    print("Invalid Triangle")


"""


"""
Q.5 Write a program to calculate a purchase discount first, then add 18% tax to the discounted amount. Choose
and clearly state your own discount rules.


amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 20 / 100

elif amount >= 2000:
    discount = amount * 10 / 100

else:
    discount = 0

discounted_amount = amount - discount
tax = discounted_amount * 18 / 100
total_amount = discounted_amount + tax

print("Purchase Amount =", amount)
print("Discount =", discount)
print("Amount After Discount =", discounted_amount)
print("Tax (18%) =", tax)
print("Final Amount =", total_amount)
"""



"""
Q.6 . Write a program to validate a time using hours, minutes, and seconds (hours 0–23, minutes 0–59, seconds
0–59).

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
    print("Valid Time")
else:
    print("Invalid Time")"""



"""Q.7  Write an ATM withdrawal program that checks the PIN, then checks whether the balance is sufficient, and
finally ensures the withdrawal amount is positive and a multiple of n100

pin = 1234
balance = 5000

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Withdrawal amount must be positive")

    elif amount % 100 != 0:
        print("Amount must be a multiple of 100")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)

else:
    print("Invalid PIN")"""