import pymongo

# $and --> either of the condition should be satisfied 
# $or --> any one of the condition can be satisfied 

 
customer =pymongo.MongoClient("mongodb+srv://Amar_24:Amar2421@cluster0.g6gs1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DataBase = customer["DapartmentsDB"]
collection = DataBase["Student_details"]


#Simple menu-driven app for
std_DB = []

class students:
    def std_database(self, Name, rollno, adminno, department):
        self.Name=Name
        self.rollno=rollno
        self.adminno=adminno
        self.department =department
        
class Marks(students):
    def std_marks(self, TechEng, EnggChe, ComputerPro, EnggGraphics, Maths,total ):
        self.TechEng = TechEng
        self.EnggChe = EnggChe
        self.ComputerPro = ComputerPro
        self.EnggGraphics = EnggGraphics
        self.Maths = Maths
        self.total = total
        
        Student_details ={"Student Name":Name, 
                          "Roll_No":rollno, 
                          "Admission_No":adminno, 
                           "Department": department, 
                          "Technical_English": TechEng,
                          "Enngineering_Chemistry": EnggChe,
                          "Computer Programming": ComputerPro,
                          "Enngineering Graphics" : EnggGraphics,
                          "Mathematics":  Maths,
                          "Total":total
                                                    
        }
        std_DB.append(Student_details)

S = Marks()

while(True):
    print("\n1. Add student Details")
    print("\n2. View all the student details")
    print("\n3. Search student Roll.No and Department")
    print("\n4. Update student details")
    print("\n5. Average Mark of Students")
    print("\n6. Exit ")

    Select = int(input("Enter your selection: "))

    if Select ==1:
        print("\n")
        print("Add student details to the database")
        Name = input("Enter student name: ")
        rollno = int(input("Enter student RollNo: "))
        adminno = int(input("Enter student Admission No: "))
        department = input("Enter Department Name: ")
        TechEng = int(input("Enter the mark in Technical English : "))
        EnggChe = int(input("Enter the mark in Engineering Chemistry: "))
        ComputerPro = int(input("Enter the mark in Computer Programming: "))
        EnggGraphics = int(input("Enter the mark in Engineering Graphics:")) 
        Maths = int(input("Enter the mark in Engineering Mathematics: "))
        total =TechEng+EnggChe+ComputerPro+EnggGraphics+Maths

        S.std_marks(TechEng, EnggChe, ComputerPro, EnggGraphics, Maths,total)

        # Student_details ={"Student Name":Name, 
        #                   "Roll_No":rollno, 
        #                   "Admission_No":adminno, 
        #                    "Department": department, 
        #                   "Technical_English": TechEng,
        #                   "Enngineering_Chemistry": EnggChe,
        #                   "Computer Programming": ComputerPro,
        #                   "Enngineering Graphics" : EnggGraphics,
        #                   "Mathematics":  Maths,
        #                   "Total":total
                                                    
        # }
         
        #std_DB.append(Student_details)
        marks =collection.insert_many(std_DB)


    if Select ==2:
        marks = collection.find({},{"_id":0})
        for i in marks:
            print(i)

    if Select==3:
        print("\n")
        print("\n3. Search student details by using Roll.No and Department")
        Dept = input("Enter department name to search: ")
        roll = int(input("Enter Roll No to search: "))
        marks = collection.find({"Department":Dept, "Roll_No":roll},{"_id":0})

        list1 =[]
        for i in marks:
            list1.append(i)
            print(list1)

    if Select ==4:
        print("Update Student Details: ")
        d =input("Enter department name to search: ")
        r =int(input("Enter Roll.No to search: "))
        Eng = int(input("Enter the mark in Technical English to update"))
        EChe = int(input("Enter the mark in Engineering Chemistry to update: "))
        ComPro = int(input("Enter the mark in Computer Programming to update: "))
        EngGra = int(input("Enter the mark in Engineering Graphics to update:")) 
        Mat = int(input("Enter the mark in Engineering Mathematics to update: "))

        marks = collection.update_many({"Department":d,"Roll_No":r},{"$set":{"Technical_English":Eng, "Enngineering_Chemistry": EChe,"Computer Programming": ComPro,"Enngineering Graphics" : EngGra,"Mathematics":  Mat}})

    if Select==5:
        d1 =input("Enter department name to search: ")
        result =collection.aggregate([{"$match":{"Department":d1}},{"$group": {"_id":"null", "TechnicalEnglish_Average":{"$avg":"$Technical_English"}}}])

        for x in result:
            print(x)

    if Select ==6:
        print("Exit")
        break 

