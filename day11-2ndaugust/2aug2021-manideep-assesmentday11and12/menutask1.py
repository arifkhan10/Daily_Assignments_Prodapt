
studentlist=[]
class StudentDetails:
    # def __init__(self,name,rollno,admin,english,hindi,maths,science,social):
    #     self.name=name
    #     self.rollno=rollno
    #     self.admin=admin
    #     self.english=english
    #     self.hindi=hindi
    #     self.maths=maths
    #     self.science=science
    #     self.social=social
    def addstudentdetail(self,name,rollno,admin,english,hindi,maths,science,social):
        totalmarks=english+hindi+maths+science+social
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"englisg":english,"hindi":hindi,"maths":maths,"science":science,"social":social}
        studentlist.append(dict1)
    def validate(dict1):
      valname=re.search("[A-z]{1}[^A-z]{0,25}$",dict1["name"])
      
      if valname :
         return True
      else:
         return False
obj1=StudentDetails()
while(True):
    print("1.Add student:")
    print("2.Display students like API:")
    print("3.Search Students using rollno:")
    print("4.ranking")
    print("5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter the Student name:")
        rollno=int(input("enter your rollno:"))
        adminno=int(input("enter your adminno:"))
        english=int(input("enter your english marks:"))
        hindi=int(input("enter your hindi marks"))
        maths=int(input("enter your maths marks:"))
        science=int(input("enter your science marks:"))
        social=int(input("enter your social marks:"))
        obj1.addstudentdetail(name,rollno,adminno,english,hindi,maths,science,social)
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("enter your rollno to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i['total'],reverse=True))
    if choice==5:
        break

