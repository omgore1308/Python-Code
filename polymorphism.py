# 1. Animal Sound: Create an Animal class with a method sound(). Create child classes Dog and Cat.
#  Override the sound() method in both child classes to display their respective sounds.


# class Animal():

#     def sound(self):
#         pass


# class Dog(Animal):
#     def sound(self):
#         self.Dog_sound = "Bark"
#         print("Dog sounds :",self.Dog_sound)

# class Cat(Animal):
#     def sound(self):
#         self.Cat_sound = "Meow"
#         print("Cat sounds :",self.Cat_sound)


# Dog().sound()

# Cat().sound()



# 2. Vehicle Starting System: Create a Vehicle class with a method start(). Create child classes 
# Car, Bike, and Bus. Override the start() method to display how each vehicle starts.


# class Vehicle():

#     def start(self):
#         pass

# class Car(Vehicle):

#     def start(self):
#         self.car_start = "By Button"
#         print("Car start by :",self.car_start)

# class Bike(Vehicle):

#     def start(self):
#         self.bike_start = "By switch on Key"
#         print("Bike start info :",self.bike_start)

# class Bus(Vehicle):

#     def start(self):
#         self.bus_start = "By Key and Press Button"
#         print("Bus Start info :",self.bus_start)


# C = Car()
# C.start()

# B = Bike()
# B.start()

# Bu = Bus()
# Bu.start()


# 3. Employee Salary: Create an Employee class with a method calculate_salary(). Create child 
# classes FullTimeEmployee and PartTimeEmployee. Override the method to calculate their salaries differently.


# class Employee():

#     def calculate_salary(self):
#         pass

# class FullTimeEmployee(Employee):

#     def calculate_salary(self,salary):
#         self.F_salary = salary
#         print("FullTimeEmployee salary :",self.F_salary)


# class PartTimeEmployee(Employee):

#     def calculate_salary(self,salary):
#         self.P_salary = salary
#         print("PartTime salary :",self.P_salary)


# F_S = FullTimeEmployee()
# F_S.calculate_salary(60000)

# P_S = PartTimeEmployee()
# P_S.calculate_salary(30000)


# 4. Shape Area: Create a Shape class with a method area(). Create child classes Rectangle, Square,
#  and Circle. Override the method to calculate the area of each shape.


# class Shape():

#     def area(self):
#         pass


# class Rectangle(Shape):

#     def area(self,length,width):
#         self.len_R = length
#         self.wid_R = width 

#         print("Length of Rectangle :",self.len_R)
#         print("Width of Rectangle :",self.wid_R)
#         print("Area of Rectangle :",self.len_R * self.wid_R)
#         print("--------------------------------------------")

# class Square(Shape):

#     def area(self,length,width):
#         self.len_S = length
#         self.wid_S = width

#         print("Length of Square :",self.len_S)
#         print("Width of Square :",self.wid_S)
#         print("Area of Square :",self.len_S * self.wid_S)


# R = Rectangle()
# R.area(30,50)

# S = Square()
# S.area(40,40)

        
# 5. Payment System: Create a Payment class with a method pay(). Create child classes UPIPayment,
#  CardPayment, and CashPayment. Override the method to display different payment details.



# class Payment():

#     def pay(self):
#         pass


# class UPIPayment(Payment):

#     def pay(self,app):
#         self.upi_app = app
#         print("Payment Method using :",self.upi_app)
#         print("-----------------------------------")

# class CardPayment(Payment):

#     def pay(self,cardtype):
#         self.Card_payment = cardtype
#         print("Payment method using :",self.Card_payment)
#         print("----------------------------------------")

# class CashPayment(Payment):

#     def pay(self):
#         self.Cash_payment = "Cash"
#         print("Payment method using :",self.Cash_payment)

# U = UPIPayment()
# U.pay("Google Pay")

# C = CardPayment()
# C.pay("Credit Card")

# Cash = CashPayment()
# Cash.pay()


# 6. Bank Interest System: Create a Bank class with a method calculate_interest(). Create child
# classes SBI, HDFC, and ICICI. Override the method to calculate interest according to each bank's 
# rate.


# class Bank():
#    def calculate_interest(self):
#       pass

