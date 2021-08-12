import csv
import re
import json
import pymongo
import logging
studentlist=[]
studentlist2=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017")
    mydatabase=client["Highschooldb"]
    collection_name=mydatabase['students']
    class StudentDetails:
        def init(self,name,rollno,class1,english,maths,science,social):
            self.name=name
            self.rollno=rollno
            self.class1=class1
            self.english=english
            self.maths=maths
            self.science=science
            self.social=social
        def addstudentdetail(self,name,rollno,class1,english,maths,science,social):
            totalmarks=english+maths+science+social
            dict1={"total":totalmarks,"name":name,"rollno":rollno,"class1":class1,"english":english,"maths":maths,"science":science,"social":social,"status":0} 
            return dict1
    def validate(name): 
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",name) 
        if valname:
            return True
        else:
            return False


    obj=StudentDetails()
    if(__name__=="__main__"):     
        while True:
            print("1.add student")
            print("2.view students details with marks")
            print("3.search based on class and rollno")
            print("4.update student marks based on class and rollno")
            print("5.find the average marks of english based on class")
            print("6. delete student based on class and rollno")
            print("7.exit") 
            choice=int(input("Enter your choice : "))
            if choice==1:
                name=input("Enter the name : ")
                rollno=int(input("Enter the roll no : "))
                class1=int(input("Enter class: "))
                english=int(input("Enter the marks of English : "))
                
                maths=int(input("Enter the marks of maths : "))
                science=int(input("Enter the marks of Science : "))
                social=int(input("Enter the marks of Social : "))
            

            
                a=validate(name)
                if a:
                    data=obj.addstudentdetail(name,rollno,class1,english,maths,science,social)
                    studentlist.append(data)
                    result=collection_name.insert_many(studentlist)
                    print(result.inserted_ids) 
                else:
                    logging.error("invalid data enter a valid data")
            
            if choice==2:
                result=collection_name.find({"status":0},{"_id":0})
                for i in result:
                
                    studentlist2.append(i)
                print(studentlist2)
                studentlist2.clear()

            if choice==3:
                Rollno=int(input("Enter the rollno to search:"))
                class1=int(input("Enter the class to search:"))
                
                result=collection_name.find({"$and":[{"rollno":Rollno,"class1":class1,"status":0}]},{"_id":0})
                for i in result:
                    print(i)
                
            if choice==4:
                Rollno=int(input("Enter the rollno to update"))
                class1=int(input("Enter the class to update"))
                english1=int(input("Enter the improved marks of English : "))
                maths1=int(input("Enter the improved marks of maths : "))
                science1=int(input("Enter the improved marks of Science : "))
                social1=int(input("Enter the improved marks of Social : "))
                result=collection_name.update_one({"$and":[{"rollno":Rollno,"class1":class1,"status":0}]},{"$set":{"english":english1,"maths":maths1,"science":science1,"social":social1}})
                print(result.modified_count)
            if choice==5:
                class1=int(input("Enter the class:"))
                result=collection_name.aggregate([{"$match":{"class1":class1,"status":0}},{"$group":{"_id":"$class1","Avg_eng_marks":{"$avg":"$english"}}}])
                for i in result:
                    print(i)
            if choice==6:
                rollno1=int(input("Enter student roolno to delete:"))
                class1=int(input("Enter the class to delete:"))
                result=collection_name.update_one({"$and":[{"rollno":rollno1,"class1":class1}]},{"$set":{"status":1}})
                print(result.modified_count)
            if choice==7:
                break
except:
    logging.error("unable to process!! sorry")
finally:
    print("thank you")