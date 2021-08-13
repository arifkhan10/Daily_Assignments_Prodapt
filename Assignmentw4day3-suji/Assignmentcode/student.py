import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
mydatabase=client['ExamDb']    #database
collection_name=mydatabase['studentsmarks'] 
studentlist=[]

fetchlist=[]
class StudentDetails:
    def addstudentdetail(self,name,rollno,sclass,english,maths,social,science):
        totalmarks=english+maths+social+science
        average=totalmarks/400
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"sclass":sclass,"english":english,"maths":maths,"social":social,"science":science,"average":average}
        studentlist.append(dict1)
obj1=StudentDetails() 

while(True):
    print("\n 1.Add student:")
    print("\n 2.view all students with their total marks:")
    print("\n 3.search a student with class and rollno:")
    print("\n 4.update student data with class and rollno:")
    print("\n 5.Average marks of english subject based on class::")
    print("\n 6.Delete a student based on rollno and class")
    print("\n 7.exit")
    choice=int(input("enter your choice:"))

    if choice==1:
        name=input("enter your name:")
        rollno=int(input("enter your rollno:"))
        sclass=input("enter class:")
        english=int(input("enter english marks:"))
        maths=int(input("enter maths marks:"))
        social=int(input("enter social marks:"))
        science=int(input("enter science marks:"))
        obj1.addstudentdetail(name,rollno,sclass,english,maths,social,science)
        collection_name.insert_many(studentlist)
        studentlist.clear()

    if choice==2:
        result=collection_name.find()
        for i in result:
          fetchlist.append(i)
        print(fetchlist)
          
   
    if choice==3:
        rollno=int(input("\n enter the rollno to search:"))
        sclass=int(input("\n enter class to search:"))
        result=collection_name.find({"$or":[{"rollno":rollno},{"sclass":sclass}]})
        for i in result:
            fetchlist.append(i)
        print(fetchlist)   

    if choice==4:
        rollno=int(input("\n enter the rollno to search:"))
        sclass=int(input("\n enter class to search:"))
        maths=int(input("\n enter marks to update:"))
        result=collection_name.update_one({"$and":[{"rollno":rollno},{"sclass":sclass}]},{"$set":{"maths":maths}})
        print(fetchlist)

        
    if choice==5:
        #result=collection_name.aggregate([{"$group": {"_id":"$average","no_of_students":{"$sum":1}}}])
        for i in result:
            print(i)

    if choice==6:
        rollno=int(input("\n enter the rollno to search:"))
        sclass=int(input("\n enter class to search:"))
        result=collection_name.delete_one({"$and":[{"rollno":rollno},{"sclass":sclass}]})
        print(fetchlist)

    if choice==7:
        break