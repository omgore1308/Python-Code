# Create an abstract class Animal with an abstract method eat(). Implement it in Dog and
#  Cow

# from abc import ABC , abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def eat(self):
#         pass

# class Dog(Animal):

#     def eat(self):
#         print("Dog Eats slower beacuse it has small mouth")


# class Cow(Animal):

#     def eat(self):
#         print("Cow Eats Faster Because it has big mouth")        


# D = Dog()
# D.eat()

# C = Cow()
# C.eat()

# 2. Create an abstract class Vehicle with start() and stop(). Implement both methods in Bike and Car


# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass
    
#     def stop(self):
#         pass
        
       
# class Car(Vehicle):

#     def start(self):

#         self.type = "Car"
#         self.startSystem = "By Button"
        
#         print("Vehicle Name :",self.type)
#         print("Car Start with :",self.startSystem)

#     def stop(self):

#         self.Stopsystem = "Using Brake"
#         print("Car Stop With :",self.Stopsystem)
#         print("--------------------------------")                



# class Bike(Vehicle):

#     def start(self):
#         self.type = "Bike"
#         self.startSystem = "By Button"
    
#         print("Vehicle Name :",self.type)
#         print("Bike Start with :",self.startSystem)
    
#     def stop(self):
#         self.Stopsystem = "Using Brake"
        
#         print("Bike Stop With :",self.Stopsystem)
        


# C = Car()
# C.start()
# C.stop()

# B = Bike()
# B.start()
# B.stop()
                       
# 3. Create an abstract class Bank with calculate_interest(). Implement different sample 
# interest rates in SBI and HDFC
    

# from abc import ABC, abstractmethod

# class Bank(ABC):

#     @abstractmethod
#     def calculate_interest(self):
#         pass

# class SBI(Bank):

#     def calculate_interest(self):
#         self.amount = 50000
#         self.interest_rate = 3.5
#         self.time = 2

#         print("Bank Name : SBI")
#         print(" Deposite Amount :",self.amount)
#         print("interest Rate :",self.interest_rate,"%")
#         print("Time :",self.time,"yrs")
#         print("Simple Interest :",(self.amount * self.interest_rate * self.time) / 100)
#         print("----------------------------------------------------------------------")


# class HDFC(Bank):

#     def calculate_interest(self):
#         self.amount = 100000
#         self.interest_rate = 4.5
#         self.time = 2
    
#         print("Bank Name : HDFC")
#         print(" Deposite Amount :",self.amount)
#         print("interest Rate :",self.interest_rate,"%")
#         print("Time :",self.time,"yrs")
#         print("Simple Interest :",(self.amount * self.interest_rate * self.time) / 100)
       
        


# S = SBI()
# S.calculate_interest()

# H = HDFC()
# H.calculate_interest()
    

#Create an abstract class Shape with calculate_area(). Implement Circle, Rectangle and Triangle.

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def calculate_area(self):
#         pass


# class Circle(Shape):

#     def calculate_area(self):
#         print("Area of Circle")
#         print("-----------------")


# class Rectangle(Shape):

#     def calculate_area(self):
#         print("Area of Rectangle")
#         print("-----------------")

# class Triangle(Shape):

#     def calculate_area(self):
#         print("Area of Triangle")

# C = Circle()
# C.calculate_area()

# R = Rectangle()
# R.calculate_area()

# T = Triangle()
# T.calculate_area()



# 5. Create an abstract class Employee with calculate_salary(). Implement it in Manager and Developer

# from abc import ABC, abstractmethod

# class Employee(ABC):

#     @abstractmethod
#     def calculate_salary(self):
#         pass


# class Manager(Employee):

#     def calculate_salary(self):
#         print("Salary For Manager")
#         print("--------------------")

# class Developer(Employee):

#     def calculate_salary(self):
#         print("Salary For Developer")


# M = Manager()
# M.calculate_salary()

# D = Developer()
# D.calculate_salary()


# 6. Create an abstract class Payment with make_payment(). Implement CardPayment, UpiPayment and CashPayment

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def make_payment(self):
#         pass

# class CardPayment(Payment):

#     def make_payment(self,amount):
#         print("Card Payment :",amount)
#         print("----------------------")

# class UpiPayment(Payment):

#     def make_payment(self,amount):
#         print("Upi Payment :",amount)
#         print("--------------------")

# class CashPayment(Payment):

#     def make_payment(self,amount):
#         print("Cash Payment :",amount)
#         print("---------------------")

# Payments = [
#     CardPayment(),
#     UpiPayment(),
#     CashPayment()   
#     ]

# for payment in Payments:
#     payment.make_payment(500)                


# 7. Create an abstract class Notification with send_notification(). Implement 
# EmailNotification and SMSNotification.     


# from abc import ABC, abstractmethod       

# class Notification(ABC):

#     @abstractmethod
#     def send_notification(self):
#         pass


# class EmailNotification(Notification):

#     def send_notification(self):
#         print("Email Notification")
#         print("-------------------")

# class  SMSNotification(Notification):

#     def send_notification(self):
#         print("SMS Notification")
#         print("-----------------")


# E = EmailNotification()
# E.send_notification()

# S = SMSNotification()
# S.send_notification()


