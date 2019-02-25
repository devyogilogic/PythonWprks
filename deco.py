def getX(x):
   return  x+20



def processx(func):
   def innerProcess(a):
      b=func(a)
      return  b/2
   return innerProcess


@processx
def fu(a):
   return  a+20

a=fu(10)
print(a)