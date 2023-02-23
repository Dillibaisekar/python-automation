from datetime import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import parent_class

driver=webdriver.Chrome()
driver.get("https://sitsfl.stfc.in/")
driver.maximize_window()
element_to_hover_over=driver.find_element(By.XPATH,"//div[@class='head-link'][1]")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
parent_class.ele("main_nav_rd")
print("Navin Done!")
print("Hello")
#
