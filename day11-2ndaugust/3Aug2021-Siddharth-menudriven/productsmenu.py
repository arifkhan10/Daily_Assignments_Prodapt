from datetime import date
import time
import re
productlist=[]
class Products:
    def addProducts(self,proname,prodescp,proprice,promanufacture,manufactdate,expdate):
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict1={"proname":proname,"prodescp":prodescp,"proprice":proprice,"promanufacture":promanufacture,"manufactdate":manufactdate,"expdate":expdate,"purchased_time":current_local_time}
        productlist.append(dict1)
obj1=Products()

def valid_product(pname,pprice):
    val=re.match("([a-z]+)([a-z]+)([a-z]+)$",pname)
    val2=re.match("[0-9]{0,7}$",pprice)
    if val and val2:
        return True
    else:
        return False


while(True):
    print("1. Add products")
    print("2. view products")
    print("3. search product by name")
    print("4. product which expire today")
    print("5. exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        while(True):
            proname=input("enter product name: ")
            proprice=input("Enter product price: ")
            if valid_product(proname,proprice):
                prodescp=input("Enter product description: ")
                promanufacture=input("enter product manufacturer: ")
                manufactdate=input("enter manufacture date: ")
                expdate=input("Enter expiry date: ")
                obj1.addProducts(proname,prodescp,proprice,promanufacture,manufactdate,expdate)
            else:
                print("PLease Try again by entering valid name and price")
                continue
            break

    if choice==2:
        print(productlist)
    if choice==3:
        searchme=input("Enter name to search product: ")
        print(list(filter(lambda a:a["proname"]==searchme,productlist)))
    if choice==4:
        today=date.today()
        d=today.strftime("%d/%m/%y")
        print(list(filter(lambda i:i["expdate"]==str(d),productlist)))     

    if choice==5:
        break