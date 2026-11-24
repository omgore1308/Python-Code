# 1. Single Inheritance: Create a Person class with name and age variables. Create a Student 
#    class that inherits from Person and adds roll_no. Display all student details.


# class Person():

#     Name = "Rahul"
#     age = 23

#     print("Student Name: ",Name)
#     print("Age :",age)

# class Student(Person):

#     Roll_No = 13
#     print("Roll_No :",Roll_No)


# stu = Student()


    
# 2. Create a Vehicle class with a method start() that prints "Vehicle Started". Create a Car 
# class that inherits from Vehicle and adds a method drive().


# class Vehicle():

#     def start(self):
#         print("Vehicle Started")


# class Car(Vehicle):

#     def Drive(self):
#         print("Drive a Car")

# C = Car()  
# C.start()
# C.Drive()


# 2. Employee Salary: 
# Create an Employee class with name and salary. Create a Manager class 
# that inherits from Employee and calculates a 20% bonus on salary.

# class Employee():

#     def Details(self,Name,salary):
#         self.name = Name
#         self.salary = salary

#     def display(self):
#         print("Name :",self.name)
#         print("Salary :",self.salary)    

# class Manager(Employee):

#     def cal_bonus(self):
#         print("Bonus on salary :",self.salary * 20 / 100) 


# C = Manager()

# C.Details("Rohit",50000)
# C.display()
# C.cal_bonus()


# 3. Bank Account: Create a BankAccount class with account_holder and balance. Create a 
# SavingsAccount class that inherits from it and adds interest_rate. Calculate the interest amount.


# class BankAccount():

#     def details(self,Acc_holder_Name,Balance):
#         self.name = Acc_holder_Name
#         self.balance = Balance

#     def display(self):
#         print("Account Holder Name :",self.name)
#         print("Balance :",self.balance)


# class SavingAccount(BankAccount):

#     def cal_intrest(self,rate,Time):

#         print("Interest Amount :", self.balance * rate * Time / 100) 


# Bank = SavingAccount()

# Bank.details("Virat",50000)
# Bank.display()
# Bank.cal_intrest(3.5,365)


# 4. Electricity Bill: Create an Electricity class with customer name and units consumed. Create a Bill class that inherits from it. Calculate the bill using these conditions:
# - First 100 units: ₹3 per unit
# - Next 100 units: ₹5 per unit
# - Above 200 units: ₹8 per unit.


# class Electricity():

#     def __init__(self,name,units):

#         self.Name = name
#         self.units = units

#         print("Customer Name :",self.Name)
#         print("units :",self.units)

# class Bill(Electricity):

#     def cal_bill(self):
#         if self.units <= 100:
#             print("First 100 units :",self.units * 3) 

#         elif self.units <= 200:
#             print("Next 100 units :",(self.units - 100) * 5) 

#         else:
#             print("Above 200 units :",(self.units - 200) * 8)


#     def Total_bill(self):
#         print("Total Bill :",(100 * 3) + (100 * 5) + (self.units - 200) * 8)


# B = Bill("Rakesh",150)

# B.cal_bill()
# B.Total_bill()



# 5.Shopping Product: Create a Product class with product name and price. Create a Discount class 
# that inherits from it. Calculate the final price after applying a 15% discount.


# class Product():

#     def __init__(self,P_name,price):
#         self.pname = P_name
#         self.price = price

#         print("Product Name :",self.pname)
#         print("Price :",self.price)

# class Discount(Product):

#     def cal_Price(self):
#         print("Final Price :",self.price * 15 / 100)

# bill = Discount("shoes",3000)

# bill.cal_Price()



# 6. Student Result: Create three classes: Person, Student, and Result. Student inherits from 
# Person, and Result inherits from Student. Display name, roll number, and marks.

# class Person():

#     Name = "Ajinkya"

#     print("Student Name :",Name)

# class Student(Person):

#     Roll_No = 13

#     print("Roll No :",Roll_No)

# class Result(Student):

#     Marks = 89
#     print("Marks :",Marks)


# Stu = Result()


# 7. Company Management: Create Company, Department, and Employee classes using multilevel 
# inheritance. Display company name, department name, and employee details.


# class Company():

#     Name = "Tata Consultency Services"

#     print("Company Name :",Name)

# class Department(Company):

#     Department = "Developement"

#     print("Department Name :",Department)   

# class Employee(Department):

#     Employee_Name = "Ramesh Kiran Patil"  

