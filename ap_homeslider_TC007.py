#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#import time module
import time
#import Select module
from selenium.webdriver.support.select import Select
#declare and initialize the driver variable
driver=webdriver.Chrome()
#browser should be loaded in maximized window
driver.maximize_window()
#driver should wait impicitly for a given duration ,for the element under the considertaion to load.
#we will use built-in implicitly_wait() of our driver projects
driver.implicitly_wait(10)#10 sec
#to load given url in the browser window
driver.get('http://automationpractice.com/index.php')

#Automate the homeslider images and find the no of images in the Homeslider
driver.find_element_by_xpath('//ul[@id="homeslider"]')
webelement_homeslider=driver.find_elements_by_xpath('//ul[@id="homeslider"]/li/a')
#find the length of the homeslider images
lengthof_homeslider=len(webelement_homeslider)
print('No of images present in homslider :',lengthof_homeslider)

#Automating the buttons previous and back
driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]')
driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]/div')
homeslider_butnnext=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]/div/a[2]'))
homeslider_butnnext.click()
time.sleep(2)

homeslider_butnprev=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//*[@id="homepage-slider"]/div/div[2]/div/a[1]'))
homeslider_butnprev.click()

#Automate the homecontent and find the no of image in the homecontent
driver.find_element_by_xpath('//ul[@class="htmlcontent-home clearfix row"]')
webelement_homecontent=driver.find_elements_by_xpath('//ul[@class="htmlcontent-home clearfix row"]/li')
#find the length of the homecontent images
lengthof_homecontent=len(webelement_homecontent)
print("No of images present in homecontent :",lengthof_homecontent)

driver.close()
