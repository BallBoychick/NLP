import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from pymorphy3 import MorphAnalyzer
from nltk.corpus import stopwords
import numpy as np
import torch.nn as nn
from sklearn.model_selection import train_test_split
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader
import matplotlib.pyplot as plt

stopwords = stopwords.words('russian')
# ch = 2

# def rem_html(s):
#     s += 1
#     return s


# def token(s):
#     s += 2
#     return s

# def lemm(s):
#     s += 3
#     return s

# general_mass = {
#     "rem" : rem_html,
#     "tok" : token,
#     "lemm" : lemm
# }

# # print(general_mass["rem"](ch))
# list_m = ["rem", "tok"]
# def prepro(list_m, ch):
#     prep_list = ch
#     for i in list_m:
#         prep_list = general_mass[i](prep_list)

#     return prep_list

# print(prepro(list_m=list_m, ch=ch))

df = pd.read_csv('./data/Petitions.csv')
df.drop(columns="id", inplace=True)
new_df = df.sample(5)
X = new_df["public_petition_text"].to_list()
# print(X)

def remove_html(text): 
    html_tag=re.compile('<.*?>')
    text_no_html = html_tag.sub('', text)
    return text_no_html

def remove_quots(text):
    text_only_letters = re.sub('[^\w\s]', '', text)
    return text_only_letters

general_mass = {
    "rem_html" : remove_html,
    "remove_quots" : remove_quots
}

list_m = ["rem_html", "remove_quots"]

text = ['<img>Я ?люблю !кошек', 'I love& music']
ls = []
pr_t = []
prep_text = text
for i in list_m:
    for j in text:
        prep_text = general_mass[i](j)
        pr_t.append(prep_text)
    text = pr_t
    pr_t = []
print(text)
# def prepro(list_m, text):
#     pl = []
#     prep_list = text
#     for i in list_m:
#         for j in text:
#             print(i)
#             print("Before", j)
#             prep_list = general_mass[i](j)
#             print("after", j)
#             pl.append(prep_list)
#     return pl

# print(prepro(list_m=list_m, text=X))
