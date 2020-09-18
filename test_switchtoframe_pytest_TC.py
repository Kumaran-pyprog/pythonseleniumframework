#Switch TO Frame Testcase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
import pytest
import time

@pytest.mark.smoketest
def test_switchToFrame_tc():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm')
    xpath_iframe = '//iframe[@id="iframeResult"]'
    xpath_trybtn = '//button[.="Try it"]'
    # click iframe box
    iframe_butn = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(xpath_iframe))
    # accept the iframe
    driver.switch_to.frame(iframe_butn)
    # select and click Try it button
    tryit_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(xpath_trybtn))
    tryit_button.click()
    # dynamic way to handle windows popup
    try:
        alert_acept = driver.switch_to.alert
        alert_acept.accept()  # if you want ok ,you can use accept
        # if you want cancel ,you can use dismiss
    except:
        print("No alert found")


def test_tearDown():
    # close the driver
    driver.close()
