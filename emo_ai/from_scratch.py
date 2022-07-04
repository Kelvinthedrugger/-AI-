# AUTOGENERATED! DO NOT EDIT! File to edit: 00_model_api_wout_dependency.ipynb (unless otherwise specified).

__all__ = ['test', 'fetch', 'get_train_set']

# Cell
def test():
    print("success")

# Cell
# read the file w/out unzip it
"""by GeoHotz"""

# this works but not so much for parser() # since we're doing language, not image
def fetch(name,dataset_name='emotional.zip'):
    import hashlib
    import os
    # generate encrypted file name to avoid collision ?
    fp = os.path.join(os.getcwd(), hashlib.md5(
        name.encode('utf-8')).hexdigest())
    dat = None
    if os.path.isfile(fp):
        with open(fp, "rb") as f:
            dat = f.read()
    else:
        import tempfile
        from zipfile import ZipFile
        # dat = requests.get(url).content
        with ZipFile(dataset_name) as zip:
            with zip.open("%s.csv" % name, mode='r') as f:
                dat = f.read()
        # important trick here to create a .tmp file
        with open(fp+".tmp", "wb") as f:
            f.write(dat)
        os.rename(fp+".tmp", fp)

    return dat



# Cell
import csv
import numpy as np
import os
import pandas as pd # to process csv files more conveniently

# Cell
# use pandas to process training.csv here

# Cell
# we should abandon this and just use pandas instead ?
def get_train_set():
    with open("training.csv", 'r') as f:
        cnt = 0
        for line in f:
            print(line, type(line), line.rstrip(','))
            cnt += 1
            if cnt == 2:
                break
    return True
