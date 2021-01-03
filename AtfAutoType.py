from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import random

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.atfonline.cz")

username = driver.find_element_by_id('logName')
password = driver.find_element_by_id('logPass')
username.send_keys('Vaše přihlašovací jméno') # <- zde přepište 
password.send_keys('Vaše Heslo') # <- zde přepište 
password.send_keys(Keys.RETURN)

def typing():
    keyboard.wait("Ctrl")
    lection_text = driver.find_element_by_id("original")
    for i in list(lection_text.text):
        time.sleep(random.uniform(0.2,0.35)) # lekce se pudou psát průměrně okolo 200úh/min s tím, že každá lece bude mít trochu jiné hodnoty. Pokud chcete rychlost změnit, stačí přepsat hodnoty
        keyboard.write(i)
    typing()
typing()
