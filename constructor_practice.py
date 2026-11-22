# Student Management System

# Create a Student class with the following attributes:
# - Student name
# - Roll number
# - Course
# Create a method display_details() to display all student information. Create three student objects.


# class student():

#     def details(self,name,roll_no,course):
#         self.stu_name = name
#         self.Roll_no = roll_no
#         self.course = course

#     def display(self):
#         print("Student_name :",self.stu_name)
#         print("Roll_No :",self.Roll_no)
#         print("course :",self.course)

# s1 = student()
# s2 = student()
# s3 = student()

# s1.details("om",13,"python")
# s1.display()

# s2.details("Ram",15,"java")
# s2.display()

# s3.details("rohit",45,"data science")
# s3.display()


# Employee Salary Details

# Create an Employee class with:
# - Employee name
# - Employee ID
# - Basic salary
# Create a method calculate_salary() that calculates and displays the annual salary.


# class employee():

#     def details(self,name,id,salary):
#         self.emp_name = name
#         self.emp_id = id
#         self.salary = salary

#     def display(self):
#         print("Employee_name",self.emp_name)
#         print("employee id",self.emp_id)
#         print("salary",self.salary)
#         print("Annual salary",self.salary * 12)  


# emp = employee()

# emp.details("Rohan",34,35000)

# emp.display()


# Create a Mobile class with brand, model and price.

# Create the following methods:
# - display_details()
# - apply_discount(discount)
#    Pass the discount amount as an argument and display the final price.


# class mobile():

#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self.price = price

    
#     def discount(self,amt):
#         self.dis = amt 
        


#     def display_data(self):
#             print("brand :",self.brand)  
#             print("model :",self.model)
#             print("price :",self.price)
#             print("discount :",self.dis)
#             print("Final_price :",self.price * self.dis / 100)


# bill = mobile("apple","iphone 18",800000)

# bill.discount(10)
# bill.display_data()




# 4. Bank Account

# Create a BankAccount class with account holder name and balance.

# Create methods:
# - deposit(amount)
# - withdraw(amount)
# - display_balance()
#    Perform deposit and withdrawal operations.


# class BankAccount():

#     def __init__(self,Name,Balance):
#         self.name = Name
#         self.balance = Balance


#     def deposit(self,amt):
#         self.dep = amt
#         self.balance = self.balance + amt


     
#     def withdraw(self,amt):
#         self.withd = amt
#         if self.balance > self.withd:
#             print("Transaction successfully")

#         else:
#             print("Their is no required amount in your account")    

#     def display_balance(self):
#         self.total_bal = self.balance - self.withd

#     def display_details(self):
#         print("Account holder Name :",self.name)
#         print("Account Balance :",self.balance)
#         print("Deposit Amount :",self.dep)
#         print("Updated Balance :",self.balance)
#         print("withdraw Amount :",self.withd)
#         print("Remaining balance :",self.total_bal)  

# acc = BankAccount("Om",100000)

# acc.deposit(30000)

# acc.withdraw(2000)

# acc.display_balance()

# acc.display_details()



# 5. Car Rental System

# Create a Car class with car name, rent per day and number of rental days.

# Create a method calculate_rent() that accepts the number of days and calculates the total rental amount.
# Section 2: Constructors – No Args & Args

# class car():

#     def __init__(self):
#         self.name = "innova"
#         self.rent = 7000
#         self.days = 3

#     def cal_rent(self,days):
#         total_rent = days * self.rent
#         print("Total Rent :",total_rent)
        


#     def dis_total_amt(self):
#         print("Car Name :",self.name)
#         print("Rent Per Day :",self.rent)
#         print("No of Days :",self.days)
      
        

# c = car()

# c.cal_rent(3)

# c.dis_total_amt()



# 6. Laptop Information – No-Argument Constructor

# Create a Laptop class with a no-argument constructor.

# Initialize the following values inside the constructor:
# - Brand = Dell
# - RAM = 16GB
# - Price = 55000
#    Create a method to display laptop details.