# class SBI(Bank):
#    def calculate_interest(self,amount,rate,Time):
#       self.amount = amount
#       self.rate = rate
#       self.time = Time
#       SI = (self.amount * self.rate * self.time)/100

#       print("BanK Name :SBI")
#       print("Deposite Amount :",self.amount)
#       print("Rate of interest :",self.rate,"%")
#       print("Time :",self.time,"yrs")
#       print("simple interest :",SI)
#       print("Total Amount :",SI + self.amount)
#       print("--------------------------------")


# class HDFC(Bank):
#    def calculate_interest(self,amount,rate,Time):
#         self.amount = amount
#         self.rate = rate
#         self.time = Time
#         SI = (self.amount * self.rate * self.time)/100
   
#         print("BanK Name :HDFC")
#         print("Deposite Amount :",self.amount)
#         print("Rate of interest :",self.rate,"%")
#         print("Time :",self.time,"yrs")
#         print("simple interest :",SI)
#         print("Total Amount :",SI + self.amount)
#         print("--------------------------------")
   

# class ICICI(Bank):

#     def calculate_interest(self,amount,rate,Time):
#         self.amount = amount
#         self.rate = rate
#         self.time = Time
#         SI = (self.amount * self.rate * self.time)/100
       
#         print("BanK Name :ICICI")
#         print("Deposite Amount :",self.amount)
#         print("Rate of interest :",self.rate,"%")
#         print("Time :",self.time,"yrs")
#         print("simple interest :",SI)
#         print("Total Amount :",SI + self.amount)
#         print("--------------------------------")  



# S = SBI()
# S.calculate_interest(50000,3.5,2)
     
# HD = HDFC()
# HD.calculate_interest(50000,5,2)


# IC = ICICI()
# IC.calculate_interest(50000,4,2)        

        
# 7. Electricity Bill: Create an ElectricityBill class with a method calculate_bill().
#  Create child classes Residential and Commercial. Override the method to calculate electricity
#  bills using different unit rates.

# class ElectricityBill():

#     def calculate_bill(self):
#         pass

# class residential(ElectricityBill):

#     def calculate_bill(self,units):
#         self.units = units

#         if self.units <= 100:
#             print("For First 100 units :",self.units * 3)

#         elif self.units <= 200:
#             print("For next 100 units :",(self.units - 100) * 5)

#         else: 
#             print("Above 200 units :",(self.units - 200) * 7)

#     def displayBill(self):    
#         print("Total Bill :",(100 * 3) + (100 * 5) + (self.units - 200) * 7)  
#         print("---------------------------------------------------")

# class Commercial(ElectricityBill):

#     def calculate_bill(self,units):
#         self.units = units

#         if self.units <= 100:
#             print("For First 100 units :",self.units * 5)

#         elif self.units <= 200:
#             print("For next 100 units :",(self.units - 100) * 7)

#         else: 
#             print("Above 200 units :",(self.units - 200) * 10)

#     def displaybill(self):    
#         print("Total Bill :",(100 * 5) + (100 * 7) + (self.units - 200) * 10)  
#         print("---------------------------------------------------")
  


# R = residential()
# R.calculate_bill(90)
# R.displayBill()

# C = Commercial()
# C.calculate_bill(400)
# C.displaybill()


# 8. Discount System: Create a Product class with a method calculate_discount(). Create child
#  classes Electronics, Clothing, and Grocery. Override the method to apply different discount
# percentages.

# class Product():

#     def calculate_discount(self):
#         pass

# class Electronics(Product):

#     def calculate_discount(self,P_name,MRP,discount):
#         self.pname = P_name
#         self.mrp = MRP
#         self.discount = discount
#         Total = self.mrp - self.mrp * self.discount / 100
#         print("Product Name :",self.pname)
#         print("MRP :",self.mrp)
#         print("Discount :",self.discount,"%")
#         print("Total Amount :",Total)
#         print("--------------------------------------------------")

# class Clothing(Product):

#     def calculate_discount(self,P_name,MRP,discount):
#             self.pname = P_name
#             self.mrp = MRP
#             self.discount = discount
#             Total = self.mrp - self.mrp * self.discount / 100

