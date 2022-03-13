#https://github.com/SergeyPirogov/webdriver_manager (for the first four lines)
#This one if for windows with chrome
from selenium.webdriver.common.by import By
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Global_Variables
TOTALSECONDS=60
SPANNUM=1

#StartHere
driver.get("https://10fastfingers.com/typing-test/english")

driver.implicitly_wait(3)

t_end = time.time() + TOTALSECONDS
while time.time() < t_end:
    Word1=driver.find_element(by=By.XPATH, value='//div[@id="row1"]/span['+str(SPANNUM)+']')
    listWord=list(Word1.text)
    for letter in listWord:
        pyautogui.typewrite(letter)
    pyautogui.typewrite(" ")
    SPANNUM=SPANNUM+1

time.sleep(10)
driver.quit()
 