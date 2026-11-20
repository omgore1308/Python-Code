
# Non Parameterized constructor
#  When we do not initialize parameter with contructor then it's called Non parameterized constrctor 

# class employee:
#     def __init__(self):
#         self.name = "Rohit"
#         self.age = 23
#         self.salary = 50000

#     def display_info(self):
#         print("Employee name",self.name)
#         print("age",self.age)
#         print("salary",self.salary)

# emp = employee()

# emp.display_info()



#Parameterized constructor 

# When we pass paratemeters with constructor then it's called parameterized constructor


# class Bank:

#     def __init__(self,name,age,account_type,gender):
#         self.name = name
#         self.age = age
#         self.acc_type = account_type
#         self.gender = gender

#     def display(self):
#         print("Account Holder Name : ",self.name)
#         print(" age : ",self.age)
#         print("Account_type : ",self.acc_type)
#         print("gender : ",self.gender)



# Acc_hold = Bank("ram",23,"saving","male")

# Acc_hold.display()


# Default constructor

# when we do not use contructor in class then python provide default contrctor as per inheritance mechnism.


# class library():

#     def details(self):
#         self.name = "om"
#         self.ass_book = "chava"
#         self.limit = "15 days"

#     def diplay_details(self):
#         print("Name book receiver :",self.name)
#         print("assign book :",self.ass_book)
#         print("limit :",self.limit)

# book = library()

# book.details()
# book.diplay_details()


# class variable

# class variable is assign for all objects in class

# class multiplex():

#     Movie_Name = "RAMAYANA"

#     def movie_details(self,Name,age,show_time,ticketprice):
#         self.name = Name
#         self.age = age
#         self.time = show_time
#         self.price = ticketprice

#     def ticket(self):
#         print("Name",self.name)
#         print("age",self.age)
#         print("time",self.time)
#         print("price",self.price)   
#         print("MovieName",self.Movie_Name)         


# mov = multiplex()

# mov.movie_details("rahul",23,"4:00",450)
# mov.ticket()


# mov.movie_details("virat",35,"4:00",450)
# mov.ticket()