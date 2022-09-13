# post only!!!!
# since we now training on {text->[V,A]}
# , there's no guarantee that the comments will have
# the same [V,A] to the post
# so, we fetch the posts
# Option 1: fetch post + ABA
# Option 2: fetch post only, don't check for ABA condition
# Probably option 2, since we want our VA to be as precise as possible?

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

"load face list"
import pickle
with open("Face_list.pkl", "rb") as f:
    face_list = pickle.load(f)
    f.close()
assert len(face_list) == 70

# file saving
from pathlib import Path
basedir = Path("faces_ANOTHER") # change to faces_experiment just in case the quality is weird?

# FUCK
if not basedir.is_dir():
    basedir.mkdir()


# the crawler per se

#自動化流程，跑這個就對了
def run_it(face):

    #emoji, filename = face_list[face_idx]
    emoji, filename = face[0], face[1]
    #print(emoji, filename)
    # check if file exists or not
    if Path(basedir/(filename+".json")).is_file():
        print(f"{emoji} {filename} has been fetched, skip")
        return

    # make driver local
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=optionla)

    TAR_URL = f"https://www.plurk.com/search?q={emoji}&date=2022-09"
    driver.get(TAR_URL)

    # "row to the bottom first"
    # should change to while not bottom: scroll the darn thing?
    # "SUCCEEDED", while not at the buttom, scroll it!
    while len(driver.find_elements(By.XPATH, '//*[@id="result"]//*[@class="status-holder"]//*[@class="button"]')) == 0:
        driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
        sleep(0.3)

    # "then get the data"
    # t = 0 # move this into the loop
    final = []
    #for t, ele in ...:
    posts = driver.find_elements('xpath', '//*[@class="content"]')
    final = [ele.text for ele in posts]

    with open(f"{basedir/filename}.json",'w', encoding = 'utf-8') as yyyyy:
        json.dump(final,yyyyy)
        yyyyy.close()

    print(f"{emoji} {filename} fetch succeeded")
    # close the driver / browser after the task for this emoji is done
    driver.quit()


if __name__ == "__main__":
    import multiprocessing
    import sys
    
    "e.g.,"
    tar_tmp = [
        "🤗 huggingface",
        "😁 grinningfacewithsmilingeyes", #Grinning face with smiling eyes')",
        "😆 grinningsquintingface"
    ]

    "split the target into [emoji, text] format"
    tar = [ele.split(" ") for ele in tar_tmp]
    "to record the processes"
    processes = []

    for face in tar:
        p = multiprocessing.Process(target=run_it, args=(face,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()


