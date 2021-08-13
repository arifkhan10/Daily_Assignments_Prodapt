import pymongo
import logging
import re
import valmodule
try:   
    
    
    client=pymongo.MongoClient("mongodb://localhost:27017/StudentDb")
    mydatabase=client['StudentDb']
    collection_name=mydatabase['students']

    studlist=[]
    studentlist=[]  

    class Student:
        def addstudentdetail(self,name,roll,sclass,eng,maths,sci,soc):   
            totalmarks=int(eng)+int(maths)+int(sci)+int(soc)
            total=str(totalmarks)
            dict1={"name":name,"roll":roll,"sclass":sclass,"eng":eng,"maths":maths,"sci":sci,"soc":soc,"total":total}
            studentlist.append(dict1)
            r=collection_name.insert_one(dict1)



    obj=Student()
    if(__name__=='__main__'):
        while(1):
            print("1. add student")
            print("2. view student")
            print("3. search student with class and rollno")
            print("4. update student data and marks")
            print("5. find avg mark")
            print("6. delete based on rolno and class")
            print("7. exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                name=input("enter the name: ")
                roll=input("enter the rollno: ")
                sclass=input("Enter the class :")
                eng=input("Enter the eng : ")
                maths=input("Enter the maths : ")
                sci=input("Enter the sci : ")
                soc=input("Enter the soc: ")
                x = (valmodule.validate(name,roll))
                if x:
                    obj.addstudentdetail(name,roll,sclass,eng,maths,sci,soc)
                else:
                    logging.error("please enter valid data")



            if choice==2:
                r=collection_name.find()
                for i in r:
                    studlist.append(i)
                print(studlist)
                studlist.clear()
                
            if choice==3:
                r=input("enter rollno:")
                c=input("enter class")
                r=collection_name.find({"$and":[{"roll":r},{"sclass":c}]})
                for i in r:
                    print(i)

            if choice==4:
                
                r=input("enter the rollno:")
                c=input("enter the class:")
                n=input("enter name:")
                r=collection_name.update_many({"roll":r,"sclass":c},{"$set":{"name":n}})
                print("updated")

            if choice==5:
                
                r=collection_name.aggregate([{"$group":{"_id":"$sclass","average":{"$avg":"eng"}}}])
                for i in r:
                    print(i)
                
            if choice==6:
                rol=input("enter rollno to delete:")
                clas=input("enter class to delete:")
                results=collection_name.delete_many({"roll":rol,"sclass":clas})
                print("deleted")

            if choice==7:  
                break

except:
    logging.error("something went wrong")