"""
import re
compile : understand the pattern
search : finding  something  into a slelected  string
findall : find all matching values

"""
import re
ob= re.compile(r'\d\d-\d"{10}')
result=ob.search(" hello 91-9166371779")
#print(result.group())
link="adhdf,fflgcgjlgjcfg;fkgmc,www.google.com,fjdslgdrgjrdlogdjgoierg,www.yahoo.com"
r1=re.findall(r'[\w\.]+[\w\.]+com',link)
for i in r1:
    print(i)
               
