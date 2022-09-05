#!/usr/bin/env python
# coding: utf-8

# BUT IT'S MULTITHREADING

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
from selenium.common.exceptions import *

#先把通知都關掉，不然後面會點不到按鈕
optionla = Options();
optionla.add_argument("disable-notifications");
driver = webdriver.Chrome(ChromeDriverManager().install(), options=optionla)
#driver.get("https://www.plurk.com")
#那些個%F0啥小的其實是一個笑臉的表情符號的Coding！

# In[2]:

"load face list"
import pickle
with open("Face_list.pkl", "rb") as f:
    face_list = pickle.load(f)
    f.close()
assert len(face_list) == 70

# file saving
from pathlib import Path
basedir = Path("faces")

if not basedir.is_dir():
    basedir.mkdir()

# the crawler per se


#自動化流程，跑這個就對了
def run_it(face_idx):

    emoji, filename = face_list[face_idx]

    TAR_URL = f"https://www.plurk.com/search?q={emoji}&date=2022-09"
    driver.get(TAR_URL)

    # "row to the bottom first"
    for i in range(600):
        driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
        sleep(0.5)

    # "then get the data"
    t = 0
    final = []
    #len(driver.find_elements(By.CSS_SELECTOR,"[class='plurk cboxAnchor divplurk bigplurk plink']"))
    #for i in range(0,10000):
    for el in driver.find_elements(By.CSS_SELECTOR,"[class='plurk cboxAnchor divplurk bigplurk plink']"):
        sleep(0.2)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #el = driver.find_elements(By.CSS_SELECTOR,"[class='plurk cboxAnchor divplurk bigplurk plink']")[i]
        sleep(0.2)
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(el, (el.size['width'])/2, 0)
        action.click()
        action.perform()
        sleep(0.2)
        try:
            testuser0 = driver.find_element(By.CSS_SELECTOR,"[class='cbox_plurk_holder']").find_element(By.CSS_SELECTOR,"[class='user']").text
            motherfucker = driver.find_elements(By.XPATH,"//div[@data-type='response']")
            testuser1 = motherfucker[0].find_element(By.XPATH,".//div[@class='user']").text
            testuser2 = motherfucker[1].find_element(By.XPATH,".//div[@class='user']").text
            testtext0 = driver.find_element(By.CSS_SELECTOR,"[class='cbox_plurk_holder']").find_element(By.CSS_SELECTOR,"[class='content']").text
            testtext1 = motherfucker[0].find_element(By.CSS_SELECTOR,"[class='content']").text
            testtext2 = motherfucker[1].find_element(By.CSS_SELECTOR,"[class='content']").text
            if testuser0==testuser2 and testuser0!=testuser1:
                TD = [[testuser0,testtext0],[testuser1,testtext1],[testuser2,testtext2]]
                print(TD)
                final.append(TD)
            else:
                print("可惜了")
        except:
            print("不合條件")
        sleep(0.2)
        #"add error handling"
        try:
            driver.find_element(By.CSS_SELECTOR, "[class='cbox_close pif-cancel']").click()
        except ElementNotInteractableException:
            pass
        t+=1
        print(t)
    with open(f"{basedir/filename}.json",'w', encoding = 'utf-8') as yyyyy:
        json.dump(final,yyyyy)
        yyyyy.close()

if __name__ == "__main__":
    import multiprocessing
    processes = []
    # loop thru the face list
    # and then fetch them
    # remember to redirect the output to a file
    # , instead of printing them all on the screen
    # face list index:
    #  disappointed but relieved, fearful

    # face_idx: put as many index in the list as you want
    for face_idx in [56, 51]:
        #run_it(face_idx)
        p = multiprocessing.Process(target=run_it, args=(face_idx,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print("mult succeeded!")



