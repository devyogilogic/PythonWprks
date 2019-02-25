
def primelist():
    num=flag=0

    for num  in range(2,101):
        flag=0
        for table in range(2, num):
            if(num%table==0):
                flag=1
                break

        if(flag==0):
            yield num


for i in primelist():
     print(i)