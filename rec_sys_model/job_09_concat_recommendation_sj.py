import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle
from konlpy.tag import Okt
import re
from gensim.models import Word2Vec
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import glob

def getRecommendation(cosin_sim):
    simScore = list(enumerate(cosin_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:11]
    movieIdx = [i[0] for i in simScore]
    recMovieList = df.iloc[movieIdx, 2]
    return recMovieList

            # 머신러닝엔지니어[https://www.wanted.co.kr/wd/53925]
df_reviews = pd.read_csv('./wanted/clear_data/13_머신러닝엔지니어_data_scaler.csv')
user_data = ['https://www.wanted.co.kr/wd/75640', 'https://www.wanted.co.kr/wd/114692', 'https://www.wanted.co.kr/wd/56091', 'https://www.wanted.co.kr/wd/109068', 'https://www.wanted.co.kr/wd/111447']
df_머신러닝엔지니어 = pd.read_csv('./wanted/clear_data/13_머신러닝엔지니어_data_scaler.csv')
df_데이터사이언티스트 = pd.read_csv('./wanted/clear_data/14_데이터사이언티스트_data_scaler.csv')
df_빅데이터엔지니어 = pd.read_csv('./wanted/clear_data/15_빅데이터엔지니어_data_scaler.csv')


df_머신러닝엔지니어.dropna(inplace=True)
df_머신러닝엔지니어.reset_index(inplace=True)

df_데이터사이언티스트.dropna(inplace=True)
df_데이터사이언티스트.reset_index(inplace=True)

df_빅데이터엔지니어.dropna(inplace=True)
df_빅데이터엔지니어.reset_index(inplace=True)

data_DB = [df_머신러닝엔지니어, df_빅데이터엔지니어, df_데이터사이언티스트]
print(1)
df = pd.DataFrame()
for path in data_DB:
    df = pd.concat([df, path], ignore_index=True)
df.drop_duplicates(['page_url'], inplace=True)

df_mark = pd.DataFrame()
for path in user_data:
    data_ = df[df['page_url'] == path]
    print(data_)
    df_mark = pd.concat([df_mark, data_], ignore_index=True)
df_mark.drop_duplicates(inplace=True)
print(2)
one_post_welfare = []
one_post_work = []

for title1 in df_mark['first_cleaned_welfare'] :
    post1 = df_mark[df_mark['first_cleaned_welfare'] != title1]
    one_sentence_welfare = ' '.join(post1['first_cleaned_welfare'])
    # one_sentence_welfare = ''.join(title1)
    one_post_welfare.append(one_sentence_welfare)
for title2 in df_mark['first_cleaned_works'] :
    post2 = df_mark[df_mark['first_cleaned_works'] != title2]
    one_sentence_work = ' '.join(post2['first_cleaned_works'])
    # one_sentence_work = ''.join(title2)
    one_post_work.append(one_sentence_work)
# 'category' : df_mark['category'].unique(),'page_url' : df_mark['page_url'].unique(),
# 'picture_url' : df_mark['picture_url'].unique(),'title' : df_mark['title'].unique(),
# 'company' : df_mark['company'].unique(),'work' : df_mark['work'].unique(),
# 'qualification' : df_mark['qualification'].unique(),'favor' : df_mark['favor'].unique(),
# 'welfare' : df_mark['welfare'].unique(),'skill_stack' : df_mark['skill_stack'].unique(),
# 'place' : df_mark['place'].unique(),'money' : df_mark['money'].unique(),
#  'employee' : df_mark['employee'].unique(),'scaler_money' : df_mark['scaler_money'].unique()

df_one_post = pd.DataFrame({'page_url' : df_mark['page_url'].unique(),
                            'first_cleaned_welfare' : one_post_welfare, 'first_cleaned_works' : one_post_work})
df_one_post.to_csv('./test.csv', index=False)
print(df_one_post)

Tfidf_welfare = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix_welfare = Tfidf_welfare.fit_transform(df['first_cleaned_welfare'])

Tfidf_work = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix_work = Tfidf_work.fit_transform(df['first_cleaned_works'])
print(Tfidf_matrix_welfare)

Tfidf = TfidfVectorizer(sublinear_tf=True)

Tfidf_matrix_mk_welfare = Tfidf.fit_transform(df_one_post['first_cleaned_welfare'])
Tfidf_matrix_mk_work = Tfidf.fit_transform(df_one_post['first_cleaned_works'])

print(Tfidf_matrix_mk_work)
print(Tfidf_matrix_mk_welfare)
print(3)
# job_idx = df_reviews[df_reviews['page_url']=='https://www.wanted.co.kr/wd/111367'].index[0]
job_idx_welfare = (df_one_post['first_cleaned_welfare']).index[0]
job_idx_work = (df_one_post['first_cleaned_works']).index[0]

print(Tfidf_matrix_mk_welfare)
print(Tfidf_matrix_work)

cosine_sim1 = linear_kernel(Tfidf_matrix_mk_welfare[job_idx_welfare], Tfidf_matrix_welfare)
cosine_sim2 = linear_kernel(Tfidf_matrix_mk_work[job_idx_work], Tfidf_matrix_work)
print(4)
cosine_sim = cosine_sim1 * 0.25 + cosine_sim2 * 0.6 + np.array(df['scaler_money'], np.float) * 0.15

recommendation = getRecommendation(cosine_sim)
print(recommendation[1:11])