# 2. Student Marks Management (Easy)
# Create a Student class with:
# - Private variable: __marks
# - Create a method set_marks() to assign marks.
# - Create a method get_marks() to display marks.
# - Marks should be between 0 and 100.
# - If marks are invalid, display an error message.

        
# class Student():

#     def __init__(self,marks):
#         self.__marks = marks
        
    
#     def set_marks(self,newmarks):
#         if newmarks >= 0 and newmarks <= 100:
#             self.__marks = newmarks
#             print("Marks update successfully")
                    
#         else:   
#             print("Invalid Marks")

    
#     def get_marks(self):
#         print("Students Marks :",self.__marks)


        

    
# s = Student(85)

# s.get_marks()


# s.set_marks(-75)
# s.get_marks()


# 3. Employee Salary Management (Medium)
# Create an Employee class with:
# - Instance variables: name, department
# - Private variable: __salary
# - Create a method to set employee salary.
# - Create a method to get employee salary.
# - Salary should not be negative.
# - Display all employee details.




# class Employee():

#     def __init__(self,name,department,Salary):
#         self.name = name
#         self.department = department
#         self.__salary = Salary


#     def set_empsalary(self,new_salary):
#         if new_salary <= 0 :
#             print("Salary Never be Nagative")

#         else:
#             self.__salary = new_salary
#             print("Salary update Successfully")    

#     def get_empsalary(self):
#         print("Salary :",self.__salary)

#     def emp_details(self):
#         print("Employee Name :",self.name)
#         print("Department :",self.department)
        


# emp = Employee("Om","Software Devlopement",45000)

# emp.emp_details()
# emp.get_empsalary()

# emp.set_empsalary(55000)
# emp.get_empsalary()
        

# 4. ATM PIN Verification (Medium)
# Create an ATM class with:
# - Private variable: __pin
# - Private variable: __balance
# - Create a method check_pin() to verify the PIN.
# - Create a method withdraw() to withdraw money only if the PIN is correct.
# - Create a method display_balance() to display the balance.



# class Atm():

#     def __init__(self,pin,balance):
#         self.__pin = pin
#         self.__balance = balance

#     def set_check_pin(self,A_pin,amount):
#         if self.__pin == A_pin :

#             if amount < 0 :
#                 print("Invalid Amount")

#             elif self.__balance >= amount:
#                 self.__balance -= amount
#                 print("Transaction Successful")    
                
#             else:
#                 print("Insufficient Balance")

            
#         else:    
#             print("Re-Enter your Pin")

#     def get_display_balance(self,A_pin):
#         if self.__pin == A_pin: 
#             print("Remaining Balance :",self.__balance)


# B = Atm(1308,50000)
# B.set_check_pin(1308,10000)
# B.get_display_balance(1308)



# 5. Product Price Management (Medium)
# Create a Product class with:
# - Instance variable: product_name
# - Private variable: __price
# - Create a method set_price() to update the product price.
# - Create a method get_price() to display the price.
# - Price should always be greater than zero.
# - Create three product objects and display their details.





# class Product():

#     def __init__(self,P_name,price):
#         self.name = P_name
#         self.__price = price

#     def set_price(self,new_price):
#         if new_price >= 0:
#             self.__price = new_price
#             print("Price Update Successfully")

#         else:
#             print("Price should always be greater than zero")

#     def get_price(self):
#         print("Product Price :",self.__price)
    
    
#     def display_details(self):
#         print("Product Name :",self.name)
        



# A1 = Product("shirt",1000)

# A1.display_details()
# A1.get_price()
# A1.set_price(1500)
# A1.get_price()

# print("------------------------------------------------")

# A2 = Product("pant",2000)

# A2.display_details()
# A2.get_price()
# A2.set_price(1000)
# A2.get_price()

# print("-----------------------------------------")

# A3 = Product("shoes",3000)
# A3.display_details()
# A3.get_price()
# A3.set_price(5000)
# A3.get_price()