# class Laptop():

#     def __init__(self):
#         self.Brand = "Dell"
#         self.Ram = "16GB"
#         self.Price = 55000

#     def laptop_details(self):
#         print("Laptop Brand :",self.Brand)
#         print("Ram :",self.Ram)
#         print("Price :",55000)

# Source = Laptop()

# Source.laptop_details()
            



# 7. Book Information – Parameterized Constructor

# Create a Book class with a parameterized constructor accepting:
# - Book name
# - Author name
# - Book price
#    Create two objects with different information.


# class Book():

#     def __init__(self,B_name,A_name,Price):
#         self.bookname = B_name
#         self.A_Name = A_name
#         self.Price = Price

#     def Details(self):
#         print("Book Name :",self.bookname)
#         print("Author Name :",self.A_Name)
#         print("Price :",self.Price)  


# B1 = Book("Shaymchi Aai","Sane Guruji",500)
# B1.Details()

# B2 = Book("Chaava","Shivaji Sawant",800)
# B2.Details()




# 8. Rectangle Area

# Create a Rectangle class with a parameterized constructor accepting length and width.

# Create a method calculate_area() to calculate and display the area.


# class Rectangle():

#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def cal_area(self):
#         print("Area Of Rectangle :",self.length * self.width)

# R = Rectangle(40,20)

# R.cal_area()



# 9. Electricity Bill

# Create an ElectricityBill class with a parameterized constructor accepting:
# - Customer name
# - Units consumed
# Create a method calculate_bill() using the following conditions:
# - First 100 units: ₹5 per unit
# - Next 100 units: ₹7 per unit
# - Above 200 units: ₹10 per unit

           
# class ElectricityBill():

#     def __init__(self,Name,Units):
#         self.Name = Name
#         self.Units = Units

#     def calculate_Bill(self):
#         if self.Units <= 100:
#             print("first 100 units :",self.Units * 5)

#         elif self.Units <= 200:
#             print("Next 100 units :",(self.Units - 100) * 7)

#         else:
#             print("Above 200 units :",(self.Units - 200) * 10) 

#     def Display_Bill(self):
#         print("Customer Name :",self.Name)
#         print("Units consumed :",self.Units)
#         print("Total_Bill :",(100 * 5) + (100 * 7) + (self.Units - 200) * 10)


# bill = ElectricityBill("Rohit",250)


# bill.Display_Bill()
# bill.calculate_Bill()




# 10. Product Inventory

# Create a Product class with a parameterized constructor accepting product name, price and quantity.

# Create methods:
# - display_product()
# - calculate_total_price()
# - update_quantity(new_quantity)
# Section 3: Variables – Instance, Class & Local



# class Product():

#     shop_name = "D_Mart"
    
#     def __init__(self,Name,Price,quantity):
#         self.name = Name
#         self.price = Price
#         self.quantity = quantity

#     def display_product(self):
#         print("Product Name :",self.name)

#     def calculate_total_price(self):
#         print("Calculate Total Price :",self.price * self.quantity)   


#     def update_quantity(self,new_quantity):
#         self.quantity = new_quantity

# P = Product("Shampoo",500,3)

# P.display_product()

# P.calculate_total_price()

# P.update_quantity(5)

# P.calculate_total_price()


             
# Company Employee Counter

# Create an Employee class with:
# - Class variable: company_name
# - Class variable: employee_count
# - Instance variables: employee_name, employee_id
#     Every time an object is created, increase the employee count by 1.

#     Display employee details and total employees.


# class Employee():

#     company_name = "Google"
#     emp_count = 0

#     def __init__(self,Name,Id):
#         self.Name = Name
#         self.Id = Id
#         Employee.emp_count += 1

#     def details(self):
#         print("Company_name",Employee.company_name)
#         print("Employee Name :",self.Name)
#         print("Employee Id :",self.Id)
#         print("Employee count :",Employee.emp_count)

# emp1 = Employee("Om",101)
# emp1.details()
           
# emp2 = Employee("Ram",102)
# emp2.details()



