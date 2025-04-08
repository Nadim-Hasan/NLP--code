from selenium import webdriver
from selenium.webdriver.common.by import By


import time 
driver = webdriver.Chrome()
import re
driver.get("https://www.daraz.com.bd/catalog/?page=1&q=sand%20timer")
driver.maximize_window()

total_product_text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text

print (total_product_text)
pattern = r"\b\d+\b"

match = re.search(pattern, total_product_text)
bnumber = 0 
all_text = []
all_img =[]
all_links = []
if match :
    bnumber = match.group()
    print ("Bnumber", bnumber)
total = int(bnumber)
total_pages = round(total/40)

print(total_pages)


for page in range (1, total_pages + 1):
    p = str(page)
    driver.get(f'https://www.daraz.com.bd/catalog/?page={p}&q=sand%20timer')
    for t in range (1,40):
      txt = str(t)
      text_x_path = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+txt+']/div/div/div[2]/div[2]/a'
      text = driver.find_element(By.XPATH, text_x_path).text
      all_text.append(text)
      #links_x_path = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+txt+']/div/div/div[2]/div[2]/a'
      #links = driver.find_element(By.XPATH, links_x_path).get_attribute("href")
      #all_links.append(links)

      #img_x_path  = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+txt+']/div/div/div[1]/div/a/div/img'
      #imgs = driver.find_element(By.XPATH, img_x_path).get_attribute("src")
      #all_img.append(imgs) 


print("TEXT" , len(all_text))
# print("Link", len(all_links))
#print ("Image", all_img)
time.sleep(60)
driver.quit()

