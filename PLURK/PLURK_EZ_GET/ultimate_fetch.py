# ULTIMATE VER.
#from MULT_Plurk_Stead_Data_smiling_face_with_open_mouth import * // this line doesn't work for some reason

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
optionla.add_argument('--headless') # don't render the webpage per se, but more difficult to debug
optionla.add_argument('--disable-gpu') # prevent weird bug
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=optionla)
#driver.get("https://www.plurk.com")
#那些個%F0啥小的其實是一個笑臉的表情符號的Coding！


"load face list"
import pickle
with open("Face_list.pkl", "rb") as f:
    face_list = pickle.load(f)
    f.close()
assert len(face_list) == 70

# file saving
from pathlib import Path
basedir = Path("faces_exp") # change to faces_experiment just in case the quality is weird?

# the crawler per se


#自動化流程，跑這個就對了
def run_it(face_idx):

    emoji, filename = face_list[face_idx]

    # check if file exists or not
    if P(basedir/(filename+".json")).is_file():
        print(f"{filename} has been fetched, skip")
        return

    # make driver local
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=optionla)

    TAR_URL = f"https://www.plurk.com/search?q={emoji}&date=2022-09"
    driver.get(TAR_URL)

    # "row to the bottom first"
    # should change to while not bottom: scroll the darn thing?
    #for i in range(600):
    #    driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
    #    sleep(0.5)
    # "SUCCEEDED", while not at the buttom, scroll it!
    while len(driver.find_elements(By.XPATH, '//*[@id="result"]//*[@class="status-holder"]//*[@class="button"]')) == 0:
        driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
        sleep(0.3)

    # "then get the data"
    # t = 0 # move this into the loop
    final = []
    for t, el in enumerate(driver.find_elements(By.CSS_SELECTOR,"[class='plurk cboxAnchor divplurk bigplurk plink']")):
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
            # here? moved!
            if testuser0==testuser2 and testuser0!=testuser1:
                testtext0 = driver.find_element(By.CSS_SELECTOR,"[class='cbox_plurk_holder']").find_element(By.CSS_SELECTOR,"[class='content']").text
                testtext1 = motherfucker[0].find_element(By.CSS_SELECTOR,"[class='content']").text
                testtext2 = motherfucker[1].find_element(By.CSS_SELECTOR,"[class='content']").text
                TD = [[testuser0,testtext0],[testuser1,testtext1],[testuser2,testtext2]]
                print(TD)
                final.append(TD)
            # move this to front so that we don't have to find the texts of invalid ones?
            # testtext0 = driver.find_element(By.CSS_SELECTOR,"[class='cbox_plurk_holder']").find_element(By.CSS_SELECTOR,"[class='content']").text
            # testtext1 = motherfucker[0].find_element(By.CSS_SELECTOR,"[class='content']").text
            # testtext2 = motherfucker[1].find_element(By.CSS_SELECTOR,"[class='content']").text
            # if testuser0==testuser2 and testuser0!=testuser1:
                # TD = [[testuser0,testtext0],[testuser1,testtext1],[testuser2,testtext2]]
                # print(TD)
                # final.append(TD)
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

    # close the driver / browser after the task for this emoji is done
    driver.quit()


# fetch ALL 70 POSTS
# not tested
# TODO
# (done)add filename check: check if the file exists
# (done)make driver a local variable, aka, put it in the function to run faster
# (done)close the driver after done fetching on emoji

if __name__ == "__main__":
    import multiprocessing
    import sys
    # instead of doing this, we should get all 70 files
    # and exclude the fetched ones
    # remember to exclude the ones from Sam as well?
    """
    tar = [int(ele) for ele in sys.argv[1:] if len(ele) > 0 and ele[0] in "0123456789"]
    processes = []
    for face_idx in list(map(int, tar)):
        #run_it(face_idx)
        p = multiprocessing.Process(target=run_it, args=(face_idx,))
        processes.append(p)
        p.start()

    # Try to maintain len(working queue) == 8
    #  if one is done, insert new one to that position
    #   pop the one that's done

    for process in processes:
        process.join()

    """

    # below is run all at once version
    tar = [int(ele) for ele in sys.argv[1:] if len(ele) > 0 and ele[0] in "0123456789"]
    all_ps = []
    processes = []
    for face_idx in list(map(int, tar)):
        p = multiprocessing.Process(target=run_it, args=(face_idx,))
        processes.append(p)

    # Try to maintain len(working queue) == 8
    #  if one is done, insert new one to that position
    #   pop the one that's done
    tmpp = []
    for p in processes:
        if len(tmpp) < 8:
            tmpp.append(p)
        else:
            all_ps.append(tmpp)
            tmpp = [] # reset

    # 8 at a time
    # but not what i mean by 'maintain the queue'
    for process_list in all_ps:
        for process in process_list:
            process.join()


    print("mult succeeded!")



