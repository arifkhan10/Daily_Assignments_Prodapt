import threading ,time,logging
first=2
end=500
def find_Prime():
    for num in range(first, end + 1):
   
     if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
     else:
        print(num)
   
def find_Palindrome():
    for num in range(10, 500 + 1):
        temp = num
        reverse = 0
    
        while(temp > 0):
            Rem = temp % 10
            reverse = (reverse * 10) + Rem
            temp = temp //10

        if(num == reverse):
            print(num)
            
if(__name__=="__main__"):
       

    p1=threading.Thread(target=find_Prime)
    p2=threading.Thread(target=find_Palindrome)
    p1.start()
    p1.join()
    print("******")
    p2.start()
    p2.join()
    print("$$$$$$$$$")
    logging.error("something went wrong")