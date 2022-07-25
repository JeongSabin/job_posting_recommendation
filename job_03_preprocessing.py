import pandas as pd
from konlpy.tag import Okt
import re
# import nltk
# nltk.download("book", quiet=True)
import nltk
# nltk.download()
from nltk.tokenize import word_tokenize

df = pd.read_csv('./wanted/clear_data/All_clear_data.csv')
df.info()


okt = Okt()
df_stopwords = pd.read_csv('./stopwords.csv')
stopwords = list(df_stopwords['stopword'])
stopwords = stopwords + []


# count = 0
first_cleaned_works = []
first_cleaned_welfare = []

for work in df.work:
    # count += 1
    # if count % 10 == 0 :
    #     print('.', end='')
    # if count % 100 == 0 :
    #     print()

    work = re.sub('[^가-힣a-zA-Z ]', ' ', work)
    #review = review.split()
    token = okt.pos(work, stem=True)

    # 영어 단어 단위 토크나이징
    sentence = work
    token2 = word_tokenize(sentence)

    df_token = pd.DataFrame(token, columns=['word', 'class'])  #튜플형태 >> 컬럼 두개짜리 데이터프레임 으로 변환
    df_token = df_token[(df_token['class']=='Noun') | (df_token['class']=='Verb') | (df_token['class']=='Adjective') | (df_token['class']=='Adverb')]
    print(df_token)
    print(token2)
    # exit()

    words =[]
    for word in df_token.word:
        if 1 < len(word) < 10 :
            if word not in stopwords :
                words.append(word)
    cleaned_sentence = ' '.join(words + token2)
    first_cleaned_works.append(cleaned_sentence)
    # first_cleaned_works.append(token2)

for welfare in df.welfare:
    # count += 1
    # if count % 10 == 0 :
    #     print('.', end='')
    # if count % 100 == 0 :
    #     print()

    review = re.sub('[^가-힣a-zA-Z ]', ' ', welfare)
    #review = review.split()
    token = okt.pos(welfare, stem=True)

    # 영어 단어 단위 토크나이징
    sentence = work
    token2 = word_tokenize(sentence)

    df_token = pd.DataFrame(token, columns=['word', 'class'])  #튜플형태 >> 컬럼 두개짜리 데이터프레임 으로 변환
    df_token = df_token[(df_token['class']=='Noun') | (df_token['class']=='Verb') | (df_token['class']=='Adjective') | (df_token['class']=='Adverb')]
    print(df_token)
    # exit()

    words =[]
    for word in df_token.word:
        if 1 < len(word) < 10 :
            if word not in stopwords :
                words.append(word)
    cleaned_sentence = ' '.join(words + token2)
    first_cleaned_welfare.append(cleaned_sentence)
first_cleaned_all = []
for i in range(len(first_cleaned_welfare)):
    first_cleaned_all.append(first_cleaned_welfare[i] + first_cleaned_works[i])
df['first_cleaned_all'] = first_cleaned_all
# df['first_cleaned_welfares'] = first_cleaned_welfare
df.dropna(inplace=True)

df.to_csv('./wanted/clear_data/wanted_data_preprocessing_all.csv', index=False)
print(df)
df.info()