def GenrateArm(start, end):
    for num in range(start,end+1):
      temp=num
      sum=0
      while temp:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10

      if sum == num:
        print (num)

GenrateArm(1,9999)
