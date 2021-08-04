import re
import time
prodlist=[]

        
    

   
class productdetails():
    def addProductdetails(self,ProductName,description,price,manufacturing,expiry):
        
        current_local_time=time.strftime("%Y-%m-%d ",time.localtime())
        dict1={"ProductName":ProductName,"description":description,"price":price,"manufacturing":manufacturing,"expiry":expiry,"addedon":current_local_time}
        prodlist.append(dict1)
obj1=productdetails()
while(True):
    print("1. Add Product:")
    print("2. display product details: ")
    print("3. search product using product Name")
    print("4. list product that expire today")
    print("5. exit")
    choice=int(input("enter your choice: "))
    
    if choice==1:

        ProductName=input("Enter product Name: ")
        
        
        
        price=input("enter the price: ")
        description=input("enter the description")
        
         
        
        manufacturing=input("enter date manufacturing date in mm-dd-yyyy format" )
        expiry=input("enter date expiry date  mm-dd-yyyy format" )
        

            
        
    obj1.addProductdetails(ProductName,description,price,manufacturing,expiry)
        
    if choice==2:
        print(prodlist)
    if choice==3:
        sprod=input("Enter product want  to search: ")
        print(list(filter(lambda i:i["ProductName"]==sprod,prodlist)))
    if choice==4:
        local_current_time=time.localtime()
        find_date=time.strftime("%m-%d-%Y",local_current_time)
        expire=(list(filter(lambda i:i["expiry"]==find_date,prodlist)))
        print(expire)
        
        
        #current_local_time=time.strftime("%m-%d-%Y ",time.localtime())
        #if (current_local_time==expiry ):
        #    print (ProductName)
        ## print ('Renew License Soon')
    

    if choice==5:
        break