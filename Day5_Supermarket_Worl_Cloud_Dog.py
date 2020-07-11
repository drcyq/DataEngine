# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:38:40 2020

@author: DongRunchao
"""

from wordcloud import WordCloud, ImageColorGenerator
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize


# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    cut_text = word_tokenize(f)
    cut_text = " ".join(cut_text)
	#print(cut_text)
    mask = np.array(Image.open("dog.png"))
    wc = WordCloud(mask = mask, max_words = 100, width = 2000, height = 2000, background_color = "Black")
    wordcloud = wc.generate(cut_text)
    image_color = ImageColorGenerator(mask)
    wc.recolor(color_func = image_color)
    wordcloud.to_file("SupermarketWorldCloud.jpg")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv',header=None)
transactions=[]
for i in range(0,data.shape[0]):
    temp=[]
    for j in range(0,20):
        item=str(data.values[i,j])
        if item !='nan':
            temp.append(item)
    transactions.append(temp)

# 生成词云
all_word=''.join('%s' %item for item in transactions)
create_word_cloud(all_word)