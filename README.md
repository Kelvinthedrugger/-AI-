# -AI-

About
This repo contains the code snippets for 中技AI competition 2022. Product name: EMO-AI,對話不難──即時線上對話情緒分析 工具


<b>(should we hide this?)</b>Notion: https://www.notion.so/AI-_Database-5f3828b51a004e8aa5ef67f2e4190a0e


### twitter_sentiment_kaggle.zip

Due to it's large size ( > 50 Mb, over the recommended size of git), if there's an problem, 

a. fetch the local storage
b. just visit the source (see notion)


### plurk dataset

It now works!

To fetch newest data, just run

```python
# inside Plurk folder
from plurk.all import *
content = fetch_emoji(emoji='your emoji')
for ele in content: print(ele)
"For more info, see Plurk folder"
```



