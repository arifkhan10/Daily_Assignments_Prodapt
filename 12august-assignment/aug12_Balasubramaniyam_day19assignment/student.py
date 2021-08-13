'''1) add student(name,roll,class,english,maths,social,science,total)
2)view all students with their marks
3)search student with class and roll number
result=productcollection.aggregate([{"$group":{"_id":"$description","products":{"$sum":1}}}])
4)update student data with marks based on roll number and class
5)find average marks of english subject based on class 
6) delete the student based on roll and class '''
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydata=client["StudentsDb"]
collection_name=mydata["students1"]
class Student:
    def addstudent(self,name,roll,std,english,maths,social,science):
        total=english+maths+social+science
        dict1={"name":name,"roll":roll,"std":std,"english":english,"maths":maths,"science":science,"social":social,"total":total,"flag":1}
        collection_name.insert_one(dict1)
obj1=Student()
while(1):
    print("1) add student")
    print("2) view all students with their marks")
    print("3) search student with class and roll number")
    print("4) update student data with marks based on roll number and class")
    print("5) find average marks of english subject based on class ")
    print("6) delete the student based on roll and class")
    print("7) Ranking ")
    print("8) Exit : ")
    option=int(input("Enter the option : "))
    if option==1:
        name=input("Enter the Student name : ")
        roll=int(input("Enter your rollno : "))
        std=input("Enter the class  : ")
        english=int(input("Enter your English marks : "))
        maths=int(input("Enter your maths marks : "))
        science=int(input("Enter your Science marks: "))
        social=int(input("Enter your Social Marks : "))
        obj1.addstudent(name,roll,std,english,maths,social,science)
    if option==2:
        result=collection_name.find({"flag":1})
        for i in result:
            print(i)
    
    if option==3:
        std1=input("enter class of student:")
        roll1=int(input("Enter your rollno : "))
        result=collection_name.find({"$and":[{"std":std1},{"roll":roll1}]})
        for i in result:
            print(i)
    if option==4:
        std1=input("enter class of student:")
        roll1=int(input("Enter your rollno : "))
        english=int(input("Enter your English marks : "))
        maths=int(input("Enter your maths marks : "))
        science=int(input("Enter your Science marks: "))
        social=int(input("Enter your Social Marks : "))
        total=english+maths+social+science
        result=collection_name.update_one({"$and":[{"std":std1},{"roll":roll1}]},{"$set":{"english":english,"maths":maths,"science":science,"social":social,"total":total}})
    if option==5:
        
        result=collection_name.aggregate([{"$group" : {"_id" : None, "average" : {"$avg" : "$english"}}}])
        print(result)
        for i in result:
            print(i)
    if option==6:
        std1=input("enter class of student:")
        roll1=int(input("Enter your rollno : "))
        result=collection_name.update_many({"$and":[{"std":std1},{"roll":roll1}]},{"$set":{"flag":0}})
    
    if option==7:
        result=collection_name.aggregate([{"$sort":{'total':-1}}])
        for i in result:
            print(i)
    if option==8:
        break