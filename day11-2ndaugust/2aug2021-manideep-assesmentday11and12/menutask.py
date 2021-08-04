employeedict={}
from os import name
import re,collections,time
def getdatetime():
    time1=time.localtime()
    currenttime=time.strftime("%Y-%m-%d %H:%M:%S",time1)
    return currenttime
def addemployee():
    id=int(input("enter your id:"))
    name=input("enter your name")
    designation=input("enter your designiation:")
    salary=input("enter the salary:")
    address=input("enter the address:")
    pincode=input("enter the pincode:")
    timedate1=getdatetime()
    dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode,"addedOn":timedate1}
    return dict1

def validate(dict1):
    valname=re.search("[A-z]{1}[^A-z]{0,25}$",dict1["name"])
    valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
    valpincode=re.search("(^6)[0-9]{5}$",dict1["pincode"])
    if valname and valsalary and valpincode:
        return True
    else:
        return False

while(1):
    print("1.add employee")
    print("2.view employee")
    print("3.exit")
    option =int(input("enter your option:"))
    if option==1:
        a=addemployee()
        if validate(a):
            if len(employeedict)==0:
               employeedict=collections.ChainMap(a)
            else:
               employeedict=employeedict.new_child(a)
    if option==2:
        print(employeedict)
    if option==3:
        break




