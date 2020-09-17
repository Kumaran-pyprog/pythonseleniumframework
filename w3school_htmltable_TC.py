from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
import time
import unittest
#selenium webdriver ,initialization,maximize window
'''
#Testcase:Find the Company and where it located
driver=webdriver.Chrome()
#nvigate the webpage
driver.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver.maximize_window()
driver.implicitly_wait(10)

#Find the company location
table=driver.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    if(len(tds)>0):
        if(tds[0].text=='Island Trading'):
            print(tds[2].text)
#close the driver
driver.close()
print()

#Testcase1:Find Rows and Colums in HTML Table
driver1=webdriver.Chrome()
#nvigate the webpage
driver1.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver1.maximize_window()
driver1.implicitly_wait(10)

#Find the No of Rows and columns  in HTML Table
table=driver1.find_element_by_id("customers")
nrow_tr=table.find_elements_by_xpath('//table[@id="customers"]/tbody/tr')
ncol_th = table.find_elements_by_xpath('//table[@id="customers"]/tbody/tr[1]/th')
nrows=len(nrow_tr)
ncols=len(ncol_th)
print("No of Rows in HTML Table:",nrows)
print("No of column in HTML Table:",ncols)
#close the driver
driver1.close()
print()

#Testcase2:
driver2=webdriver.Chrome()
#nvigate the webpage
driver2.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver2.maximize_window()
driver2.implicitly_wait(10)

#No of company using xpath in HTML Table
tr_compny=driver2.find_elements_by_xpath('//table[@id="customers"]/tbody/tr')
lenth_of_company=len(tr_compny)-1
print("No of company in HTML Table:",lenth_of_company)
#close the driver
driver2.close()

#Testcase3:Find No of company in HTML Table
driver3=webdriver.Chrome()
#nvigate the webpage
driver3.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver3.maximize_window()
driver3.implicitly_wait(10)
#Finding No of company using count() in HTML Table
table=driver3.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
count = 0
for tr in trs:
    tds = tr.find_elements_by_tag_name('td')
    for i in range(len(tds)):
        if i==0:
            count+=1
print("No of company present in HTML Table:",count)
#close the driver
driver3.close()
print()


#Testcase:4 Printing all the company name
print("Print All company Name:")
driver4=webdriver.Chrome()
#nvigate the webpage
driver4.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver4.maximize_window()
driver4.implicitly_wait(10)

#Printing all the company name
table=driver4.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    if(len(tds)>0):
        if(tds[0].text=='Alfreds Futterkiste'):
            print(tds[0].text)
        if (tds[0].text == 'Centro comercial Moctezuma'):
            print(tds[0].text)
        if (tds[0].text == 'Ernst Handel'):
            print(tds[0].text)
        if (tds[0].text == 'Island Trading'):
            print(tds[0].text)
        if (tds[0].text == 'Laughing Bacchus Winecellars'):
            print(tds[0].text)
        if (tds[0].text == 'Magazzini Alimentari Riuniti'):
            print(tds[0].text)
#close the driver
driver4.close()

#Testcase:5 Printing all the company name
print("Print All company Name:")
driver4=webdriver.Chrome()
#nvigate the webpage
driver4.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver4.maximize_window()
driver4.implicitly_wait(10)

#Printing all the company name
table=driver4.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    for i in range(len(tds)):
        if i ==0:
            print(tds[0].text)
#close the driver
driver4.close()
print()

#Testcase:6
#To display all the company contacts
print("Print All Company Contact")
driver5=webdriver.Chrome()
#nvigate the webpage
driver5.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver5.maximize_window()
driver5.implicitly_wait(10)

#display all the company contacts
table=driver5.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    for i in range(len(tds)):
        if i ==1:
            print(tds[1].text)
#close the driver
driver5.close()
print()

#Testcase7
#To display all the country name
print("Print All the country name:")
driver6=webdriver.Chrome()
#nvigate the webpage
driver6.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver6.maximize_window()
driver6.implicitly_wait(10)

#display all the country name
table=driver6.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    for i in range(len(tds)):
        if i ==2:
            print(tds[2].text)
#close the driver
driver6.close()
print()

#Testcase8:Print all the row value
driver7=webdriver.Chrome()
#nvigate the webpage
driver7.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver7.maximize_window()
driver7.implicitly_wait(10)

#display all the  row value
table=driver7.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    for i in range(len(tds)):
        if i==0:
            print(tds[0].text)
        if i==1:
            print(tds[1].text)
        if i==2:
            print(tds[2].text)

#close the driver
driver7.close()
print()


#Testcase8:Print the all row element
driver8=webdriver.Chrome()
#nvigate the webpage
driver8.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver8.maximize_window()
driver8.implicitly_wait(10)

#display all the row element
table=driver8.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    for i in range(len(tds)):
        if i==0:
            print(tds[0].text,tds[1].text,tds[2].text)
#close the driver
driver8.close()


#Testcase9:Print the 1st row element
driver9=webdriver.Chrome()
#nvigate the webpage
driver9.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver9.maximize_window()
driver9.implicitly_wait(10)

#display the 1st of  row element
table=driver9.find_element_by_id("customers")
trs=table.find_elements_by_tag_name('tr')
tds=table.find_elements_by_tag_name('td')
for i in range(len(tds)):
    if i==0:
        print(tds[0].text,tds[1].text,tds[2].text)

#close the driver
driver9.close()
print()
'''
#Testcase10:Print all the company name without using index value
driver9=webdriver.Chrome()
#nvigate the webpage
driver9.get('https://www.w3schools.com/html/html_tables.asp')
#maximize the window
driver9.maximize_window()
driver9.implicitly_wait(10)
#Find the No of Rows and columns  in HTML Table
table=driver9.find_element_by_id("customers")
nrow_tr=table.find_elements_by_xpath('//table[@id="customers"]/tbody/tr')
ncol_th = table.find_elements_by_xpath('//table[@id="customers"]/tbody/tr[1]/th')
nrows=len(nrow_tr)
ncols=len(ncol_th)
print("No of cols in HTML Table:",nrows)
print("No of cols in HTML Table:",ncols)
for i in range(2,nrows+1):
    row=[]
    for j in range(1,2):
        row.append(table.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text)
    #print(row)
    for col0_value in row:
        print(col0_value)
#close the driver
driver9.close()
print()