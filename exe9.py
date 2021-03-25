from threading import *
class ex:

    def myfunc(self): #self necessary as first parameter in a class func
        for x in range(7):
            print("Child")
myobj=ex()
thread1=Thread(target=myobj.myfunc)
thread1.start()
thread1.join()
print("done")
