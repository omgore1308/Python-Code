# class car():

#     def detail(self,name,type,colour,price):
#         self.name = name
#         self.type = type
#         self.colour = colour
#         self.price = price

    
#     def display(self):
#         print("car name -->",self.name)   
#         print("car type -->",self.type)
#         print("car colour -->",self.colour)
#         print("car price -->",self.price)    
            
            
# a = car()        
# a.detail("bmw","sport","black",8800000)
# a.display()



# class shopping_cart:

#     def set_details(self,name,p_name,price,quantity):
#         self.customer_name = name
#         self.product_name = p_name
#         self.price = price
#         self.quantity = quantity
#         self.discount = 0
       

#     def cal_total(self):
#         self.total = self.price * self.quantity
        

#     def dis(self):
#         if self.total > 25000:
#             self.discount = self.total * 10 / 100
#             print("Discount",self.discount)
        

#         else:
#             print("you are not valid for discount")
        
#     def total_bill(self):
#         print("custm_name : " , self.customer_name) 
#         print("p_name : ",self.product_name)
#         print("price : ",self.price)
#         print("quantity : ",self.quantity)
#         print("total : ",self.total)
#         print("Discount : ",self.discount)
#         print("final bill : ", self.total - self.discount)
        
    
# a = shopping_cart()
# a.set_details("om","shirt",8000,5)
# a.cal_total()
# a.dis()
# a.total_bill()






# class library_book:
#     def set_details(self):
#         self.bookname = "syamchi aai"
#         self.auth_name = "sane guruji"
#         self.price = 1000
#         self.status = True

    

#     def issue_book(self):
#         self.status = False
#         print("Book is issued successully")

#     def return_book(self):
#         self.status = True
#         print("return Book successfully")  


#     def display_details(self):
#             print("bookname : ",self.bookname)    
#             print("authorname : ",self.auth_name)
#             print("price : ",self.price)
#             print("is_available : ",self.status)      

# a = library_book()

# a.set_details()

# a.display_details()

# a.issue_book()
# a.display_details()

# a.return_book()
# a.display_details()




# class eletricity_bill():

#     def cutm_details(self):
#         self.name = "Ram"
#         self.units = 500

#     def cal_bill(self):
#         if self.units <= 100:
#            print("first 100 units",self.units * 3)

#         elif self.units <= 200:
#             print("next 100 units",(self.units - 100) * 5)   

#         else:
#             print("units above 200",(self.units - 200) * 8)    


#     def display_bill(self):
#         print("customer_name",self.name)
#         print("units_consumed",self.units)
#         bill = (100 * 3) + (100 * 5) + ((self.units - 200) * 8)
#         print("Final Bill",bill)


# finalbill = eletricity_bill()

# finalbill.cutm_details()

# finalbill.cal_bill()

# finalbill.display_bill()
                


         




