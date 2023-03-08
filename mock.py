from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pickle
import test_present_prn

driver = webdriver.Chrome()

driver.get("C:/Users/adity/OneDrive/Desktop/edi kmkc/software/mcok/copy_.html")
driver.implicitly_wait(5)

file=  open("final_presnt_prn.p", 'rb')

Present_prn=pickle.load(file)


for i in range (1,12):
    xpath_prn= (f"/html/body/div/div[2]/table/tbody/tr[%d]/td[3]" %(i))
    xpath_but= (f"/html/body/div/div[2]/table/tbody/tr[%d]/th/input" %(i))
    
    prn_ele=driver.find_element(By.XPATH,xpath_prn).text
 
    
    for j in Present_prn:
        if(prn_ele== str(j)):       
            driver.find_element(By.XPATH,xpath_but).click()
            print("check "+ prn_ele)


time.sleep(3600)
