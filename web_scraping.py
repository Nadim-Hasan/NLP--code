from selenium import webdriver #webdrive ekta name dilam, web k calanor jonno
from selenium.webdriver.common.by import By


import time # time import korlam

driver = webdriver.Chrome()

driver.get("https://www.daraz.com.bd/catalog/?spm=a2a0e.tm80335411.search.9.14fe12f77XUUZn&q=sand%20timer&_keyori=ss&from=search_history&sugg=sand%20timer_7_1")  # give the link of the web site where I really want to make scraping
driver.maximize_window() # for full screen the window

all_text =[]

links = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute("href")

img = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img').get_attribute("src")

for t in range (1,5):
    txt = str(t)
    x_path = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+txt+']/div/div/div[2]/div[2]/a'
    text = driver.find_element(By.XPATH, x_path).text
    all_text.append(text)


print("TEXT" , all_text)
print("Link", links)
print ("Image", img)
time.sleep(5)
driver.quit()

