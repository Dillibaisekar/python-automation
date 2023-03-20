
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
excel= pd.read_excel(r'E:\Python Project\Python\PycharmProject\pythonProject1\InputFiles\articles.xlsx')
for ind in excel.index:
    article_url= excel['URLs'][ind]
    driver.get(article_url)
    print('Entered article URL is : ',article_url)
    lnks = driver.find_elements(By.TAG_NAME, 'a')
    if lnks == '':
        print("This link does not contain any links")
        continue

    for link in lnks:
        article_link = (link.get_attribute('href'))
        string = 'https:'
        # print(article_link)
        if string in article_link:
            print(article_link)



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




