import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

sauce=requests.get("http://www.mfd.gov.np/").content
soup=BeautifulSoup(sauce,"html.parser")

#creating dictionary
weather={}
weathersallaround=[]
table=soup.find("table",class_="table")
trs=table.find_all("tr")
tabledatas=[]

heads=['Place','Maximum Temperature(°C)','Minimum Temperature(°C)','Rain Fall(mm)']
stations=[]
maxtemps=[]
mintemps=[]
rainfalls=[]
i=0
for tr in trs:
    for td in tr.find_all("td"):
        if (i%4==0 and len(td.string)!=0 and len(td.string)<20):
            stations.append(td.string)
        if (i%4==1 and len(td.string)!=0 and len(td.string)<20):
            maxtemps.append(td.string+"°C")
        if (i%4==2 and len(td.string)!=0 and len(td.string)<20):
            mintemps.append(td.string+"°C")
        if (i%4==3 and len(td.string)!=0 and len(td.string)<20):
            rainfalls.append(td.string)
        i+=1
    i=0



weatherinnepal=pd.DataFrame({
    heads[0]:stations,
    heads[1]:maxtemps,
    heads[2]:mintemps,
    heads[3]:rainfalls
})

weatherinnepal.to_csv("weatherinnepal.csv")
