import time
from datetime import datetime
productlist=[]
class productdetails:
    def addProducts(self,name,description,price,manufacturer,manufacturingdate,expirydate):
        dict1={"name":name,"description":description,"price":price,"manufacturer":manufacturer,"manufacturingddate":manufacturingdate,"expirydate":expirydate}
        productlist.append(dict1)
obj=productdetails()
while(1):
    print("1. Add products:")
    print("2. View all products:")
    print("3. Search a product:")
    print("4. List all the products that expire today :")
    print("5. Exit:")

    option=int(input("enter your choice:"))
    if option==1:
        name=input("Enter the product name:")
        description=input("Enter the product description:")
        price=input("Enter the product price:")
        manufacturer=input("Enter the product manufacturer:")
        manufacturingdate=input("Enter the product manufacturingdate:")
        expirydate=input("Enter the product expirydate:")
        obj.addProducts(name,description,price,manufacturer,manufacturingdate,expirydate)
    if option==2:
        print("list of all products")
        print(productlist)
    if option==3:
        print("Search the product")
        pname=input("enter the product name:")
        print(list(filter(lambda i:i ["name"]==pname,productlist)))
    if option==4:
        current_time=time.localtime()
        date=time.strftime("%Y-%m-%d",current_time)
        expire=(list(filter(lambda i:i["expirydate"]==date,productlist)))
        if len(expire)>0:
            print(expire)
        else:
            print("no products expired")
    if option==5:
        break
