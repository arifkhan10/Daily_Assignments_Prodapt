from datetime import datetime

productlist=[]
class ProductDetails:
    def addproductdetails(self,productname,description,price,manufracturingdate,expirydate):
        
        dict1={"productname":productname,"description":description,"price":price,"manufracturingdate":manufracturingdate,"expirydate":expirydate}
        studentlist.append(dict1)
obj1=ProductDetails()
while(True):
    print("1.Add products:")
    print("2.view all products:")
    print("3.Search a product:")
    print("4.list all products expire today:")
    choice=int(input("enter your choice"))
    if choice==1:
        productname=input("enter the product name:")
        description=input("enter description:")
        price=int(input("enter price :"))
        manufracturingdate=str(input("Enter mfdate(yyyy-mm-dd):"))
        print(datetime.strptime(manufracturingdate, "%Y-%m-%d"))
        expirydate=str(input("enter epdate(yyyy-mm-dd):"))
        print(datetime.strptime(expirydate, "%Y-%m-%d"))
        obj1.addproductdetails(productname,description,manufracturingdate,expirydate)
    if choice==2:
        print(productlist)
    if choice==3:
        srollno=int(input("enter your product to search:"))
        print(list(filter(lambda i:i["productname"]==sproduct,productlist)))
        break
    
    