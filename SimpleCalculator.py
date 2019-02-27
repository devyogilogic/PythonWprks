class Calculator :
    num1, num2=0,0

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def ad(self):
        num3=self.num1+self.num2
        print(num3)
    def sb(self,num1,num2):
        num3=num1-num2
        print(num3)
    def multiply(self):
        num3=self.num1*self.num2
        print(num3)
    def div(self):
        num3=self.num1/self.num2
        print(num3)

c1=Calculator(2,3)
Calculator.ad(c1)
Calculator.div(c1)
Calculator.mul(c1)
Calculator.div(c1)

