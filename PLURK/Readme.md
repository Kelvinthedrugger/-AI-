
## Selenium (better)

see bottom of [04_selenium.ipynb](https://github.com/Kelvinthedrugger/-AI-/blob/main/PLURK/04_use_selenium.ipynb)

see [fix_0805.ipynb](https://github.com/Kelvinthedrugger/-AI-/blob/main/PLURK/fix_0805.ipynb) // this is better!

see [create_dataset.ipynb](https://github.com/Kelvinthedrugger/-AI-/blob/main/PLURK/create_dataset.ipynb) // the whole thing together!

### Stable posts on plurk

### load the whole dataset at once

```python
from pathlib import Path as P

target_dir = P("total_dataset")
target_file = target_dir/"dataset.pkl"

with open(target_file, "rb") as f:
    reload_f = pickle.load(f)

print(len(reload_f), reload_f[0])

# output:
# (23510,
 ('伴侶：臭貓貓 我玩遊戲的時候一直煩我，罵他還一直蹭我😡\n（還是伴侶）\n伴侶：我早上幫他乾洗澡後他就不讓我摸摸了😭', 'anger', '😡'))
```

#### stable_pkl/
#### fix_0804/

#### larger file size -> more posts!

### Ways to read the files (.pkl, .pickle)

```python
"For example with context, see 'fix_0805.ipynb'"
import os, pickle
from pathlib import Path

# enter the folder that you want
dir_name = Path("the directory that you want")

# get the files in that directory
file_list = list(os.walk(dir_name))[0][2]

# collect files here
posts = []

for ele in file_list:
    # notice that each ele is a list, very easy to use
    with open(dir_name/ele, "rb") as f:
        posts.append(pickle.load(f))

# check the content
from info_list import emoji_list

for ele in posts:
    idx = ele.index(".")
    if "_" in ele:
        idx = ele.index("_")

    print(emoji_list[:idx], ele[0]) 

```

#### Steps to fetch emoji on Plurk
   
    decide the emoji

    go to the search page & select end of date (normally 2022-8) and emoji

        e.g.,
        emoji: 😂; date: 2022-8
        
        https://www.plurk.com/search?q=%F0%9F%98%82&date=2022-08

    check folder & file name

    run the notebook


#### Tips, login before you fetch allows you to view adult content (that's what they said on the website)
```python
driver.get("https://www.plurk.com/login?r=")
#輸入帳密
usr, pwd = input("account: "), input("password: ") 

key1 = driver.find_element("id", "input_nick_name")
key1.send_keys(usr)
sleep(0.5)
key2 = driver.find_element("id", "input_password")
key2.send_keys(pwd)
sleep(0.5)
driver.find_element("id","login_submit").click()
print("Login done!")

```

## Plurk API

### To request a token:
        
[Plurk OAuth service endpoints](https://www.plurk.com/API/2):

obtain request token: https://www.plurk.com/OAuth/request_token (HTTPS GET/POST)
authorization page: https://www.plurk.com/OAuth/authorize
authorization page for mobile: https://www.plurk.com/m/authorize
obtain access token: https://www.plurk.com/OAuth/access_token (HTTPS GET/POST)


### Steps

visit [here](https://www.plurk.com/PlurkApp/) to see the list of application we've applied

click 測試工具 on the app you want (EMO_demo_0 in this case, it's a web crawler)

and you'll be able to generate tokens


## !別急著關掉驗證碼頁面, 你在測試的時候需要他, shxt


### Docs

Python module doc: [link](https://github.com/clsung/plurk-oauth)

Plurk API doc: [link](https://www.plurk.com/API/2)

