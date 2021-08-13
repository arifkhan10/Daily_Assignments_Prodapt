import re,csv,logging,pymongo
try:
    
    studentlist=[]
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['Student1Db'] #database
    collection_name=mydatabase['Student_agg']
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
            totalmarks=int(english)+int(maths)+int(science)+int(social)
            dict1={"total":totalmarks,"name":name,"rollno":rollno,"class1":class1,"english":english,"maths":maths,"science":science,"social":social,"delflag":0} 
            return dict1
    def validate(name,rollno,class1,english,maths,science,social):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
        valrollno=re.search("^[0-9]{1,2}$",rollno)
        valclass1=re.search("^[0-9]{1,2}$",class1)
        valenglish=re.search("^[0-9]{1,2}$",english)
        valmaths=re.search("^[0-9]{1,2}$",maths)
        valscience=re.search("^[0-9]{1,2}$",science)
        valsocial=re.search("^[0-9]{1,2}$",social)
        if valname and valrollno and valclass1 and valenglish and valmaths and valscience and valsocial:
            return True
        else:
            return False
    obj=StudentDetails() 
    if(__name__=="__main__"):       
        while True:
            print("1.Add student")
            print("2.View all student with marks")
            print("3.search a student with class and roll no")
            print("4.update the student data with marks based on roll no and class")
            print("5.Average marks of English subject based on class") 
            print("6.Delete  a student based on roll no and class")
            print("7.Exit")

            choice=int(input("Enter your choice : "))
            if choice==1:
            
                name=input("Enter the name : ")
                rollno=input("Enter the roll no : ")
                class1=input("Enter the class : ")
                english=input("Enter the marks of English : ")
                maths=input("Enter the marks of maths : ")
                science=input("Enter the marks of Science : ")
                social=input("Enter the marks of Social : ")
                if validate(name,rollno,class1,english,maths,science,social)==True:
                    data=obj.addstudentdetail(name,rollno,class1,english,maths,science,social)
                    studentlist.append(data)
                    result=collection_name.insert_many(studentlist)
                    print(result.inserted_ids)
                else:
                    logging.warning("Wrong details")
                    break
            if choice==3:
                sea=input("Enter the class :")
                sea1=input("Enter the roll no :")
                result= collection_name.find({"$and":[{"class1":sea},{"rollno":sea1}]},{"delflag":0}) 
                for j in result:
                    print(j)
                studentlist.clear()
            if choice==2:
                result= collection_name.find({"delflag":0},{"_id":0}) 
                for i in result:
                    print(i)
            if choice==4:
                s=input("Enter the roll no:")
                r=input("Enter the class :")
                t=input("Enter the of english subject to be updated : ")
                result= collection_name.update_one({"$and":[{"rollno":s},{"class1":r}]},{"$set":{"english":t}})
                print(result) 
            if choice ==5:
            
                result=collection_name.aggregate([{"$group":{"_id":0,"average":{"$avg":{"$toDouble":"$english"}}}}])
                for i in result:
                    print(i)
                    
            if choice==6:
                de=input("Enter the roll no :")
                de1=input("Enter the class :")
                result= collection_name.update_one({"$and":[{"rollno":de},{"class1":de1}]},{"$set":{"delflag":1}}) 
                print(result)
            if choice==7:
                break    
except:
    logging.error("Something went wrong")      
finally:
    print("THANK YOU")          