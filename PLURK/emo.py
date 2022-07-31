
from acc import *

def main(use_file=False):
    from plurk_oauth import PlurkAPI

    if use_file:
        import os
        from pathlib import Path
        APIfile = Path(os.getcwd() + "/API.keys")
        assert os.path.isfile(APIfile), "shxt, something wrong with (one of) the tokens\nmost likely expired"
        # this works
        #plurk = PlurkAPI.fromfile(APIfile)
        print(plurk.callAPI('/APP/Profile/getOwnProfile'))

    else:
        plurk = PlurkAPI(acc_info["CONSUMER_KEY"], acc_info["CONSUMER_SECRET"])
        plurk = PlurkAPI(acc_info["API_KEY"], acc_info["API_SECRET"])
        print(plurk.callAPI('/APP/Profile/getOwnProfile'))
        print(plurk.callAPI('/APP/Timeline/getPlurk',options={"plurk_id": 16675741}))


if __name__ == "__main__":
    main()
