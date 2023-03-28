import numpy as np
import pandas as pd
from numpy.ma import count
import array as arr


from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
excel= pd.read_excel(r'E:\Python Project\Python\PycharmProject\pythonProject1\InputFiles\articles.xlsx')
f = open('articles_write.txt', 'w')
count=0
valid_urls={}
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

    inv_urls = ""
    for link in lnks:
        article_link = (link.get_attribute('href'))
        string = 'shriramfinance.in'
        # print(article_link)
        i=0

        if string not in article_link:
            if article_url not in valid_urls:
                valid_urls[article_url]=[]

            valid_urls[article_url].append(article_link)

            # b = np.array(article_link)
            inv_urls = inv_urls+article_link+"\n"
            # print(article_link)
        else:

         count=count+1

    if inv_urls != "":
        inv_urls = "Invalid URLs: \n"+inv_urls
        f.writelines(inv_urls + '\n')




print(valid_urls)







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




