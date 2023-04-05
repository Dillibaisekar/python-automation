from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
filename = "InputFiles/articles.txt"
f_obj = open(filename, "r")
write= open(filename,"a")
for a in f_obj:
    driver.get(a)
    # pageSource = driver.find_element(By.CLASS_NAME,'//div[@class="maximumu_ten"]/tbody/tr').get_attribute("outerHTML")
    # pageSource = driver.find_element(By.XPATH,'//div[@class="maximumu_ten"]/tbody/tr')
    try:
        if driver.find_element(By.XPATH,'//div[@class="table-responsive"]') or driver.find_element(By.TAG_NAME,'table'):
            print('Entered article URL is : ',a)
            write.writelines("\n This URL contains table:"+ a)

    except:
        print(a+": This URL doesn't contains table.")
    # print(pageSource)
    # if pageSource!='':
    #     print('Entered article URL is : ', a)


