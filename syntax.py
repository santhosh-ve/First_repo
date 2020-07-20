---Packages---

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import time
import openpyxl
import logging

***WebDriver***

driver = webdriver.Chrome(executable_path = "",chrome_options=) #To open a browser
driver.get("http://newtours.demoaut.com/") #To open url

***Browser options***
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("test",{"download.default_directory":"C:\NewFolder"})
driver = webdriver.Chrome(chrome_options=chromeOptions) 

***headless browser***
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


print(driver.title) #To get the page title
assert "Welcome: Mercury Tours" in driver.title #To verify the title
print(driver.current_url) #To get the current url
print(driver.page_source) #To get the HTML content of the page_source

driver.close() #Close current browser window
driver.quit() #Close all the windows

#Boolean 

is_enabled()
is_displayed()
is_selected()

#Navigation

driver.back()
driver.forward()

#Waits
#Implicit
driver.implicitly_wait(5)

#Explicit
from selenium.webdriver.support import expected_conditins as EC 
from selenium.webdriver.support.ui import WebDriverWait 

ExpWait = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"")))  #Include the driver and maximum time
element.click()

#Multiple check box
multiplecheckbox = driver.find_elements(By.XPATH,"//*[@id='contentblock']/section/div[4]//input")
for checkbox in multiplecheckbox:
    if not checkbox.is_selected():
        checkbox.click()
		
#No of options
Element = driver.find_element(By.CLASS_NAME,"dropdown")
dropdown = Select(Element) # Use select class
print(len(dropdown.options))

#To print the options
for option in dropdown.options:
    print(option.text)

#Dropdown actions
select_by_value
select_by_index
select_by_visible_text

#Alerts
driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()

#Frames
driver.switch_to_frame("classFrame")

#Browser window
driver.current_window_handle
driver.window_handles

#Scrolling
Scrolldown the page by pixel
driver.execute_script("window.scrollBy(0,500)","")

Scrolldown the page till element found
driver.execute_script("arguments[0].scrollintoView();",Element)

Scroll to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


#Actions
actions = ActionChains(driver)
actions.move_to_element().click().perform()

available actions 
drag_and_drop()
click_and_hold()
double_click()
context_click()

#To upload a file 
driver.find_element("sample").send_keys("filepath")


#Connect to db

import cx_Oracle
import os

os.environ['PATH'] = "Oracle desktop client"

#Establish db connection
con = cx_Oracle.connect("username","password","servername")

cur = con.cursor()
query1 = ""
query2 = ""
cur.close()

con.commit()
con.close()
