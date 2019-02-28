import urllib

from  bs4 import  BeautifulSoup as soup
import  tkinter as tk
from urllib.request import urlopen as uReq
import pandas as pd
import  tkinter.messagebox as mb
import numpy as num
window=tk.Tk()
u=tk.StringVar()
li=[]
do=[]
def scrap(url,element="a"):
        try:
            filename=str(url)
            filename=filename.split(".")[1]
            print(filename)
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
                i+=""
                ln.append("https://"+i)
            dataframe = pd.DataFrame({"x": [ln]})

            writer = pd.ExcelWriter(filename+".xlsx", engine="xlsxwriter")
            dataframe.to_excel(writer, "Sheet1")
            writer.save()
        except urllib.error.HTTPError :
            mb.showerror("$03","HTTP Error 403: Forbidden")
            u.set("")
        except Exception:
            mb.showerror("oops", "Something went wrong")
            u.set("")




def genrateslx():



    print(li)




tk.Label(window,text="Enter your url here :").grid(row=0,column=4)
tk.Entry(window,textvariable=u,bd=5).grid(row=0,column=5)
tk.Button(window,text="Scrap",command=lambda :scrap(url=u.get())).grid(row=2,column=5)
window.mainloop()



