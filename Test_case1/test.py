import os
import unittest
import sys
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/Manveer/.AndroidStudio3.4/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
        # Url
driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?keyword=")

       #Goto overview
b= driver.find_element_by_link_text("Overview")
b.click()

if __name__ == "main":
    unittest.main()