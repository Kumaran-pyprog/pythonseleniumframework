#import selenium webdriver
from selenium import webdriver
#import time module
import time
#import Select module
from selenium.webdriver.support.select import Select
#declare and initialize the driver variable
driver=webdriver.Chrome('C:\Driver\chromedriver_win32\chromedriver.exe')
#browser should be loaded in maximized window
driver.maximize_window()
#driver should wait impicitly for a given duration ,for the element under the considertaion to load.
#we will use built-in implicitly_wait() of our driver projects
driver.implicitly_wait(10)#10 sec
#to load given url in the browser window
driver.get('http://automationpractice.com/index.php')

#Navigate the poular menu and click the button
driver.find_element_by_xpath('//ul[@id="home-page-tabs"]/li[1]/a').click()
#Finding the No of Grid items in Popular menu Using xpath locator
webelement_popular=driver.find_elements_by_xpath("//ul[@id='homefeatured']/li")
lenof_griditems_popular=len(webelement_popular)
#display the No of images present in popular menu
print("No of images present in popular :",lenof_griditems_popular)
time.sleep(2)

#Navigate the poular menu and click the button
driver.find_element_by_xpath('//ul[@id="home-page-tabs"]/li[2]/a').click()
#Finding the No of Grid items in Bookseller menu Using xpath locator
webelement_bestseller=driver.find_elements_by_xpath('//ul[@id="blockbestsellers"]/li')
#display No of image present in bestseller
lenof_griditems_bookseller=len(webelement_bestseller)
print("No of images present in Bookseller :",lenof_griditems_bookseller)
driver.close()