# 12. School Student Information

# Create a Student class with:
# - Class variable: school_name
# - Instance variables: student_name, roll_number
# - Local variable inside a method: percentage
#     Create a method to display complete student information.

# class student():

#     School_name = "MITCON InterNational School"
    
#     def __init__(self,student_name,roll_number):

#         self.Name = student_name
#         self.rollNo = roll_number
#         percentage = 78
#         print("percentage :",percentage) 

        
#     def display(self):

#         print("Student Name :",self.Name)
#         print("Roll_NO :",self.rollNo)
#         print("School Name :",student.School_name)
        

# s = student("Virat",18)

# s.display()

#13. Shopping Cart

# Create a ShoppingCart class with:
# - Instance variable: customer_name
# - Instance variable: total_amount
# - Class variable: discount_percentage
# Create a method calculate_discount() that uses a local variable to calculate the final payable amount.


# class shoppingcart():

#     Discount_Percentage = 10

#     def __init__(self,customer_name,total_amount):
#         self.name = customer_name
#         self.total = total_amount

#     def calculate_discount(self):

        
#         print("Customer Name :",self.name)
#         print("Discount_percentage :",shoppingcart.Discount_Percentage)
#         print("Total Amount :",self.total)
#         final_payable_amount = self.total * 10 / 100
#         print("Final Payable Amount :",self.total - final_payable_amount)

# S = shoppingcart("Mohan",5000)

# S.calculate_discount()


# 14. Hospital Patient Management

# Create a Patient class with:
# - Class variable: hospital_name
# - Instance variables: patient_name, patient_age, disease
# Create a method display_patient() to display patient details.

#     Create three patient objects and display their information.


# class Patient():

#     hospital_name = "City Hospital"

#     def __init__(self, patient_name, patient_age, disease):
#         self.patient_name = patient_name
#         self.patient_age = patient_age
#         self.disease = disease

#     def display_patient(self):
#         print("Hospital Name:", Patient.hospital_name)
#         print("Patient Name:", self.patient_name)
#         print("Patient Age:", self.patient_age)
#         print("Disease:", self.disease)
        


# p1 = Patient("mohan", 23, "Fever")
# p2 = Patient("Ram", 25, "Cold")
# p3 = Patient("Sham", 30, "Headache")

# p1.display_patient()
# p2.display_patient()
# p3.display_patient()



# 15. Online Course Management

# Create a Course class with:
# - Class variable: institute_name
# - Instance variables: course_name, course_fee
# - Local variable: discount
# Create a method calculate_fee() that calculates the final course fee after discount.
# Section 4: Methods, Arguments & Return Values




# class Course():

#     institute_name = "The Kiran Academy"

#     def __init__(self, course_name, course_fee):
#         self.course_name = course_name
#         self.course_fee = course_fee

#     def calculate_fee(self):
#         discount = 10

#         discount_amt = self.course_fee * discount / 100
#         final_fee = self.course_fee - discount_amt

#         print("Institute Name:", Course.institute_name)
#         print("Course Name:", self.course_name)
#         print("Course Fee:", self.course_fee)
#         print("Discount:", discount, "%")
#         print("Final Course Fee:", final_fee)


# c = Course("Python Full Stack", 30000)

# c.calculate_fee()




# 16. ATM Withdrawal System

# Create an ATM class with account holder name and balance.

# Create methods:
# - check_balance()
# - withdraw(amount)
# - deposit(amount)
#     The withdrawal method should accept an argument and return the updated balance.



# class ATM():

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def check_balance(self):
#         print("Account Holder:", self.name)
#         print("Account Balance:", self.balance)

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance = self.balance - amount
#             print("Withdrawal Successfully")
#         else:
#             print("Insufficient Balance")

#         return self.balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Deposit Successfully")
#         return self.balance


# a = ATM("Om", 10000)

# a.check_balance()

# print("Updated Balance:", a.withdraw(2000))

# print("Updated Balance:", a.deposit(5000))