#             print("Product Name :",self.pname)
#             print("MRP :",self.mrp)
#             print("Discount :",self.discount,"%")
#             print("Total Amount :",Total)
#             print("--------------------------------------------------")

# class Grocery(Product):

#      def calculate_discount(self,P_name,MRP,discount):
#             self.pname = P_name
#             self.mrp = MRP
#             self.discount = discount
#             Total = self.mrp - self.mrp * self.discount / 100
#             print("Product Name :",self.pname)
#             print("MRP :",self.mrp)
#             print("Discount :",self.discount,"%")
#             print("Total Amount :",Total)
#             print("--------------------------------------------------")            
            

# E = Electronics()
# E.calculate_discount("TV",80000,5)

# C = Clothing()
# C.calculate_discount("Jacket",4000,10)

# G = Grocery()
# G.calculate_discount("oil",3000,5)


# 9. Ticket Booking: Create a Ticket class with a method calculate_price(). 
# Create child classes MovieTicket, BusTicket, and TrainTicket. Override the method to 
# calculate ticket prices differently.            


# class Ticket():

#     def calculate_price(self):
#         pass

# class MovieTicket(Ticket):

#     def calculate_price(self,price,count):

#         self.price = price
#         self.count = count
#         print("Price of ticket :",self.price)
#         print("Count of Ticket :",self.count)
#         print("Total Movie Ticket Price :",self.price * self.count)
#         print("------------------------------------------------------")

# class BusTicket(Ticket):

#     def calculate_price(self,price,count):
    
#         self.price = price
#         self.count = count
#         print("Price of ticket :",self.price)
#         print("Count of Ticket :",self.count)
#         print("Total Bus Ticket Price :",self.price * self.count)
#         print("--------------------------------------------------")


# class TrainTicket(Ticket):

#     def calculate_price(self,price,count):
    
#         self.price = price
#         self.count = count
#         print("Price of ticket :",self.price)
#         print("Count of Ticket :",self.count)
#         print("Total Train Ticket Price :",self.price * self.count)
#         print("---------------------------------------------------")     


# M = MovieTicket()
# M.calculate_price(500,4)

# B = BusTicket()
# B.calculate_price(100,2)

# T = TrainTicket()
# T.calculate_price(750,6)


# 10. Delivery Charges: Create a Delivery class with a method calculate_charge(). Create child 
# classes NormalDelivery, ExpressDelivery, and SameDayDelivery. Override the method to calculate 
# delivery charges based on delivery type.



# class Delivery():

#     def cal_charge(self):
#         pass

# class NormalDelivery(Delivery):

#     def cal_charge(self,charge):
#         self.charge = charge
#         print("charge of Normal Delivery :",self.charge)
#         print("----------------------------------------")

# class ExpressDelivery(Delivery):

#     def cal_charge(self,charge):
#         self.charge = charge
#         print("Charge of Express Delivery :",self.charge)
#         print("----------------------------------------")
        
# class SameDayDelivery(Delivery):         

#     def cal_charge(self,charge):
#         self.charge = charge
#         print("Charge of Express Delivery :",self.charge)
#         print("----------------------------------------")



# N = NormalDelivery()
# N.cal_charge(10)

# E = ExpressDelivery()
# E.cal_charge(30)

# S = SameDayDelivery()
# S.cal_charge(50)


# 11. ATM Withdrawal: Create an ATM class with a method withdraw(). Create child classes 
# SavingsAccount and CurrentAccount. Override the method to apply different withdrawal limits 
# and minimum balance conditions.


# class ATM():

#     def withdraw(self):
#         pass

# class SavingAccount(ATM):

#     def withdraw(self,type,limit,minimum_balance):
#         self.type = type
#         self.W_limit = limit
#         self.Min_Balance = minimum_balance

#         print("Account Type :",self.type)
#         print("WithDrawal Limit :",self.W_limit)
#         print("Minimum Balance :",self.Min_Balance)
#         print("-------------------------------------")

# class CurrentAccount(ATM):

#     def withdraw(self,type,limit,minimum_balance):
#         self.type = type
#         self.W_limit = limit
#         self.Min_Balance = minimum_balance
    
#         print("Account Type :",self.type)
#         print("WithDrawal Limit :",self.W_limit)
#         print("Minimum Balance :",self.Min_Balance)
#         print("-------------------------------------")


