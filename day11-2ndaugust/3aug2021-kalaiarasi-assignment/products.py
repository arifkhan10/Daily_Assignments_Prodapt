import time
productlist=[]
class Productdetail:

    def addproductdetail(self,name,description,price,manufactdate,expirydate):
        
        dict1={"name":name,"description":description,"price":price,"manufactdate":manufactdate,"expirydate":expirydate}
        productlist.append(dict1)
obj1=Productdetail()
while(True):
    print("1. add product")
    print("2. view all product")
    print("3. search a product name")
    print("4. list all product that expired today:")
    print("5. exit")
    choice=int(input("enter ur choice:"))
    
    if choice==1:
        name=input("enter your name:")
        description=input("enter your description:")
        price=int(input("enter your price:"))
        manufactdate=input("enter your manuf date:")
        expirydate=input("enter your expiry date:")
        obj1.addproductdetail(name,description,price,manufactdate,expirydate)
    
    if choice==2:

        print(productlist)
    
    if choice==3:
        searchpro=input("enter your product name:")
        print(list(filter(lambda i:i["name"]==searchpro,productlist)))
    
    if choice==4:
        
        currenttime=time.localtime()
        currentclock=time.strftime("%d %m %Y",currenttime)
        print(list(filter(lambda i: i["expirydate"]==currentclock,productlist)))
    if choice==5:
        break

