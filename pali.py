num=int(input("Enter the number : "))


temp= num
rem=newnum=0

while num:
    rem = num %10
    newnum= newnum*10+rem
    num=int(num/10)
if(temp==newnum):
    print(" Ya this palidrome ")
else:
    print(" this is not palidrome :(")

