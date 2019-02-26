from numpy import *
""""
#1 way array()
arr= array([1,2,3,4])
print(arr)
# 2 linespace(start,stop is included,setp is divide)
arr2= linspace(1,10,10)
print(arr2)
# 3logspace()
arr4= logspace(1,10,10)
print(arr4)
# 4arange(start,step,range)
arr3= arange(1,10,2)
print(arr3)
#5 zerors(count ,datatype)
arr4= zeros (5)
print(arr4)
#5  ones(count, datatype)
arr5= zeros(5)
print(arr5)
"""
#copy Array using Numpy
arr1= array([1,2,4,5])
arr2=arr1.copy() #it will create other refernces
print(arr1)
print(arr2)