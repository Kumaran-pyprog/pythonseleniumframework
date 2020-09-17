
#Testcase:1 switch_to_frame
#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
#driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm')
driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm')
#select Try it Yourself  button and  click it
time.sleep(5)
#switch_to.frame
#<iframe frameborder="0" id="iframeResult" name="iframeResult" xpath="1"></iframe>
# xpath   //iframe[@id='iframeResult']
xpath_iframe='//iframe[@id="iframeResult"]'
xpath_trybtn='//button[.="Try it"]'
#click iframe box
iframe_butn=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(xpath_iframe))
#accept the iframe
driver.switch_to.frame(iframe_butn)
#select and click Try it button
tryit_button=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(xpath_trybtn))
tryit_button.click()
#accept the alert by using switch_to.alert()
alert_acept=driver.switch_to.alert
alert_acept.accept()
time.sleep(10)
#close the driver
driver.close()
