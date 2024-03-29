# -AI-

### About
This repo contains the code snippets for 中技AI competition 2022. Product name: EMO-AI,對話不難──即時線上對話情緒分析 工具



### twitter_sentiment_kaggle.zip

Due to it's large size (> 50 MB, over the recommended size of git)
if there's an problem, 

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

Or, for how to fetch many posts at once, see [here](https://github.com/Kelvinthedrugger/-AI-/tree/main/emo_nbs/CODE_EXAMPLE_TO_PUSH/Multi_thread_web_scraper)

### Emoji to VA model
Below is the link to how we convert Emoji to VA: https://docs.google.com/spreadsheets/d/1HWSkkt0H6ZIaYyW5Bxj5GuXrdSHE-4qywptP44hW5og/edit?usp=sharing


## Web App
for details of web-app, see [EmoAppVer1](https://github.com/Kelvinthedrugger/-AI-/tree/main/EmoAppVer1) folder


## Model implementation
### VA-Regression model

<a target="_blank" id="bt" href="https://colab.research.google.com/github/Kelvinthedrugger/-AI-/blob/main/emo_nbs/EMOAI_EmotionLoopModel_DataProcess_Training.ipynb">
<!---the image--->
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
</a>

For original implementation, see [here](https://github.com/Kelvinthedrugger/-AI-/blob/main/emo_nbs/EMOAI_EmotionLoopModel_DataProcess_Training.ipynb)


### simplified examples
see [here](https://github.com/Kelvinthedrugger/-AI-/tree/main/emo_nbs/CODE_EXAMPLE_TO_PUSH)


## Model training Result
### Loss of EMO-AI 語意模型

![image](https://user-images.githubusercontent.com/59814445/189539001-33bec975-6dc7-4e6e-803b-d02e05ece0a5.png)


### EMO-AI 語意模型預測點投射至VA平面的結果

![image](https://user-images.githubusercontent.com/59814445/189539080-e1af906d-a6f6-4ae6-8e90-b88ef0e21d5d.png)


### EMO-AI 情緒遞迴模型訓練結果

![image](https://user-images.githubusercontent.com/59814445/189539091-53cdb4a7-d406-46d1-b483-5b8aa3118995.png)

![image](https://user-images.githubusercontent.com/59814445/189539097-4e4f66af-c083-4e2a-8851-2b70f6d63ddb.png)