# S = SavingAccount()
# S.withdraw("Saving",50000,2000)

# C = CurrentAccount()
# C.withdraw("Current",100000,10000)



# 12. Student Result System: Create a Student class with a method calculate_result(). Create
# child classes EngineeringStudent, MedicalStudent, and CommerceStudent. Override the method 
# to calculate results according to different subject marks and passing criteria.

# class Student():

#     def calculate_result(self):
#         pass

# class EngineeringStudent(Student):

#     def calculate_result(self,Deep_learning,ISR,MC,WC):
#         self.Dmarks = Deep_learning
#         self.Imarks = ISR
#         self.MCmarks = MC
#         self.Wcmarks = WC

        

#         print("Feild : Engineering")
#         print("Deep Learning Marks :",self.Dmarks)
#         print("ISR Marks :",self.Imarks)
#         print("Mobile Computing Marks :",self.MCmarks)
#         print("Wireless Communication Marks :",self.Wcmarks)

#         Total = self.Dmarks + self.Imarks + self.MCmarks + self.Wcmarks 

#         Total_percentage = Total * 100 / 280

#         print("Total Marks :", Total)
#         print("Percentage :", Total_percentage, "%")


#         if Total_percentage >= 35:
#             print("Result :","Pass") 
        
#         else:
#             print("Result :","Fail") 

#         print("----------------------------------------------------")       


# class MedicalStudent(Student):

#     def calculate_result(self, Biology, Chemistry, Physics, English):

#         self.Bmarks = Biology
#         self.Cmarks = Chemistry
#         self.Pmarks = Physics
#         self.Emarks = English

#         print("Feild : Medical")
#         print("Biology Marks :", self.Bmarks)
#         print("Chemistry Marks :", self.Cmarks)
#         print("Physics Marks :", self.Pmarks)
#         print("English Marks :", self.Emarks)

#         Total = self.Bmarks + self.Cmarks + self.Pmarks + self.Emarks

#         Total_percentage = Total * 100 / 280

#         print("Total Marks :", Total)
#         print("Percentage :", Total_percentage, "%")

#         if Total_percentage >= 35:
#             print("Result :", "Pass")

#         else:
#             print("Result :", "Fail")

#         print("----------------------------------------------------")    


# class CommerceStudent(Student):

#     def calculate_result(self, Accountancy, Economics, Business_Studies, English):

#         self.Amarks = Accountancy
#         self.Ecomarks = Economics
#         self.Bmarks = Business_Studies
#         self.Engmarks = English

#         print("Feild : Commerce")
#         print("Accountancy Marks:", self.Amarks)
#         print("Economics Marks:", self.Ecomarks)
#         print("Business Studies Marks:", self.Bmarks)
#         print("English Marks:", self.Engmarks)

#         Total = self.Amarks + self.Ecomarks + self.Bmarks + self.Engmarks

#         Total_percentage = Total * 100 / 280

#         print("Total Marks :", Total)
#         print("Percentage :",Total_percentage, "%")

#         if Total_percentage >= 35:
#             print("Result :", "Pass")

#         else:
#             print("Result :", "Fail")


# E = EngineeringStudent()   
# E.calculate_result(60,45,56,44)


# M = MedicalStudent()
# M.calculate_result(75, 65, 70, 80)

# C = CommerceStudent()
# C.calculate_result(80, 75, 85, 70)


# 13. Food Ordering System: Create a Food class with a method calculate_price(). Create child
# classes Pizza, Burger, and Sandwich. Override the method to calculate the final price based
# on quantity and additional toppings.


# class Food():

#     def calculate_price(self):
#         pass

# class pizza(Food):

#     def calculate_price(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


#         print("Dish Name :",self.name)
#         print("price :",self.price)
#         print("quantity :",self.quantity)
#         print("Total Amount :",self.price * self.quantity)
#         print("-------------------------------------------")

# class Burger(Food):

#     def calculate_price(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
    
#         print("Dish Name :",self.name)
#         print("price :",self.price)
#         print("quantity :",self.quantity)
#         print("Total Amount :",self.price * self.quantity)
#         print("-------------------------------------------")


