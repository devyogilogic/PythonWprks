num=int(input("Enter the number : "))


temp= num
rem=newnum=0

while num:
    rem = num %10
    newnum+= rem**3
    num=int(num/10)
if(temp==newnum):
    print(" Ya this Armstrong ")
else:
    print(" this is not Armstrong :(")

