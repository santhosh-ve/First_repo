import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="specifypathofthedriver")
driver.get("enterurl")
driver.maximize_window()

path = "specifyexcelfilepath"
rows = XLUtils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
	username = XLUtils.readData(path,"Sheet1",r,1)
	password = XLUtils.readData(path,"Sheet1",r,2)
	
	driver.find_element_by_name("userName").send_keys(username)
  driver.find_element_by_name("password").send_keys(password)
	driver.find_element_by_name("login").click()
	
	 if driver.title == "pagetitle":
        print("Test Passed!")
        XLUtils.writeData(path,"Sheet1",2,3,"Test Passed!!")
    else:
        print("Test failed")
		    XLUtils.writeData(path,"Sheet1",2,3,"Test Failed!!")
        driver.find_element_by_link_text("Home").click()

driver.close()
