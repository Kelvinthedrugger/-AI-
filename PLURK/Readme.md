
### Account 1:

    name:     hardhardhard123
    password  suckmaid456

    email: 890225kelvin@gmail.com
    birthday: 1999/9/10

    tokens:
        Name: EMO_demo_0
        作者:	hardhardhard123
        Consumer_key:	jq5mU9ufmj6N
        Consumer_secret:	mNbClA7I1hbtsTM3uzCZMYcdQV1FtNMc

## Selenium (better)

see bottom of [04_selenium.ipynb](https://github.com/Kelvinthedrugger/-AI-/blob/main/PLURK/04_use_selenium.ipynb)

Steps:
   
    decide the emoji

    go to the search page & select end of date (normally 2022-8) and emoji

        e.g.,
        emoji: 😂; date: 2022-8
        
        https://www.plurk.com/search?q=%F0%9F%98%82&date=2022-08

    check folder & file name

    run the notebook


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

