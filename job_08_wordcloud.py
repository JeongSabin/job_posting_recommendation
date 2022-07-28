from turtle import back
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./wanted/preprocessing_data/13_머신러닝엔지니어_preprocessing_01.csv')
words = df[df['page_url']=='https://www.wanted.co.kr/wd/111367']['first_cleaned_welfare']
# words = df[df['page_url']=='https://www.wanted.co.kr/wd/111367']['first_cleaned_works']
print(words.iloc[0])
words = words.iloc[0].split()
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

wordcloud_img = WordCloud(
    background_color='white', max_words=2000,
    font_path='AppleGothic').generate_from_frequencies(worddict)

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()