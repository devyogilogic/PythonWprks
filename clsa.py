class PyChram :
    @staticmethod
    def e():
        print("go")
class Student:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile

    def code(self,ide):
        ide.e();

i=PyChram()
s1=Student("Yogesh","9166371779")
s1.code(i)