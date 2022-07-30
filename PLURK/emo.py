import os
from plurk_oauth import PlurkAPI
from pathlib import Path
from acc import *
APIfile = Path(os.getcwd() + "/API.keys")
assert os.path.isfile(APIfile), "shxt, something wrong with (one of) the tokens\nmost likely expired"

# this works
plurk = PlurkAPI.fromfile(APIfile)
print(plurk.callAPI('/APP/Profile/getOwnProfile'))

# without access token
#plurk = PlurkAPI(CONSUMER_KEY, CONSUMER_SECRET)
# 需要驗證碼, shxt
#plurk.authorize()

