from gettext import find

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
    print('done')

    for trow in interest_rate:
        data = trow.find_all("td")
        # print(trow)
        period=data[0].text
        rate = data[1].text
        maturityvalue = data[2].text
        print(period)
        print(rate)
        print(maturityvalue)
        print(period,rate,maturityvalue)
        # break
        sheet.append([period,rate,maturityvalue])

except Expection as e:
    print("exception")

excel.save("RD_InterestRate.xlsx")








