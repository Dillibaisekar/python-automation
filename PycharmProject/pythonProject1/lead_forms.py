import parent_class



import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome(executable_path="E:\DRIVER\chromedriver.exe")
driver.get("https://sitsfl.stfc.in/")
driver.maximize_window()
time.sleep(3)
element_to_hover_over=driver.find_element(By.XPATH,'//*[@id="body"]/app-root/app-header/header/section[2]/div/div/div[2]/p')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
parent_class.getElementById("main_nav_tyre")
print("Navin Done!")
print("Hello")

