import pandas as pd
import numpy as num
import matplotlib.pyplot as grph
def genratedatafromexcel():
    file = open("collegedata.xlsx", "rb")
    dataframe_read = pd.read_excel(file)
    plotdata=dataframe_read[['x','y']]
    plotdata=num.array(plotdata)
    #print(plotdata)
    grph.plot(plotdata)
    grph.show()


def genrategraph ():
    a=[120,15,67,89]
    b=[12,1,6,8]
    grph.plot(a,b)
    grph.show()


def readexcelfile():
    file = open("collegedata.xlsx", "rb")
    dataframe_read = pd.read_excel(file)
    print(dataframe_read)


def genrateslx():
    dataframe = pd.DataFrame({"x": [1,67,89, 89, 20,45],"y":[1,2,4, 4, 20,45]})

    writer = pd.ExcelWriter("collegedata.xlsx", engine="xlsxwriter")
    dataframe.to_excel(writer, "Sheet1")
    writer.save()
genratedatafromexcel()