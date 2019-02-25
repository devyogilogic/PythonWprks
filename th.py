from time import  sleep
from threading import Thread
class Task1(Thread):
    def run(self):
        for i in range(100000000000000000000000000000):
            """sleep(1)"""

            print(i)


class Task2 (Thread):
     def run(self):
         for i in range(10):

             print("hi yogesh ")


t1= Task1()
t2= Task2()
t1.setName("yogi")
t2.setName("yadav")

t1.start()


t2.start()
t1.join()
t2.join()

print("hello")

