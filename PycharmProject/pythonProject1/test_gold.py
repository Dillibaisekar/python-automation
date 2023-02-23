import time

import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


## def test_f():
#     pass
#     a=3
#     b=5
#     c=a+b
#     if c==15 :
#         print('working')
#     else :
#         print('no')
## test_f()
# from unittest import TestCase

# class TryTesting(TestCase):
#     def test_always_passes(self):
#         self.assertTrue(True)
#
#     def test_always_fails(self):
#         self.assertTrue(False)


def picker(value):
    data = driver.find_elements(By.XPATH, "//div[@class='mat-calendar-body-cell-content mat-focus-indicator']")
    for element in data:
        datas = element.text
        print(datas)
        if datas == value:
            element.click()
            break



driver = webdriver.Chrome ("E:\DRIVER\chromedriver.exe")
# driver = webdriver.Chrome()
driver1.get("https://sitsfl.stfc.in/")
driver1.maximize_window()
time.sleep(2)

element_to_hover_over = driver1.find_element(By.XPATH,
                                             '//*[@id="body"]/app-root/app-header/header/section[2]/div/div/div[2]/p')
hover = ActionChains(driver1).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(5)
print("hover done")
driver1.find_element(By.ID, 'main_nav_gl').click()
time.sleep(3)
print("gold loan opened sucessfully")
driver1.execute_script("window.scrollTo(0, 500)")


def test_lead():
    name = driver1.find_element(By.ID, "cus_name")
    name.send_keys('Vanishree')
    mobile = driver1.find_element(By.ID, "cus_mobile")
    mobile.send_keys('9791399762')
    mail = driver1.find_element(By.ID, "cus_email")
    mail.send_keys('vani@gmail.com')
    driver1.find_element(By.ID, 'pf-apply-btn').click()
    time.sleep(5)
    print("OTP screen opened sucessfully")
    driver1.find_element(By.ID, "changeMobNo").click()
    mobile.clear()
    mobile.send_keys('9791399723')
    driver1.find_element(By.ID, 'pf-apply-btn').click()
    time.sleep(5)

    thankyou = driver1.find_element(By.XPATH, "//div[@class='thank-you']")
    if thankyou and thankyou.is_displayed():
        print("Form already submitted for this lead")
        assert (True)


def test_nolead():
    otp1 = driver1.find_element(By.ID, "otpCode1")
    otp1.send_keys('1')
    otp2 = driver1.find_element(By.ID, "otpCode2")
    otp2.send_keys('1')
    otp3 = driver1.find_element(By.ID, "otpCode3")
    otp3.send_keys('1')
    otp4 = driver1.find_element(By.ID, "otpCode4")
    otp4.send_keys('1')
    otp5 = driver1.find_element(By.ID, "otpCode5")
    otp5.send_keys('1')
    otp6 = driver1.find_element(By.ID, "otpCode6")
    otp6.send_keys('1')
    driver1.find_element(By.ID, "otpVerifybtn").click()
    time.sleep(5)
    print("OTP done sucessfully")
    driver1.find_element(By.ID, 'loan-dob').click()
    print("Date picker opened")
    time.sleep(2)
    driver1.execute_script("window.scrollTo(0, 500)")
    driver1.find_element(By.XPATH, '//*[@id="mat-datepicker-0"]/mat-calendar-header/div/div/button[1]/span[1]').click()
    print("date picker arrow clicked")
    time.sleep(5)
    picker('1999')
    time.sleep(5)

    picker('MAY')
    picker('21')
    time.sleep(2)
    pan = driver1.find_element(By.ID, 'cus_pan')
    pan.send_keys('cmmpd4348g')
    loan_amt = driver1.find_element(By.ID, 'cus_loanAmount')
    loan_amt.send_keys('50000')
    pincode = driver1.find_element(By.ID, 'cus_pincode2')
    pincode.send_keys('600026')
    female = driver1.find_element(By.XPATH, '//*[@id="stage-two"]/form/div/div[8]/div[2]/label')
    female.click()
    print("Gender clicked")
    single = driver1.find_element(By.XPATH, '//*[@id="stage-two"]/form/div/div[9]/div[2]/label')
    single.click()
    print("Marital status clicked")
    apply_now = driver1.find_element(By.ID, 'pf-apply-btn1')
    if apply_now.is_enabled():
        print("Apply now is enabed")
    else:
        print("Apply now is not enabled")
    apply_now.click()
    time.sleep(10)
    thankyou = driver1.find_element(By.XPATH, '//*[@id="feature-products"]/div/div')
    if thankyou.is_displayed():
        print("Form Submitted Sucessfully")
    else:
        print("Form not submitted")
    assert (False)
