from datetime import datetime,time
import re
import pytz


products = [ ]

class Product_Details:
    def add_products(self,p_name,description,price,manufacturer):
        self.p_name = p_name
        self.description=description
        self.price=price
        self.manufacturer = manufacturer
        return
    def timeDate(time_zone,td):
        #time1 = time.localtime()
        time_zone = pytz.timezone("Asia/kolkata")
        #current_clock_time = time.strftime("%Y %h-%d %H:%M:%S",time1)
        td = datetime.now(time_zone).strftime("%d-%h-%Y")
        return td

class Date_of_manufacturing(Product_Details):
    def MRP(self,Manuf_Date,Expiry_Date):
        self.Manuf_Date=Manuf_Date
        self.Expiry_Date =Expiry_Date
        return
    def validation(self,val,val1):
        self.val = val(re.search("2021$",Manuf_Date))
        self.val1 = val1(re.search("2022$",Expiry_Date))
        return 

PD = Product_Details()
DM = Date_of_manufacturing()

while(True):
    
    print("1.Add product details: ")
    print("2.Displaying all the product: ")
    print("3.Searching products: ")
    print("4.List all the product that expire today")
    print("5.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Selected to add product details")
        p_name = input("enter a name of the product: ")
        description = input("enter a description: ")
        price = input("Enter a price of product: ")
        manufacturer = input("Enter manufacturer Name: ")
        Manuf_Date = input("Enter a manufactured date: ",)
        Expiry_Date = input("Enter expiry date: ")

        time_date =PD.timeDate("td")

        details ={"Product Name":p_name,"Description":description,"Prize":price,
        "manufacturer":manufacturer,"MRP Date":Manuf_Date,"Expire Date":Expiry_Date,"Time and date":time_date}
        products.append(details)
        
    if choice == 2:
        print("List of all the products")
        print(products)
    if choice == 3:
        print("To search specific product details")
        name = input("enter a product Name: ")
        print(list(filter(lambda i : i ["Product Name"]==name,products)))

    if choice == 4:
        print("To check a expired product")
        Time = PD.timeDate("td")
        print(list(filter(lambda j : j ["Expire Date"]==Time,products)))
    if choice == 5:
        break