emp = {}
from os import name
import collections,time,re

def getdatetime():
    time1 = time.localtime()
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time1)
    return cur_time
def addEmployee():
    empid = input("Enter empid:")
    name = input("Enter your name:")
    designation = input("Enter your designation:")
    salary = input("Enter the salary:")
    address = input("Enter address:")
    pincode = input("Enter the pincode:")

    dict1 = {"empid": empid, "name" : name,"designation":designation,"salary":salary, "address":address, "pincode":pincode }

    return dict1
def val(dict1):
    valname = re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
    valsalary = re.search("[0-9]{0,7}$",dict1["salary"])
    valpincode = re.search("(^6)[0-9]{5}$",dict1["pincode"])

    if valname and valpincode and valsalary:
        return dict1
    else:
        return False

while(1):
    print("1.Add Employee:")
    print("2. View Empolyee details")
    print("3.Exit")

    option = int(input("Enter your choice:"))
    if option == 1:
        x = addEmployee()
        if val(x):
            dict1 = validate(x)
            if len(emp) == 0:
                emp = collections.ChainMap(dict1)
            else:
                emp = emp.new_child(dict1)
    if option == 2:
        print(emp.maps)
    if option == 3:
        break      
                          








