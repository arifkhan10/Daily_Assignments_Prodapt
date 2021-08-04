import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='demo1.log',level=logging.DEBUG)

try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    div=a/b                                    
    #print(div)
    logging.info(div)                                   
except ZeroDivisionError:
    logging.error("OOPS!,division by zero is not allowed")





logging.error("an unkown error happened")
logging.warning("excepted value is an integer")
logging.critical("critical error happened")
logging.info("normal message")
logging.debug("for developers")