#     print("Employee Name :",Employee_Name)


# details = Employee()    


# 8. Online Shopping: Create three classes: Product, Order, and Payment. Use multilevel 
# inheritance to store product details, order quantity, and payment amount. Calculate the 
# final payment.

# class Product():

#     def details(self,name):
#         self.name = name
#         print("Product Name :",self.name)


# class Order(Product):

#     def Order_info(self,quantity):
#         self.quantity = quantity
#         print("Quantity :",self.quantity)

# class Payment(Order):

#     def pri(self,price):
#         self.price = price
#         print("Price :",self.price)

#     def Final_payment(self):
#         print("Final Payment :",self.price * self.quantity)

# shopping = Payment()   
# shopping.details("T-shirt")
# shopping.Order_info(3)
# shopping.pri(2500) 
# shopping.Final_payment()                   
    

# 9. Hospital Management: Create Hospital, Doctor, and Patient classes using multilevel 
# inheritance. Display hospital name, doctor name, and patient details.

# class Hospital():

#     Hospital_Name = "Sancheti"
#     print("Hospital Name :",Hospital_Name)

# class Doctor(Hospital):

#     Doctor_Name = "Dr.Dharmadhikari" 
#     print("Doctor Name :",Doctor_Name)

# class Patient(Doctor):

#     P_name = "Rajendra Bhau Kolhe"
#     print("Patient_Name :",P_name)


# Hos = Patient()


# 10. Student Information: Create two classes Academic and Sports. Store academic marks in one 
# class and sports marks in another. Create a Student class that inherits from both and calculates total marks.


# class Academic():
#     def A_marks(self):
#         self.Academic_marks = 79
#         print("Academic Marks :", self.Academic_marks)
    

# class Sports():
#     def s_marks(self):
#         self.sports_marks = 10
#         print("Sports Marks :", self.sports_marks)
    
    

# class student(Academic,Sports):

#     def cal_total_marks(self):
#         print("Total Marks :",self.Academic_marks + self.sports_marks)

# S = student()

# S.A_marks()
# S.s_marks()
# S.cal_total_marks()


# 11. Employee Salary: Create two classes BasicSalary and Allowance. Create an Employee class 
# that inherits from both. Calculate total salary using basic salary and allowances.

          
# class BasicSalary():

#     def basic_sal(self):
#         self.salary = 45000

# class Allowance():

#     def allowance(self):
#         self.Allo_wance = 5000

# class Employee(BasicSalary,Allowance):

#     def Details(self):
#         self.Name = "Ramesh"

#         print("Employee Name :",self.Name)
#         print("Basic Salary :",self.salary)
#         print("Allowance :",self.Allo_wance)
#         print("Total Salary :",self.salary + self.Allo_wance)

# company = Employee()

# company.basic_sal()

# company.allowance()

# company.Details()


# 12. Mobile Features: Create two classes Camera and MusicPlayer. Create a Smartphone class that 
# inherits from both. Display camera resolution and music player details.


# class Camera():

#     def resol(self):
#         self.cam_resolution = "108 MP"

# class MusicPlayer():

#     def music_details(self):
#         self.Music_Name = "Veezha veera"
#         self.singer = "Sai Abyankar"
#         self.actor = "Dhanush,Sai Pallavi"

# class SmartPhone(Camera,MusicPlayer):

#     def Features(self):
#         print("Camera Resolution :",self.cam_resolution)
#         print("Music Name :",self.Music_Name)
#         print("Singer Name :",self.singer)
#         print("Actor Name :",self.actor)

# S = SmartPhone()

# S.resol()
# S.music_details()
# S.Features()


# 13. Person Information: Create two classes Father and Mother. Store their respective properties.
# Create a Child class that inherits from both and displays all family details.
                

# class Father():
#     def info_Father(self):
#         self.Father_name = "Ramesh prasad wagh"
#         self.F_age = 45

# class Mother():
#     def info_Mother(self):
#         self.Mother_Name = "yogita Ramesh wagh"
#         self.M_age = 42

# class Child(Father,Mother):
#     def child_info(self):
#         self.Child_name = "Mohan Ramesh Wagh"
#         self.age = 23

#     def Family_details(self):
#         print("Father Name :",self.Father_name)
#         print("Father's Age :",self.F_age)
#         print("Mother Name :",self.Mother_Name)
#         print("Mother's Age :",self.M_age)
#         print("Child Name :",self.Child_name)
#         print("Child's age :",self.age)

