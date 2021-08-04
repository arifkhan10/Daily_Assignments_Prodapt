import timeit
#x=print("Hello")
# print(timeit.timeit(stmt="a=20; b=10; c=a-b"))

# mycode='''
# a=15
# if(a<16):
#     pass'''
# print(timeit.timeit(stmt=mycode))

# def printnum():
#     for n in range(1000):
#         pass
# def printwhile():
#     n=0
#     while(n<=1000):
#         n=n+1
#         pass

mylist=[23,56,3,4,7,8,63,45,9,11,23,45,5]
def f1():
    filter(9,mylist)
def f2():
    for i in mylist:
        if (i==9):
            pass
print(timeit.timeit(f1,number=10000))
print(timeit.timeit(f2,number=10000))