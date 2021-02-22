from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#ENTER THE FOLLOWING CREDENTIALS
recipent = "WHOM YOU WANT TO SEND"
SUBJECT = "THE SUBJECT OF THE EMAIL"
BODY  = "THE BODY OF THE EMAIL"
YOUR_EMAIL = "ENTER YOUR EMAIL HERE"
YOUR_PASSWORD = "ENTER YOUR PASSWORD HERE"



driver = webdriver.Safari()


driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(1)
name = driver.find_element_by_id("identifierId")
name.send_keys(YOUR_EMAIL)
name.send_keys(Keys.RETURN)
time.sleep(2)

pas = driver.find_element_by_class_name("whsOnd.zHQkBf")
pas.send_keys(YOUR_PASSWORD)
pas.send_keys(Keys.RETURN)
time.sleep(2)


driver.get("https://mail.google.com/mail/u/0/#inbox")
compose= driver.find_element_by_class_name("T-I.T-I-KE.L3")
compose.click()
time.sleep(2)	

reci = driver.find_element_by_name("to")
reci.click()
reci.send_keys(recipent)
reci.send_keys(Keys.RETURN)


subject = driver.find_element_by_name("subjectbox")
subject.click()
subject.send_keys(SUBJECT)

body = driver.find_element_by_class_name("Am.Al.editable.LW-avf.tS-tW")
body.click()
body.send_keys(BODY)

submit = driver.find_element_by_id(":8i")
submit.click()
time.sleep(3)
driver.quit()

