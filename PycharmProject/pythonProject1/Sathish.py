# from selenium import webdriver
# from seleniumpagefactory.Pagefactory import PageFactory
#
# class PageClass(PageFactory):
#
#     def __init__(self,driver):
#         self.driver = driver
#         self.timeout = 15           #(Optional - Customise your explicit wait for every webElement)
#         self.highlight = True       #(Optional - To highlight every webElement in PageClass)
#         self.mobile_test = False    #(Optional - Added for Appium support)
import os.path
file="InputFiles\GoldLoan.jpeg"
print(os.path.abspath(file))