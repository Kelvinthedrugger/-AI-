# -AI-
Let's go MOFO! HARD HARD HARD

This github repo is mostly about the codes that we used in the competition
not really available to general public (it's our business secret LOL)


Notion: https://www.notion.so/AI-_Database-5f3828b51a004e8aa5ef67f2e4190a0e


### twitter_sentiment_kaggle.zip

Due to it's large size ( > 50 Mb, over the recommended size of git), if there's an problem, 

a. fetch the local storage
b. just visit the source (see notion)


### plurk dataset

It now works!

To fetch newest data, just run

'''python
# inside Plurk folder
from plurk import *
content = fetch_emoji(emoji='your emoji')
for ele in content: print(ele)
"For more info, see Plurk folder"
'''


### twitter dataset

I'm considering training a model from existing dataset (like, in this repo).
And fetch some posts from the web just to show that our product has the ability to do so.

## progress

Training officially provided model done: see Readme in emo_ds && notebook in emo_nbs
Fetch from twitter: not even started
Now working on: model backend (to communicate w/ frontend: get user input, etc)



