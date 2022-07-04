# AUTOGENERATED! DO NOT EDIT! File to edit: 01_modelAPI.ipynb (unless otherwise specified).

__all__ = ['test', 'fetch', 'get_train_set', 'mish', 'Mish', 'EmoModel', 'get_pretrained_model']

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


# Cell
# the robertA model (example from the author)
import torch
from torch import nn
from typing import List
import torch.nn.functional as F
from transformers import DistilBertTokenizer, AutoTokenizer, AutoModelWithLMHead, DistilBertForSequenceClassification, AdamW, get_linear_schedule_with_warmup
import logging
import os
from functools import lru_cache
from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
import pytorch_lightning as pl
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from argparse import Namespace
from sklearn.metrics import classification_report
# torch.__version__

# Cell
# from https://github.com/digantamisra98/Mish/blob/b5f006660ac0b4c46e2c6958ad0301d7f9c59651/Mish/Torch/mish.py
@torch.jit.script
def mish(input):
    return input * torch.tanh(F.softplus(input))

class Mish(nn.Module):
    def forward(self, input):
        return mish(input)

# Cell
class EmoModel(nn.Module):
    def __init__(self, base_model, n_classes, base_model_output_size=768, dropout=0.05):
        super().__init__()
        self.base_model = base_model

        self.classifier = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(base_model_output_size, base_model_output_size),
            Mish(),
            nn.Dropout(dropout),
            nn.Linear(base_model_output_size, n_classes)
        )

        for layer in self.classifier:
            if isinstance(layer, nn.Linear):
                layer.weight.data.normal_(mean=0.0, std=0.02)
                if layer.bias is not None:
                    layer.bias.data.zero_()

    def forward(self, input_, *args):
        X, attention_mask = input_
        hidden_states = self.base_model(X, attention_mask=attention_mask)

        # maybe do some pooling / RNNs... go crazy here!

        # use the <s> representation
        return self.classifier(hidden_states[0][:, 0, :])

# Cell
def get_pretrained_model(PATH):
    if PATH[-3:] != ".pt" and PATH[-4:] != ".pth":
        print("Unable to load pretrained model")
        return None

    # model = EmoModel(AutoModelWithLMHead.from_pretrained("distilroberta-base").base_model, len(emotions))
    # see above cell: emotions = ["sadness", "joy", "love", "anger", "fear", "surprise"]
    model = EmoModel(AutoModelWithLMHead.from_pretrained("distilroberta-base").base_model, 6)
    # lr: learning rate, adjustable
    optimizer = AdamW(model.parameters(), lr=0.0001)

    checkpoint = torch.load(PATH)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    model.eval() # or model.train()
    return model