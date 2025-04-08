from selenium import webdriver
from selenium.webdriver.common.by import By


import time 
driver = webdriver.Chrome()
import re
driver.get("https://www.daraz.com.bd/products/30-i316622489-s1603255104.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Asand%252Btimer%253Bnid%253A316622489%253Bsrc%253ALazadaMainSrp%253Brn%253A44f0debf747d05163fd8c6e6b8775d09%253Bregion%253Abd%253Bsku%253A316622489_BD%253Bprice%253A369%253Bclient%253Adesktop%253Bsupplier_id%253A700508304165%253Bbiz_source%253Ah5_external%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10000439%253Bitem_id%253A316622489%253Bsku_id%253A1603255104%253Bshop_id%253A142792%253BtemplateInfo%253A1104_L%2523-1_A3_C%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Chattogram&price=369&priceCompare=skuId%3A1603255104%3Bsource%3Alazada-search-voucher%3Bsn%3A44f0debf747d05163fd8c6e6b8775d09%3BoriginPrice%3A36900%3BdisplayPrice%3A36900%3BsinglePromotionId%3A50000029766019%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1744123100720&ratingscore=4.34765625&request_id=44f0debf747d05163fd8c6e6b8775d09&review=256&sale=1312&search=1&source=search&spm=a2a0e.searchlist.list.0&stock=1")
driver.refresh() #chace refresh the file 
driver.maximize_window()

height = driver.execute_script('return document.body.scrollHeight')  #java script marlam zeno page ta valo kore load hoy

print("height",height)

for i in range(0,height+600,50):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

comment = driver.find_elements(By.CLASS_NAME, 'content')  #list wise gather all the data
for i in comment:
    print(i.text)
#locator must be same for find_element(s)

#comment = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[1]/div[3]/div[1]').text

#print(comment)

time.sleep(60)
driver.quit()