# FD = Child()

# FD.info_Father()
# FD.info_Mother()
# FD.child_info()
# FD.Family_details()


# 14. Vehicle Management: Create a Vehicle parent class with brand and price. Create three child
#  classes Car, Bike, and Bus. Add their specific details and display them.
                    
# class Vehicle():

#     def brand(self):
#         self.B_name = "TATA"
#         self.C_Price = 2000000
#         self.B_Price = 250000
#         self.T_Price = 8000000



# class Car(Vehicle) :

#     def car_details(self):
#         self.Car_name = "Harrier"
#         print("car Name :",self.Car_name)
#         print("Car Price :",self.C_Price)
#         print("------------------------")

# class Bike(Vehicle):

#     def Bike_details(self):
#         self.B_name = "MT-15"
#         print("Bike Name :",self.B_name)
#         print("Bike Price :",self.B_Price)
#         print("------------------------")
        


# class Truck(Vehicle):

#     def Truck_details(self):
#         self.TName = "Hiwaa"
#         print("Truck Name :",self.TName)
#         print("Truck Price :",self.T_Price)
#         print("------------------------")
        


# C = Car()
# C.brand()
# C.car_details()

# B = Bike()
# B.brand()
# B.Bike_details()

# T = Truck()
# T.brand()
# T.Truck_details()
                   

# 15. Employee Management: Create an Employee parent class with name and salary. Create two child 
# classes Developer and Tester. Add programming language for Developer and testing tool for Tester.


# class Employee():

#     def Info(self):
#         self.D_name = "Mahesh"
#         self.T_name = "Suresh"
#         self.D_salary = 45000
#         self.T_salary = 40000

# class Developer(Employee):

#     def lan(self):
#         self.Pro_Lan = "Python"
#         self.Role1 = "Developer"

#         print("Employee Name :",self.D_name)
#         print("Role :",self.Role1)
#         print("Employee salary :",self.D_salary)
#         print("Developer Programming Language :",self.Pro_Lan)
#         print("--------------------------------------")



# class Tester(Employee):

#     def T_tool(self):
        
#         self.Test_Tool = "PowerBI"
#         self.Role2 = "Tester"

#         print("Employee Name :",self.T_name)
#         print("Role :",self.Role2)
#         print("Salary :",self.T_salary)
#         print(" Use Tool :",self.Test_Tool)


# D = Developer()
# D.Info()
# D.lan()


# T = Tester()
# T.Info()
# T.T_tool()



# 16. Bank Services: Create a Bank parent class with bank name and branch. Create three child 
# classes SavingsAccount, CurrentAccount, and FixedDeposit. Add account-specific information to each child class.


# class Bank():

#     def bank_info(self):
#         self.B_name = "SBI"
#         self.Branch = "Pune"


# class SavingsAccount(Bank):

#     def savings_details(self):
#         self.name = "Ramesh"
#         self.balance = 25000
#         self.interest = 4

#         print("Account Holder Name:", self.name)
#         print("Bank Name:", self.B_name)
#         print("Branch:", self.Branch)
#         print("Account Balance:", self.balance)
#         print("Interest Rate:", self.interest, "%")
#         print("--------------------------------")


# class CurrentAccount(Bank):

#     def current_details(self):
#         self.name = "Suresh"
#         self.balance = 50000
#         self.limit = 100000

#         print("Account Holder Name:", self.name)
#         print("Bank Name:", self.B_name)
#         print("Branch:", self.Branch)
#         print("Account Balance:", self.balance)
#         print("Overdraft Limit:", self.limit)
#         print("--------------------------------")


# class FixedDeposit(Bank):

#     def FD_details(self):
#         self.name = "Mahesh"
#         self.amount = 100000
#         self.time = 2
#         self.interest = 7

#         print("Account Holder Name:", self.name)
#         print("Bank Name:", self.B_name)
#         print("Branch:", self.Branch)
#         print("FD Amount:", self.amount)
#         print("Time Period:", self.time, "Years")
#         print("Interest Rate:", self.interest, "%")
#         print("--------------------------------")


# S = SavingsAccount()
# S.bank_info()
# S.savings_details()

# C = CurrentAccount()
# C.bank_info()
# C.current_details()

# F = FixedDeposit()
# F.bank_info()
# F.FD_details()


# 17. School Management: Create a School parent class with school name and address. Create three
#  child classes Student, Teacher, and Principal. Store their specific details and display them.

