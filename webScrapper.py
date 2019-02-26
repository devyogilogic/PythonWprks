from  bs4 import  BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
def readexcelfile():
    file = open("mydata.xlsx", "rb")
    dataframe_read = pd.read_excel(file)
    print(dataframe_read)

my_url="http://www.maism.org/alumni.php"
uClient=uReq(my_url)
pagereader=uClient.read()
uClient.close()
page_soup=soup(pagereader,"html.parser")

paratag=page_soup.find("p")

paratag=str(paratag)
paratag=paratag.replace("<p>","")
paratag=paratag.replace("</p>","")

a=paratag
dataframe=pd.DataFrame({"Data":[a]})
print(dataframe)
writer= pd.ExcelWriter("mydata.xlsx",engine="xlsxwriter")
dataframe.to_excel(writer,"Sheet1")
writer.save()
