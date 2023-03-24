


import pandas as pd
from numpy.ma import count

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
excel= pd.read_excel(r'E:\Python Project\Python\PycharmProject\pythonProject1\InputFiles\articles.xlsx')
f = open('articles_write', 'w')
count=0
for ind in excel.index:
    article_url= excel['URLs'][ind]
    driver.get(article_url)
    f.writelines('Entered URL is :\n')
    f.writelines( article_url+ '\n')
    print('Entered article URL is : ',article_url)
    lnks = driver.find_elements(By.TAG_NAME, 'a')

    if lnks == '':
        print("This link does not contain any links")
        continue

    for link in lnks:
        article_link = (link.get_attribute('href'))
        string = 'shriramfinance.in'
        # print(article_link)


        if string not in article_link:

            f.writelines(article_link + '\n')
            print(article_link)
        count=count+1









        # else :
        #     print('http except URLs',article_link)



# article_url = input("Enter the URL: ")
# driver=webdriver.Chrome()
# driver.get(article_url)
# print('Entered article URL is : ',article_url)
# lnks = driver.find_elements(By.TAG_NAME, 'a')
# if lnks == '':
#     print("This link does not contain any links")
#
# for link in lnks:
#     article_link = (link.get_attribute('href'))
#     string = 'https:'
#     # print(article_link)
#     if string in article_link:
#         print(article_link)