# class School():

#     def school_info(self):
#         self.S_name = "Dnyaneshwar School"
#         self.Address = "Pune"


# class Student(School):

#     def student_details(self):
#         self.name = "Rahul"
#         self.age = 18
#         self.std = "12th"

#         print("Student Name:", self.name)
#         print("School Name:", self.S_name)
#         print("School Address:", self.Address)
#         print("Student Age:", self.age)
#         print("Class:", self.std)
#         print("--------------------------------")


# class Teacher(School):

#     def teacher_details(self):
#         self.name = "Mahesh"
#         self.subject = "Python"
#         self.salary = 35000

#         print("Teacher Name:", self.name)
#         print("School Name:", self.S_name)
#         print("School Address:", self.Address)
#         print("Subject:", self.subject)
#         print("Teacher Salary:", self.salary)
#         print("--------------------------------")


# class Principal(School):

#     def principal_details(self):
#         self.name = "Suresh"
#         self.experience = 15
#         self.salary = 60000

#         print("Principal Name:", self.name)
#         print("School Name:", self.S_name)
#         print("School Address:", self.Address)
#         print("Experience:", self.experience, "Years")
#         print("Principal Salary:", self.salary)
#         print("--------------------------------")


# S = Student()
# S.school_info()
# S.student_details()

# T = Teacher()
# T.school_info()
# T.teacher_details()

# P = Principal()
# P.school_info()
# P.principal_details()


# 18.University Management: Create a Person class. Create two child classes Student and Teacher.
#  Then create a TeachingAssistant class that inherits from both Student and Teacher. Display all details.



# class Person():

#     def info(self):
#         self.S_name = "Ram"
#         self.T_name = "Patil sir"




# class student(Person):

#     def stu_detail(self):
#         self.S_age = 23
        


# class teacher(Person):

#     def Tea_detail(self):
#         self.T_age = 45

        

# class TeachingAssistant(student,teacher):


#     def student_info(self):
#         print("Student Name :",self.S_name) 
#         print("age is :",self.S_age)
#         print("---------------------------------")


#     def Teacher_info(self):
#         print("Teacher name :",self.T_name)
#         print("Teacher age :",self.T_age)


# A = TeachingAssistant()


# A.info()
# A.stu_detail()
# A.Tea_detail()



# A.student_info()
# A.Teacher_info()



# 19. Company Employee System: Create an Employee class. Create two child classes Developer and Manager. Create a 
# TeamLead class that inherits from both Developer and Manager. Display all details.



# class Employee():

#     def info(self):
#         self.D_name = "Rahul"
#         self.M_name = "Suresh"


# class Developer(Employee):

#     def dev_detail(self):
#         self.D_age = 23
#         self.language = "Python"


# class Manager(Employee):

#     def man_detail(self):
#         self.M_age = 40
#         self.department = "IT"


# class TeamLead(Developer, Manager):

#     def display(self):

#         self.info()
#         self.dev_detail()
#         self.man_detail()

#         print("Developer Name:", self.D_name)
#         print("Developer Age:", self.D_age)
#         print("Programming Language:", self.language)
#         print("--------------------------------")

#         print("Manager Name:", self.M_name)
#         print("Manager Age:", self.M_age)
#         print("Department:", self.department)


# T = TeamLead()
# T.display()



# 20. School and Sports Management: Create a Person class. Create two child classes Student and SportsPerson. 
# Create a SchoolStudent class that inherits from both Student and SportsPerson. Display personal, academic, and sports details.



# class Person():

#     def info(self):
#         self.name = "Rahul"
#         self.age = 18


# class Student(Person):

#     def stu_detail(self):
#         self.roll_no = 101
#         self.marks = 85


# class SportsPerson(Person):

#     def sports_detail(self):
#         self.game = "Cricket"
#         self.score = 90


# class SchoolStudent(Student, SportsPerson):

#     def display(self):

#         self.info()
#         self.stu_detail()
#         self.sports_detail()

#         print("Personal Details")
#         print("Student Name:", self.name)
#         print("Student Age:", self.age)
#         print("-----------------------------")

#         print("Academic Details")
#         print("Roll Number:", self.roll_no)
#         print("Student Marks:", self.marks)
#         print("-----------------------------")

#         print("Sports Details")
#         print("Game Name:", self.game)
#         print("Sports Score:", self.score)


# S = SchoolStudent()
# S.display()