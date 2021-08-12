import logging
import pymongo
client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydata = client["StudnetsMarksDB"]
Collection_name = mydata["StudnetsMarks"]
logging.basicConfig(filename = "StudentsDB.log" ,level=logging.DEBUG)
std_details = [ ]
class Student:
    def add_details(self,Name,Rollno,Class,Tam,Eng,Maths,Science,Social,Total):
        self.Name = Name
        self.Rollno = Rollno
        self.Class = Class
        self.Tam = Tam
        self.Eng = Eng
        self.Maths = Maths
        self.Science = Science
        self.Social = Social
        self.Total = Total
        details= {"Name":Name,"Rollno":Rollno,"Class":Class,"Tamil Mark":Tam,"English Mark":Eng,"Maths Mark":Maths,"Science Mark":Science,
        "Social Mark":Social,"Total":Total}
        std_details.append(details)

SD = Student()
while (True):
    print("1.ADD DETAILS")
    print("2.VIEW ALL STUDENTS WITH MARKS")
    print("3.SEARCH STUDENTS WITH CLASS AND ROLLNO")
    print("4.UPDATE STUDENTS DATA")
    print("5.FIND AVERAGE MARK OF STUDENTS IN ENG")
    print("6.EXIT")
    choice = int(input("Enter your choice: "))
    try:
        if choice == 1:
            Name = input("Enter student Name: ")
            Rollno = int(input("Enter student roll no: "))
            Class = int(input("Enter student Class (STD): "))
            Tam = int(input("Enter student Tamil mark: "))
            Eng = int(input("Enter student English mark: "))
            Maths = int(input("Enter student Maths mark: "))
            Science= int(input("Enter student Science mark: "))
            Social= int(input("Enter student Social mark: "))
            Total = Tam+Eng+Maths+Science+Social
            SD.add_details(Name,Rollno,Class,Tam,Eng,Maths,Science,Social,Total)
            result = Collection_name.insert_many(std_details)
            #Rollno = int(input("Enter student roll no: "))
    
        if choice == 2:
            result = Collection_name.find({ },{"_id":0})
            for i in result:
                print(i)
    
        if choice == 3:
            print("Search student details using class and roll no")
            C = int(input("Enter class to search: "))
            r = int(input("Enter roll no to search: "))
            result = Collection_name.find({"Class":C,"Rollno":r},{"_id":0})
            new_list = []
            for i in result:
                new_list.append(i)
                print(new_list)
        if choice == 4:
            print("Update student marks")
            C = int(input("Enter class to search: "))
            r = int(input("Enter roll no to search: "))
            t = int(input("Enter tamil mark: "))
            e = int(input("Enter English mark: "))
            m = int(input("Enter Maths mark: "))
            Sc = int(input("Enter science mark: "))
            So = int(input("Enter social mark: "))
            result = Collection_name.update_many({"Class":C,"Rollno":r},{"$set":{"Tamil Mark":t,"English Mark":e,
            "Maths Mark":m,"Science Mark":Sc,"Social Mark":So}})
        if choice == 5:
            C = int(input("Enter class to search: "))
            #result = Collection_name.aggregate([{"$project":{"Class":C,"engavg":{"$avg":"$English Mark"}}}])
            #result = Collection_name.aggregate([{"Class":C},{"$project":{"Engavg":{"$avg":"$English Mark"}}}])
            #result = Collection_name.aggregate([{"$group":{"_id":"null","EnglishAverage":{"$avg":"$English Mark"}}}])
            result = Collection_name.aggregate([{"$match":{"Class":C}},{"$group":{"_id":"null","EnglishAverage":{"$avg":"$English Mark"}}}])
            #avg = [ ]
            for i in result:
                print(i)
                # avg.append(i)
                # print(i)
    
        if choice == 6:
            print("Exit")
            break
    except:
        print("Something went wrong")
    finally:
        logging.info("Program run successfully")




