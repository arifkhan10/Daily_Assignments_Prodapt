#logging
import logging

#5 levels of logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='demo.log', level=logging.INFO)
logging.warning("Expected value is an integer")
logging.error("an unkown error happened")
logging.critical("Critical error happened")
logging.info("Normal message")
logging.debug("for developers")

#2
x=10
y=10
c=x+y
logging.info(c)

#task1
try:
    n = int(input("Enter a number: "))
    m = int(input("Enter a number: "))
    if x :
        x=m/n
        logging.info(x)
        logging.basicConfig(filename='demo1.log', level=logging.INFO)
    else:
        logging.
    
except: