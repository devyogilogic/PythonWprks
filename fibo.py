n=  int (input("How many numbers in fibonaacii series :"))
first,second,third=0,1,0
print(first,second,end="",sep="")
for i in range(n+1):
    third =first + second
    print(third , end= "")
    first,second=second,third