# a.check_balance()



# 17. Temperature Converter

# Create a Temperature class with temperature in Celsius.

# Create methods:
# - celsius_to_fahrenheit()
# - fahrenheit_to_celsius(fahrenheit)
#     Return the converted temperature.




# class Temperature():

#     def __init__(self, celsius):
#         self.celsius = celsius

#     def celsius_to_fahrenheit(self):
#         F = (self.celsius * 9/5) + 32
#         return F

#     def fahrenheit_to_celsius(self, fahrenheit):
#         C = (fahrenheit - 32) * 5/9
#         return C


# t = Temperature(37)

# print("Celsius to Fahrenheit:", t.celsius_to_fahrenheit())

# print("Fahrenheit to Celsius:", t.fahrenheit_to_celsius(98.6))

       

# 18. Student Result Management

# Create a StudentResult class with student name and marks in three subjects.

# Create methods:
# - calculate_total()
# - calculate_percentage()
# - display_result()
#     Return total marks and percentage using methods.



# class StudentResult():

#     def __init__(self, name, sub1, sub2, sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3

#     def calculate_total(self):
#         total = self.sub1 + self.sub2 + self.sub3
#         return total

#     def calculate_percentage(self):
#         total = self.calculate_total()
#         percentage = total / 300 * 100
#         return percentage

#     def display_result(self):
#         print("Student Name:", self.name)
#         print("Total Marks:", self.calculate_total())
#         print("Percentage:", self.calculate_percentage())


# s = StudentResult("Om", 80, 85, 90)

# s.display_result()



# 19. Food Ordering System

# Create a FoodOrder class with:
# - Customer name
# - Food item
# - Food price
# - Quantity
# Create methods:
# - calculate_bill()
# - apply_coupon(discount)
# - display_order()
#     Calculate the final bill after applying the discount.




# class FoodOrder():

#     def __init__(self, name, food, price, quantity):
#         self.name = name
#         self.food = food
#         self.price = price
#         self.quantity = quantity
#         self.discount = 0

#     def calculate_bill(self):
#         total = self.price * self.quantity
#         return total

#     def apply_coupon(self, discount):
#         self.discount = discount

#         total = self.calculate_bill()
#         discount_amt = total * discount / 100
#         final_bill = total - discount_amt

#         return final_bill

#     def display_order(self):
#         print("Customer Name:", self.name)
#         print("Food Item:", self.food)
#         print("Food Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total Bill:", self.calculate_bill())
#         print("Discount:", self.discount)
#         print("Final Bill:", self.apply_coupon(self.discount))


# f = FoodOrder("Om", "Pizza", 250, 2)

# f.apply_coupon(10)

# f.display_order()



# 20. Vehicle Management System

# Create a Vehicle class with:
# - Class variable: vehicle_count
# - Instance variables: vehicle_name, vehicle_type, vehicle_price
# Create methods:
# - display_details()
# - calculate_insurance(rate)
# - update_price(new_price)
#     Count the total vehicles created and calculate insurance using the given rate.



# class Vehicle():

#     vehicle_count = 0

#     def __init__(self, vehicle_name, vehicle_type, vehicle_price):
#         self.vehicle_name = vehicle_name
#         self.vehicle_type = vehicle_type
#         self.vehicle_price = vehicle_price

#         Vehicle.vehicle_count += 1

#     def display_details(self):
#         print("Vehicle Name:", self.vehicle_name)
#         print("Vehicle Type:", self.vehicle_type)
#         print("Vehicle Price:", self.vehicle_price)

#     def calculate_insurance(self, rate):
#         insurance = self.vehicle_price * rate / 100
#         return insurance

#     def update_price(self, new_price):
#         self.vehicle_price = new_price

#         print("Updated Price:", self.vehicle_price)


# v1 = Vehicle("Swift", "Car", 700000)

# v1.display_details()

# print("Insurance Amount:", v1.calculate_insurance(5))

# v1.update_price(800000)

# print("Total Vehicles:", Vehicle.vehicle_count)
