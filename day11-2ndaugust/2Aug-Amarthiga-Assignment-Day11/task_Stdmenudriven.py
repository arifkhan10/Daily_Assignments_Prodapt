import re
Std_list = []
class StudentDetails:            # defining class
    #def __init__(self, name, RegNo, tamil, english, maths, science, social):
        
    def Addstd(self,name, RegNo, tamil, english, maths, science, social):
        self.Name = name
        self.regNo = RegNo 
        self.Tamil = tamil 
        self.English = english 
        self.Maths = maths
        self.Science = science 
        self.Social = social 
        totalmarks = tamil+english+maths+science+social 
        dic={"Name":name, "Reg_No":RegNo, "Tamil":tamil, "English":english, "Maths": maths, "Science": science, "Social":social, "Total_Marks":totalmarks }
        Std_list.append(dic)
Objstd = StudentDetails()             
# if we put inside while loop, it will create memory leakage problem. So put it outside the while loop is good practice.
#menu driven using while loop
while(True):
    print("1. Add Student name: ")
    print("2. Displaying students like API: ")
    print("3. Search studtents using Reg_No: ")
    print("4. Ranking: ")
    print("5. Exit ")

    choice1 = int(input("Enter your choice"))
    if choice1==1:
        name =input("Enter the stduent name: ")
        RegNo =int(input("Enter the stduent Register name: "))
        tamil =int(input("Enter the stduent Tamil marks: "))
        english =int(input("Enter the stduent English marks: "))
        maths=int(input("Enter the stduent Maths marks: "))
        science=int(input("Enter the stduent Science marks: "))
        social=int(input("Enter the stduent Social marks: "))

        name1=re.search("[A-Z]{1}[^A-Z]{0,25}$", name)

        #Objstd = StudentDetails()
        Objstd.Addstd(name, RegNo, tamil,english, maths, science, social)
    if choice1==2:
        print(Std_list)
    if choice1==3:
        RegNos=int(input("Enter the register no: "))
        print(list(filter(lambda i:i["Reg_No"]==RegNos,Std_list)))
    if choice1==4:
        print(sorted(Std_list,key=lambda i:i ['Total_Marks'], reverse=True))          #sorting methods 





