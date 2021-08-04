studentlist=[]
class Studentdetail:

    def addstudentdetail(self,name,rollno,admin,eng,hindi,math,sci,soc):
        totalmarks=eng+hindi+math+sci+soc
        dict1={"totalmarks":totalmarks,"name":name,"rollno":rollno,"admin":admin,"eng":eng,"hindi":hindi,"math":math,"sci":sci,"soc":soc}
        studentlist.append(dict1)

obj1=Studentdetail()
while(True):
    print("1. add student")
    print("2. search student using rollno")
    print("3. display student like api")
    print("4. ranking")
    print("5. exit")
    choice=int(input("enter ur choice:"))
    #obj1=Studentdetail()
    if choice==1:
        name=input("enter your name:")
        rollno=int(input("enter your rollno:"))
        admin=int(input("enter your admin:"))
        eng=int(input("enter your eng:"))
        hindi=int(input("enter your hindi:"))
        math=int(input("enter your math:"))
        sci=int(input("enter your sci:"))
        soc=int(input("enter your soc:"))
        obj1.addstudentdetail(name,rollno,admin,eng,hindi,math,sci,soc)
    
    if choice==2:
        print(studentlist)
    
    if choice==3:
        srollno=int(input("enter your rollno:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
    
    if choice==5:
        break

