n=int(input("Enter the number :"))
flag=0
for i in range(2,n//2):
    if n%i==0:
        flag=1

if flag:
    print(" Not Prime ")
else :
    print(" prime ")