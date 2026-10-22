"""
Q.1. ATM Menu: Write a Python program that displays an ATM menu with options: 
    1. Check Balance, 2. Deposit Money, 3. Withdraw Money, and 4. Exit. 
    Use match-case to perform the selected operation.


menu = int(input("choose the option: "))

match menu:
    case 1:
        print("Check Balance")

    case 2:
        print("Deposite Money")

    case 3:
        print("Withdraw Money")

    case _:
        print("Exit")    
        """

"""
Q.2 Restaurant Menu: Write a program that displays a menu: 
1. Pizza – ₹200, 2. Burger – ₹100, 3. Sandwich – ₹80, and 4. Coffee – ₹50. 
Ask the user to select an item and display its price.

item = input("Select your item : ")  

match item:
    case "Pizza":
        print("Rs.200")

    case "Burger":
        print("Rs.100") 

    case "Sandwich":
        print("Rs.80")

    case _:
        print("Rs.50")    

"""

"""
Q.3 Ticket Booking: Write a program that asks the user to select a ticket type:
1. Bus – ₹50, 2. Train – ₹150, 3. Flight – ₹3,000.
Display the ticket price based on the selection.

ticket = input("select your travel mode : ")

match ticket:
    case "Flight":
        print("Rs.3000")

    case "Train":
        print("Rs.150")

    case "Bus":
        print("Rs.50")          
    
    case _:
        print("mention your travel mode")
        """

"""
Q.4 Write a program that accepts an employee's role (manager, developer, or intern) and basic salary.
calculate following points and also gross salary
- Manager: 30% HRA and 20% DA.
- Developer: 20% HRA and 15% DA.
- Intern: 10% HRA and 5% DA.


Role = input("Enter your role: ")
salary = int(input("Enter your salary: "))

match Role:
    case "manager":
        HRA = salary * 30 / 100
        DA = salary * 20 / 100 
        GS = salary + HRA + DA 
        print("Your HRA is",HRA,"your DA is",DA,"Gross salary is",GS)

    case "Developer":
        HRA = salary * 20 / 100
        DA = salary * 15 / 100 
        GS = salary + HRA + DA 
        print("Your HRA is",HRA,"your DA is",DA,"Gross salary is",GS)
          

    case "intern":
        HRA = salary * 10 / 100
        DA = salary * 5 / 100 
        GS = salary + HRA + DA 
        print("Your HRA is",HRA,"your DA is",DA,"Gross salary is",GS)
    case _:
        print("invalid input")  
        """

"""
Q.5.Write a program that accepts a membership type (regular, silver, or gold),
display
- Regular members receive a 5% discount.
- Silver members receive a 10% discount.
- Gold members receive a 15% discount.


membership_type = input("select your type: ")

match membership_type:
    case "Regular":
        print("5 % Discount")
        
    case "Silver":
        print("10 % Discount")
                
    case "Gold":
        print("15 % Discount")
                
    case _:
        print("Invalid input")
            
"""

"""
Q.6 Vending Machine: Write a program that accepts a product code: A1 for Water (₹20), A2 for Juice (₹40), B1 for Chips (₹30), and B2 for Chocolate (₹25).
Display the product name and price. If the code is invalid, display an appropriate message.

product_code = input("Enter your Product code: ")

match product_code:
    case "A1":
        print("Water(Rs.20)")

    case "A2":
        print("Juice(Rs.40)") 

    case "A3":
        print("Chips(Rs.30)")

    case "B2":
        print("Chocolate(Rs.25)") 

    case _:
        print("Invalid input") 
        """


"""
Q.7.Bank Customer Support: Write a program that displays options: 1. Account Balance, 2. Loan Information, 3. Report a Lost Card, and 4. Talk to Customer Support.
lay the appropriate message for the selected option.


custmor_support = int(input("Click your option: "))

match custmor_support:
    case 1:
        print("Account Balance")

    case 2:
        print("Loan Information")  

    case 3:
        print("Report a Lost Card")

    case 4:
        print("Talk to customer support")  

    case _:
        print("Invalid Input") 
             """


"""
Q.8 Online Payment Gateway

Write a program that accepts a payment method (UPI, Card, Net Banking, or Wallet) and displays the corresponding payment instructions.
- UPI → Enter UPI ID.
- Card → Enter card details.
- Net Banking → Select your bank.
- Wallet → Select your wallet provider.
- Use case _ for unsupported payment methods.


Payment_method = input("Select Payment Method: ")

match Payment_method:
    case "UPI":
        print("Enter UPI Id")


    case "Card":
        print("Enter Card pin")
        
    case "Net Banking":
            print("Select your Bank")

    case "wallet":
        print("Select Your Wallet Provider")

    case _:
        print("Unsupported Payment Method")
            
"""


"""
Q.9 Vehicle Rental System

Write a program that accepts a vehicle type (bike, car, suv, or scooter) and displays the rental charge per day.
- Bike: ₹500
- Car: ₹1,500
- SUV: ₹2,500
- Scooter: ₹300
- Display an appropriate message for an invalid vehicle type.

Vehicle = input("Select vehicle Type: ")

match Vehicle:
    case "bike":
        print("Rent Rs.500")

    case "car":
        print("Rent Rs.1500") 

    case "SUV":
        print("Rent Rs.2500")

    case "scooter":
        print("Rent Rs.300") 

    case _:
        print("Invalid vehicle type")  
        """  

"""
Q.10 Write a Python program that accepts a train ticket class (1AC, 2AC, 3AC, Sleeper, or General) and displays the facilities available in that class using match-case.
- 1AC → First AC: Premium bedding, meals, and private cabins.
- 2AC → Second AC: AC coach, sleeping berths, and curtains.
- 3AC → Third AC: AC coach and sleeping berths.
- Sleeper → Non-AC coach with sleeping berths.
- General → Unreserved seating.
- Use case _ to display "Invalid ticket class!" for any unsupported choice.


ticket_class = input("select your ticket class: ")

match ticket_class:
    case "1AC":
        print("Premium bed,meals,Private Cabins")

    case "2AC":
        print("AC Coach,sleeping births,curtains")

    case "3AC":
        print("AC Coach,sleeping births")

    case "Sleeper":
        print("Non AC coach,sleeping births")

    case "General":
        print("unreserved seating")

    case _:
        print("Invalid ticket class")    
        
        """
       
       
       