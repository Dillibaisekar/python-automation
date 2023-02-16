import os
from sys import path

import pandas as pd

from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Interest Rate"
sheet.append(['Period','Interest Rate','Maturity Value'])


class Expection:
    pass


try:
    response=requests.get("https://sitsfl.stfc.in/recurring-deposit-interest-and-charges")
    soup= BeautifulSoup(response.text,'html.parser')
    # print(soup)
    interest_rate=soup.find_all("tbody", class_="t_body")[0].find_all("tr")
    # print(interest_rate)


    for trow in interest_rate:
        data = trow.find_all("td")
        # print(trow)
        period=data[0].text
        rate = data[1].text
        maturityvalue = data[2].text
        # print(period)
        # print(rate)
        # print(maturityvalue)
        # print(period,rate,maturityvalue)
        # break
        sheet.append([period,rate,maturityvalue])

except Expection as e:
    print("exception")

excel.save("RD_InterestRate.xlsx")
cwdpath=os.getcwd()
# print(cwdpath)
# print(os.path.join(cwdpath,"InputFiles","InterestRate.xlsx"))

df2=pd.read_excel(os.path.join(cwdpath,"InputFiles","InterestRate.xlsx"))
print()
print("New Interest Rate Data:")
print(df2)
print()
df1=pd.read_excel(os.path.join(cwdpath,"RD_InterestRate.xlsx"))
print("Existing Interest in the Website:")
print(df1)

df1.equals(df2)
comparison_values = df1.values == df2.values
print(comparison_values)










