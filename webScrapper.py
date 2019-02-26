from  bs4 import  BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="http://www.maism.org/alumni.php"
uClient=uReq(my_url)
pagereader=uClient.read()
uClient.close()
page_soup=soup(pagereader,"html.parser")

paratag=page_soup.find("p")

paratag=str(paratag)
paratag=paratag.replace("<p>","")
paratag=paratag.replace("</p>","")
print(paratag)
filename="hii.txt"
f= open(filename,"w")
f.write(paratag)