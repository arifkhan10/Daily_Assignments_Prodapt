
employeelist=[]
class Employeedetail:
    
    def addemployeedetail(self,id,name,designation,salary,address,pincode):
        dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode}
        employeelist.append(dict1)
        
obj1=Employeedetail()

while(True):
    print("1. add employee")
    print("2. view employee")
    print("3. exit")

    choice=int(input("enter ur choice:"))

    if choice==1:
        id=int(input("enter your id:"))
        name=input("enter your name:")
        designation=input("enter your designation:")
        salary=int(input("enter your salary:"))
        address=input("enter your address:")
        pincode=int(input("enter your pincode:"))
        
        obj1.addemployeedetail(id,name,designation,salary,address,pincode)
    if choice==2:
        print("view employee")
        print(employeelist)
    if choice==3:
        break

