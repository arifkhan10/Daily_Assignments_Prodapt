import smtplib,re,logging,time,pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")  
mydatabase=client["student1Db"]
collection_name=mydatabase["stu"]
studentlist=[]
logging.basicConfig(filename='student.log',level=logging.DEBUG)
class StudentDetails:
    def addstudentdetial(self,name,rollno,std,english,maths,science,social):
        totalmarks=int(english)+int(maths)+int(science)+int(social)
        dict={"totalmarks":totalmarks,"name":name,"rollno":rollno,"std":std,"english":english,"maths":maths,"science":science,"social":social}
        studentlist.append(dict) 
obj=StudentDetails()  

def validate(vname,vrollno):
    name1=re.search("([a-z]+)([a-z]+)*([a-z]+)*$",vname)
    rollno1=re.search("[0-9]{0,7}$",vrollno)
    if name1 and rollno1:
        return True
    else:
        return False
try:
    if __name__== "__main__":
        while(True):
                print("1.Add Student")
                print("2.View all Students and Marks")
                print("3.Search a students with class & rollno")
                print("4.Update the student data based on rollno & std")
                print("5.Average mark of Student English based on std")
                print("6.Delete a student based on rollno & class")
                print("7.Exit")

                option=int(input("Enter your option :"))
                if option==1:
                    vname = input("Enter the name of the student: ")
                    vrollno=input("Ënter the RollNo:")
                    if validate(vname,vrollno):
                        std= input("Enter the Subject Std: ")
                        english=input("Enter the English marks subject: ")
                        maths= input("Enter the Maths marks subject: ")
                        science= input("Enter the Science marks subject: ")
                        social= input("Enter the Social marks  subject: ")
                        obj.addstudentdetial(vname,vrollno,std,english,maths,science,social)
                        collection_name.insert_many(studentlist)
                        studentlist=[]
                    else:
                        logging.error("Check your name and rollno")

                if option==2:
                        r=collection_name.find()
                        for i in r:
                            print(i)
                
                if option==3:
                    a=input("Search the student rollno: ")
                    b=input("Search the student std:")
                    r=collection_name.find({"rollno":a,"std":b})
                    for i in r:
                        print(i)
                        logging.info("Successfully!!! Search the data")

                if option==4:
                    a=input("Update the student rollno: ")
                    b=input("Update the student std:")
                    update_mark=input("Enter the Update mark:")      
                    r=collection_name.update_many({"rollno":a,"std":b},{"$set":{"totalmarks":update_mark}})
                    print(r)
                    studentlist.clear()
                    logging.info("Successfully!!! Update the data")

                if option==5:
                    r=collection_name.aggregate([{"$group" : {"_id" : None, "totalmark" : {"$avg" : "$english"}}}])
                    for i in r:
                        print(i)
                    
                if option==6:
                    a=input("Delete the student rollno: ")
                    b=input("Delete the student std:")
                    r=collection_name.delete_many({"rollno":a,"std":b})
                    print(r.deleted_count)
                    studentlist.clear()
                    logging.info("Successfully!!! Delete the data")

                if option==7:
                    break

except ValueError:
    logging.error("Please Check Value int or string")

except IndexError:
    logging.error("Please Check Your Index")

except Exception:
    logging.error("Something Went Wrong")

finally:
    print("Äll Block Completed Successfully")
