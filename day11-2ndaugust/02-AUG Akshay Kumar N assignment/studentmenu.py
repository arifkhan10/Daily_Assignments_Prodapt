student = {}
import collections,time

studentlist = []
class StudentDetails:
    #1
    # def __init__(self,name,rollno,admin,english,hindi,maths,science,social):
        # self.name = name
        # self.rollno = rollno
        # self.admin = admin
        # self.english = english
        # self.hindi = hindi
        # self.maths = maths
        # self.science = science
        # self.social = social

    def addStudentDetail(self,name,rollno,admin,english,hindi,maths,science,social):
        totalmarks = english+hindi+maths+science+social
        dict1 = {"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social}
        studentlist.append(dict1)
obj1 = StudentDetails()          
      
while(True):
    print("1.Add student")
    print("2. Display students like API:")
    print("3. Search students using roll no")
    print("4. Display Ranking")
    print("5. Exit")
    
    choice = int(input("Enter your choice"))
    
    if choice == 1:
        name = input("Enter your name:")
        rollno = int(input("Enter your rollno:"))
        admin = int(input("Enter your admission no:"))
        english = int(input ("Enter English marks:"))
        hindi = int(input("Enter hindi marks:"))
        maths = int(input("Enter maths marks:"))
        science = int(input("Enter science marks:"))
        social = int(input("Enter social marks:"))

        obj1.addStudentDetail(name,rollno,admin,english,hindi,maths,science,social)
    if choice == 2:
        print(studentlist)

    if choice == 3:
        srollno = int(input("Enter the roll no to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))

    if choice == 4:
        print(sorted(studentlist,key=lambda i:i['total'],reverse=True))  

    if choice == 5:
        break      






    


    