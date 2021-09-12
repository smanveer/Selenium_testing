import os
import unittest
import sys
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/Manveer/.AndroidStudio3.4/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
        # Url
driver.get("https://www.dentrix.com/products/eservices/eclaims/payor-search?keyword=")

       #search blue in payor search
textfield = driver.find_element_by_id("keyword")
textfield.send_keys("blue")
button= driver.find_element_by_id("payor_searchBtn")
button.click()
        

if __name__ == "main":
    unittest.main()