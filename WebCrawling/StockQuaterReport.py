# Import all the required library

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time


# Set the chrome driver webdriver.Chrome(<chrome driver path>/chromedriver.exe)
# This is for open the google chrome in background to extract the data in page 1 and automatic follow the href link to next page

driver = webdriver.Chrome('C:/Boon/chromedriver/chromedriver.exe') # path need to be changed accordingly

# We need to extract for whole year of 2019 (from Jan 1 until latest)

# The website will update everyday so everytime we run the code we
# will update the table with latest data.


# Extract the table data in html format from website via chrome driver
# Starting with Sep-19 (since the time of coding in Sep-19)

driver.get('https://www.malaysiastock.biz/Quarterly-Report.aspx?year=2019&month=9')


# extract the table data in first page

pageSource_1 = driver.page_source


# move to the next page
driver.find_element_by_link_text("2").click()

# extract the table data in the second page
pageSource_2 = driver.page_source

# close the chrome
driver.close()


# Build a function to sort the page source (html) into dataframe table

def into_table(x):
    bs = BeautifulSoup(x, 'html.parser')
    xx= bs.find('table',{'class':'mGrid'})
    xx_rows = xx.find_all('tr')
    A = []
    for tr in xx_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        A.append(row)
    return pd.DataFrame(A, columns=["Date", "Stock", "Quater","Revenue(RM,000)","Net_Profit(RM,000)","Earning_Per_Share (Cent)",
                                        "Dividend","Overview"])
    
# Use the function to sort page source into the table
Sep_part1 = into_table(pageSource_1)  
Sep_part2 = into_table(pageSource_2)

# Repeat the process for Aug'19

driver = webdriver.Chrome('C:/Boon/chromedriver/chromedriver.exe')
driver.get('https://www.malaysiastock.biz/Quarterly-Report.aspx?year=2019&month=8')

pageSource_1 = driver.page_source

driver.find_element_by_link_text("2").click()
pageSource_2 = driver.page_source

driver.find_element_by_link_text("3").click()
pageSource_3 = driver.page_source

driver.find_element_by_link_text("4").click()
pageSource_4 = driver.page_source

driver.find_element_by_link_text("5").click()
pageSource_5 = driver.page_source

driver.find_element_by_link_text("6").click()
pageSource_6 = driver.page_source

driver.find_element_by_link_text("7").click()
pageSource_7 = driver.page_source

driver.find_element_by_link_text("8").click()
pageSource_8 = driver.page_source

driver.find_element_by_link_text("9").click()
pageSource_9 = driver.page_source

driver.find_element_by_link_text("10").click()
pageSource_10 = driver.page_source

driver.find_element_by_link_text("...").click()
pageSource_11 = driver.page_source

driver.find_element_by_link_text("12").click()
pageSource_12 = driver.page_source

driver.find_element_by_link_text("13").click()
pageSource_13 = driver.page_source

driver.find_element_by_link_text("14").click()
pageSource_14 = driver.page_source

driver.find_element_by_link_text("15").click()
pageSource_15 = driver.page_source

driver.find_element_by_link_text("16").click()
pageSource_16 = driver.page_source

driver.find_element_by_link_text("17").click()
pageSource_17 = driver.page_source

driver.close()

def into_table2(x):
    bs = BeautifulSoup(x, 'html.parser')
    xx= bs.find('table',{'class':'mGrid'})
    xx_rows = xx.find_all('tr')
    A = []
    for tr in xx_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        A.append(row)
    return pd.DataFrame(A, columns=["Date", "Stock", "Quater","Revenue(RM,000)","Net_Profit(RM,000)","Earning_Per_Share (Cent)",
                                        "Dividend","Overview",'junk','junk2','junk3','junk4'])

Aug_part1 = into_table2(pageSource_1)
Aug_part2 = into_table2(pageSource_2)
Aug_part3 = into_table2(pageSource_3)
Aug_part4 = into_table2(pageSource_4)
Aug_part5 = into_table2(pageSource_5)
Aug_part6 = into_table2(pageSource_6)
Aug_part7 = into_table2(pageSource_7)
Aug_part8 = into_table2(pageSource_8)
Aug_part9 = into_table2(pageSource_9)
Aug_part10 = into_table2(pageSource_10)
Aug_part11 = into_table2(pageSource_11)
Aug_part12 = into_table2(pageSource_12)
Aug_part13 = into_table2(pageSource_13)
Aug_part14 = into_table2(pageSource_14)
Aug_part15 = into_table2(pageSource_15)
Aug_part16 = into_table2(pageSource_16)
Aug_part17 = into_table2(pageSource_17)

# randomly testing on the extraction
Aug_part5,Aug_part11,Aug_part17

# the process will continue to other month until all the whole year data was acheived
# then will proceed to cleaning & compile the data
