import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

data={'data1':{'name':'Vani','Course':'B.E'},'data2':{'name':'dillibai','Course':'M.com'}}
print(data)
i='Course'
for i in data:
    print(data['data1'])
    break
#  Dynamic data
d={}
driver=webdriver.Chrome()
excel= pd.read_excel(r'E:\Python Project\Python\PycharmProject\pythonProject1\InputFiles\articles.xlsx')


for ind in excel.index:
    article_url= excel['URLs'][ind]
    driver.get(article_url)
    # print('Entered article URL is : ', article_url)
    lnks = driver.find_elements(By.TAG_NAME, 'a')
    art_urls = {'invalid_urls': {}, 'valid_urls': {}}
    if lnks == '':
        print("This link does not contain any links")
        continue

    inv_urls = ""
    for link in lnks:
        article_link = (link.get_attribute('href'))
        # print(article_link)
        string = 'shriramfinance.in'
        if string not in article_link:
            if article_url not in art_urls['invalid_urls']:
                art_urls['invalid_urls'][article_url] = []
            art_urls['invalid_urls'][article_url].append(article_link)
            continue
        if article_url not in art_urls['valid_urls']:
            art_urls['valid_urls'][article_url] = []
        art_urls['valid_urls'][article_url].append(article_link)

print(art_urls['invalid_urls'])
print(art_urls['valid_urls'])









