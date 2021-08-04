import pytz
import re
import datetime

students=[]
class Std_Details:
    def AddStudents(self,name,rollno,adminno,):
        self.name =name
        self.rollno =rollno
        self.adminno = adminno
        return
    def val(self,val1):
        self.val1=val1(re.search("[A-Z]{1}[^A-Z]{0,25}$",name))
        return

class Marks:
    def std_marks(self,tamil,english,maths,science,social,total):
        self.tamil = tamil
        self.english = english
        self.maths = maths
        self.science = science
        self.social = social
        self.total = total
        #total = tamil+english+maths+science+social
        return
    # def timeDate(time_zone,td):
    #     time_zone=pytz.timezone("Asia/kolkata")
    #     td=datetime.now(time_zone.strftime("%H-%M-%S-%d-%h-%Y"))
    #     return td
MarksObj =Marks()
ObjStd =Std_Details()

while(True):
    print("1.ADD STUDENT DETAILS")
    print("2.DISPLAY ALL THE STUDENT DETAILS")
    print("3.SEARCH STUDENT DETAILS")
    print("4.PRINT ALL THE STUDENTS BASED ON RANKING")
    print("5.EXIT")
    choice = int(input("Enter your choice: "))

    if choice ==1:
        print("Add product details have selected")
        name= input("Enter student name: ")
        rollno= int(input("Enter student RollNo: "))
        adminno= int(input("Enter student Admission No: "))
        tamil = int(input("Tamil mark: "))
        english = int(input("English mark: "))
        maths   = int(input("Maths mark: "))
        science= int(input("Science mark: "))
        social = int(input("Social mark: "))
        total = tamil+english+maths+science+social

        # time_date=MarksObj.timeDate("td")

        Student_details={"Student Name":name, "Roll_No":rollno, "Admission_No":adminno, "Tamil_Mark":tamil, "English_Mark":english, "Maths_Mark":maths, "Science_Marks":science, "Social_Marks":social, "Total_Marks":total}
        students.append(Student_details)
    if choice ==2:
        print("List of all the students")
        print(students)
    if choice ==3:
        print("Search student by using Roll No")
        r_no=int(input("Enter a Roll No to search"))
        print(list(filter(lambda i:i["Roll_No"]==r_no,students)))
    if choice ==4:
        print("All the students based on ranking")
        print(sorted(students,key=lambda i:i ['Total_Marks'], reverse=True))
        
    if choice ==5:
        break 


       


