from  bs4 import  BeautifulSoup as soup
import  tkinter as tk
from urllib.request import urlopen as uReq
import pandas as pd
import numpy as num
window=tk.Tk()
u=tk.StringVar()
li=[]
do=[]
def scrap(url,element="a"):
    my_url = url
    uClient = uReq(my_url)
    pagereader = uClient.read()
    uClient.close()
    page_soup = soup(pagereader, "html.parser")
    str1=","
    for p in page_soup.select(element):

        str1=str1+str(p.get("href"))
    li=str1.split("https://")
    print(li)
    ln=[]
    for i in li:
        ln.append("https://"+i)
    dataframe = pd.DataFrame({"x": [ln]})

    writer = pd.ExcelWriter("go3.xlsx", engine="xlsxwriter")
    dataframe.to_excel(writer, "Sheet1")
    writer.save()


def genrateslx():



    print(li)




tk.Label(window,text="Enter your url here :").grid(row=0,column=4)
tk.Entry(window,textvariable=u,bd=5).grid(row=0,column=5)
tk.Button(window,text="Scrap",command=lambda :scrap(url=u.get())).grid(row=2,column=5)
window.mainloop()



