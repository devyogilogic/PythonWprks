from numpy import *

arr1=array([

    [1,2,3],
    [4,5,6],
    [10,11,21]
])

arr2 = array([

    [7, 8, 9],
    [10, 11, 12],
    [1,2,6]
])
m1=matrix(arr1)
m2=matrix(arr2)

m3=m1+m2
print(m3)
m4=m1-m2
print(m4)
m5=m1*m2
print(m5)