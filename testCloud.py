#! /usr/bin/python3
# Author:Zzf
# -*- coding = utf-8 -*-
# @Time :2021/4/1 21:57
# @File :testCloud.py
# @Software :PyCharm
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3
conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql = 'select cname from movie250'
data =cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
conn.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
img = Image.open(r'.\static\assets\img\tree.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color = 'white',
    mask = img_array,
    font_path = "msyh.ttc"
)
wc.generate_from_text(string)
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
# plt.show()
plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)