# class Sandwich(Food):

#     def calculate_price(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
        
#         print("Dish Name :",self.name)
#         print("price :",self.price)
#         print("quantity :",self.quantity)
#         print("Total Amount :",self.price * self.quantity)
#         print("-------------------------------------------")


# P = pizza()
# P.calculate_price("Pizza",300,2)

# B = Burger()
# B.calculate_price("Burger",150,2)

# S = Sandwich()
# S.calculate_price("Sandwich",170,1)



# 14.Online Shopping System: Create a Shopping class with a method final_amount(). Create child 
# classes PrimeCustomer and RegularCustomer. Override the method to calculate the final amount 
# after applying different discounts and delivery charges.    
            

# class Shopping():

#     def final_amount(self):
#         pass

# class PrimeCustomer(Shopping):

#     def final_amount(self,Shop_price,discount,delivery_charges):

#         self.shop_price = Shop_price
#         self.discount = discount
#         self.delivery_charge = delivery_charges

#         print("Customer type : Prime Customer")
#         print("Shopping Price :",self.shop_price)
#         print("Discount :",self.discount,"%")
#         print("Delivery charges :",self.delivery_charge)

#         Discount = self.shop_price * self.discount / 100
#         print("Discount :",Discount)

#         Total = self.shop_price - Discount
#         print("Total :",Total)

#         Pay = Total + self.delivery_charge
#         print("Total Pay :",Pay) 

#         print("-------------------------------------------------")

# class RegularCustomer(Shopping):

#     def final_amount(self,Shop_price,discount,delivery_charges):
    
#         self.shop_price = Shop_price
#         self.discount = discount
#         self.delivery_charge = delivery_charges
    
#         print("Customer type : Regular Customer")
#         print("Shopping Price :",self.shop_price)
#         print("Discount :",self.discount,"%")
#         print("Delivery charges :",self.delivery_charge)
    
#         Discount = self.shop_price * self.discount / 100
#         print("Discount :",Discount)
    
#         Total = self.shop_price - Discount
#         print("Total :",Total)
    
#         Pay = Total + self.delivery_charge
#         print("Total Pay :",Pay) 


# P = PrimeCustomer()
# P.final_amount(10000,15,0)

# R = RegularCustomer()
# R.final_amount(5000,10,50)
    


# 15.Cab Booking System: Create a Cab class with a method calculate_fare(). Create child classes 
# MiniCab, SedanCab, and SUV. Override the method to calculate fares based on distance, base fare,
# and per-kilometre charges.

# class Cab():

#     def calculate_fare(self):
#         pass


# class MiniCab(Cab):

#     def calculate_fare(self, distance):

#         self.distance = distance
#         self.base_fare = 50
#         self.per_km = 10

#         Total_fare = self.base_fare + (self.distance * self.per_km)

#         print("Cab Type: MiniCab")
#         print("Distance:", self.distance, "KM")
#         print("Base Fare:", self.base_fare)
#         print("Per KM Charge:", self.per_km)
#         print("Total Fare:", Total_fare)
#         print("--------------------------------")


# class SedanCab(Cab):

#     def calculate_fare(self, distance):

#         self.distance = distance
#         self.base_fare = 100
#         self.per_km = 15

#         Total_fare = self.base_fare + (self.distance * self.per_km)

#         print("Cab Type: SedanCab")
#         print("Distance:", self.distance, "KM")
#         print("Base Fare:", self.base_fare)
#         print("Per KM Charge:", self.per_km)
#         print("Total Fare:", Total_fare)
#         print("--------------------------------")


# class SUV(Cab):

#     def calculate_fare(self, distance):

#         self.distance = distance
#         self.base_fare = 150
#         self.per_km = 20

#         Total_fare = self.base_fare + (self.distance * self.per_km)

#         print("Cab Type: SUV")
#         print("Distance:", self.distance, "KM")
#         print("Base Fare:", self.base_fare)
#         print("Per KM Charge:", self.per_km)
#         print("Total Fare:", Total_fare)
#         print("--------------------------------")


# M = MiniCab()
# M.calculate_fare(10)

# S = SedanCab()
# S.calculate_fare(10)

# U = SUV()
# U.calculate_fare(10)       




