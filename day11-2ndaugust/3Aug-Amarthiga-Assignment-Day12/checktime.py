import timeit
#print(timeit.timeit(stmt="a=10+19"))

#2
mycode='''
a=10; 
if(a<15):
    pass'''
#print(timeit.timeit(stmt=mycode))

#3
def printnumbers():
    for i in range(1000):
        pass

def printwhile():
    n=0
    while(n<=1000):
        n=n+1
        pass

# print(timeit.timeit(printnumbers, number=1000))
#print(timeit.timeit(printwhile, number=1000))

    
list=[23,67,849,89,90,34,23,87,46]
def f1():
    filter(46,list)

def f2():
    for i in list:
        if (i==46):
            pass 

print(timeit.timeit(f1))
print(timeit.timeit(f2))
