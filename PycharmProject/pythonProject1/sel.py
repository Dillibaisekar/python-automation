import numbers
import time
import unittest
import body as body
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.devtools.v106 import browser
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import select

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def picker(value):
    data = driver.find_elements(By.XPATH, "//div[@class='mat-calendar-body-cell-content mat-focus-indicator']")
    for element in data:
        datas = element.text
        print(datas)
        if datas == value:
            element.click()
            break

time.sleep(2)
driver: WebDriver = webdriver.Chrome(executable_path="E:\DRIVER\chromedriver.exe")
driver.get("https://sitsfl.stfc.in/")
driver.maximize_window()
time.sleep(2)

element_to_hover_over = driver.find_element(By.XPATH,
                                            '//*[@id="body"]/app-root/app-header/header/section[2]/div/div/div[2]/p')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(5)
driver.find_element(By.ID, 'main_nav_gl').click()
time.sleep(3)
print("gold loan opened sucessfully")
driver.execute_script("window.scrollTo(0, 500)")
name = driver.find_element(By.ID, "cus_name")
name.send_keys('Vanishree')
mobile = driver.find_element(By.ID, "cus_mobile")
mobile.send_keys('9791399762')
mail = driver.find_element(By.ID, "cus_email")
mail.send_keys('vani@gmail.com')
driver.find_element(By.ID, 'pf-apply-btn').click()
time.sleep(5)
print("OTP screen opened sucessfully")
driver.find_element(By.ID, "changeMobNo").click()
mobile.clear()
mobile.send_keys('9791399723')
driver.find_element(By.ID, 'pf-apply-btn').click()
time.sleep(5)
try:
    thankyou = driver.find_element(By.XPATH, "//div[@class='thank-you']")
    if thankyou and thankyou.is_displayed():
        print("Form already submitted for this lead")
except:
    otp1 = driver.find_element(By.ID, "otpCode1")
    otp1.send_keys('1')
    otp2 = driver.find_element(By.ID, "otpCode2")
    otp2.send_keys('1')
    otp3 = driver.find_element(By.ID, "otpCode3")
    otp3.send_keys('1')
    otp4 = driver.find_element(By.ID, "otpCode4")
    otp4.send_keys('1')
    otp5 = driver.find_element(By.ID, "otpCode5")
    otp5.send_keys('1')
    otp6 = driver.find_element(By.ID, "otpCode6")
    otp6.send_keys('1')
    driver.find_element(By.ID, "otpVerifybtn").click()
    time.sleep(5)
    print("OTP done sucessfully")
    driver.find_element(By.ID, 'loan-dob').click()
    print("Date picker opened")
    # driver.find_element(By.ID,'mat-datepicker-0').click()
    # print("date picker clicked")
    # driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 500)")
    driver.find_element(By.XPATH,"//*[@id='mat-datepicker-0']/mat-calendar-header/div/div/button[1]/span[1]").click()
    print("date picker arrow clicked")
    time.sleep(5)

    # years = driver.find_elements(By.XPATH, "//div[@class='mat-calendar-body-cell-content mat-focus-indicator']")//*[@id="loan-dob"]
    # for yearelement in years:
    #     year = yearelement.text
    #     print(year)
    #     if year == '1999':
    #         yearelement.click()
    #         break
    picker('1999')
    time.sleep(5)

    picker('MAY')
    picker('21')

    # months=driver.find_elements(By.XPATH,"//div[@class='mat-calendar-body-cell-content mat-focus-indicator']")
    # for monthelement in months:
    #     month=monthelement.text
    #     print(month)
    #     if month=='MAY':
    #         monthelement.click()
    #         break

    # dates = driver.find_elements(By.XPATH, "//div[text()=' 21 ']")
    # for date in dates:
    #     element = date.text
    #     print(element)
    #     if element == '21':
    #         date.click()
    #         break
    time.sleep(2)
    pan = driver.find_element(By.ID, 'cus_pan')
    pan.send_keys('cmmpd4348g')
    loan_amt = driver.find_element(By.ID, 'cus_loanAmount')
    loan_amt.send_keys('50000')
    pincode = driver.find_element(By.ID, 'cus_pincode2')
    pincode.send_keys('600026')
    female = driver.find_element(By.XPATH, '//*[@id="stage-two"]/form/div/div[8]/div[2]/label')
    female.click()
    # genders=driver.find_element(By.XPATH,"//input[@class='myradio__input ng-valid ng-dirty ng-touched']")
    # for genderelement in genders:
    #     gender=genderelement.text
    #     if gender=="Female":
    #         genderelement.click()
    #         break
    print("Gender clicked")
    single = driver.find_element(By.XPATH, '//*[@id="stage-two"]/form/div/div[9]/div[2]/label')
    single.click()
    # marital=driver.find_element(By.XPATH,"//input[@class='myradio__input ng-untouched ng-pristine ng-valid']")
    # for maritalelement in marital:
    #     if marital=="Single":
    #         maritalelement.click()
    #         break
    print("Marital status clicked")
    apply_now = driver.find_element(By.ID, 'pf-apply-btn1')
    if apply_now.is_enabled():
        print("Apply now is enabed")
    else:
        print("Apply now is not enabled")
    apply_now.click()
    time.sleep(10)
    thankyou = driver.find_element(By.XPATH, '//*[@id="feature-products"]/div/div')
    if thankyou.is_displayed():
        print("Form Submitted Sucessfully")
    else:
        print("Form not submitted")
    # if __name__ == "__main__":
    #     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\Reports'))
