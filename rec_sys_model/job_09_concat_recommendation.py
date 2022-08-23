import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# 추천 받기 함수
def getRecommendation(cosin_sim):
    simScore = list(enumerate(cosin_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:16]
    movieIdx = [i[0] for i in simScore]
    recMovieList = df.iloc[movieIdx, 2]
    return recMovieList
            # 머신러닝엔지니어[https://www.wanted.co.kr/wd/53925]
df_reviews = pd.read_csv('./rec_sys_model/wanted/clear_data/13_머신러닝엔지니어_data_scaler.csv')
user_data = ['https://www.wanted.co.kr/wd/75640', 'https://www.wanted.co.kr/wd/114692', 'https://www.wanted.co.kr/wd/56091', 'https://www.wanted.co.kr/wd/109068', 'https://www.wanted.co.kr/wd/111447']
df_머신러닝엔지니어 = pd.read_csv('./rec_sys_model/wanted/clear_data/13_머신러닝엔지니어_data_scaler.csv')
df_데이터사이언티스트 = pd.read_csv('./rec_sys_model/wanted/clear_data/14_데이터사이언티스트_data_scaler.csv')
df_빅데이터엔지니어 = pd.read_csv('./rec_sys_model/wanted/clear_data/15_빅데이터엔지니어_data_scaler.csv')


df_머신러닝엔지니어.dropna(inplace=True)
df_머신러닝엔지니어.reset_index(inplace=True)

df_데이터사이언티스트.dropna(inplace=True)
df_데이터사이언티스트.reset_index(inplace=True)

df_빅데이터엔지니어.dropna(inplace=True)
df_빅데이터엔지니어.reset_index(inplace=True)

data_DB = [df_머신러닝엔지니어, df_빅데이터엔지니어, df_데이터사이언티스트]

df = pd.DataFrame()
for path in data_DB:
    df = pd.concat([df, path], ignore_index=True)
df.drop_duplicates(['page_url'], inplace=True)

df_mark = pd.DataFrame()
for path in user_data:
    data_ = df[df['page_url']==path]
    print(data_)
    df_mark = pd.concat([df_mark, data_], ignore_index=True)
df_mark.drop_duplicates(inplace=True)
print(df)
print(df_mark['first_cleaned_welfare'])

Tfidf_welfare = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix_welfare = Tfidf_welfare.fit_transform(df['first_cleaned_welfare'])

Tfidf_work = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix_work = Tfidf_work.fit_transform(df['first_cleaned_works'])
print(Tfidf_matrix_welfare)
print(Tfidf_matrix_work)

print(df['first_cleaned_works'])

df_one = pd.DataFrame()
texts_welfare = ''
for title in df_mark['first_cleaned_welfare']:
    texts_welfare += ' '
    texts_welfare += title

texts_work = ''
for title in df_mark['first_cleaned_works']:
    texts_work += ' '
    texts_work += title
print(type([texts_work]))
df_one['first_cleaned_welfare'] = [texts_welfare]
df_one['first_cleaned_work'] = [texts_work]

# fit_transform 이 아닌 transform 을 위에서 만든 Tfidf 모델을 사용해 vector화 시키기
welfare_vector = Tfidf_welfare.transform(df_one['first_cleaned_welfare'])
work_vector = Tfidf_work.transform(df_one['first_cleaned_work'])


cosine_sim1 = linear_kernel(welfare_vector, Tfidf_matrix_welfare)
cosine_sim2 = linear_kernel(work_vector, Tfidf_matrix_work)


cosine_sim = cosine_sim1 * 0.25 + cosine_sim2 * 0.6 + np.array(df['scaler_money'], np.float) * 0.15

recommendation = getRecommendation(cosine_sim)
print(recommendation[6:16])