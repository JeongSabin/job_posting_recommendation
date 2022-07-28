import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread
import pickle
from konlpy.tag import Okt
import re
from gensim.models import Word2Vec
import numpy as np

def getRecommendation(cosin_sim):
    simScore = list(enumerate(cosin_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:11]
    movieIdx = [i[0] for i in simScore]
    recMovieList = df_reviews.iloc[movieIdx, 2]
    return recMovieList


df_reviews = pd.read_csv('./wanted/clear_data/13_머신러닝엔지니어_data_scaler.csv')
df_reviews.dropna(inplace=True)
df_reviews.reset_index(inplace=True)
Tfidf_matrix1 = mmread('./wanted/TFIDF_model_work/13_머신러닝엔지니어_Tfidf_wanted_work.mtx').tocsr()
Tfidf_matrix2 = mmread('./wanted/TFIDF_model_welfare/13_머신러닝엔지니어_Tfidf_wanted_welfare.mtx').tocsr()
with open('./wanted/TFIDF_model_work/13_머신러닝엔지니어_Tfidf_wanted_work.pickle', 'rb') as f:
    Tfidf1 = pickle.load(f)
with open('./wanted/TFIDF_model_welfare/13_머신러닝엔지니어_Tfidf_wanted_welfare.pickle', 'rb') as g:
    Tfidf2 = pickle.load(g)

# 게임 제목 / index를 이용
job_idx = df_reviews[df_reviews['page_url']=='https://www.wanted.co.kr/wd/111367'].index[0] # gameidx = 1003

cosine_sim1 = linear_kernel(Tfidf_matrix1[job_idx], Tfidf_matrix1)
cosine_sim2 = linear_kernel(Tfidf_matrix2[job_idx], Tfidf_matrix2)
print(type(cosine_sim1))
print(type(cosine_sim2))
print(type(np.array(df_reviews['money'])))
cosine_sim = cosine_sim1 * 0.25 + cosine_sim2 * 0.6 + np.array(df_reviews['scaler_money'], np.float) * 0.15
recommendation = getRecommendation(cosine_sim)
print(recommendation[1:11])

# keyword 이용
# embedding_model = Word2Vec.load('./Google_play_models/word2vec_google_play_reviews_2.model')
# keyword = '배틀그라운드'
# sim_word = embedding_model.wv.most_similar(keyword, topn=10)
# words = [keyword]
# for word, _ in sim_word:
#     words.append(word)
# sentence = []
# count = 10
# for word in words:
#     sentence = sentence + [word] * count
#     count -= 1
# sentence = ' '.join(sentence)
# sentence_vec = Tfidf.transform([sentence])
# cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)
# recommendation = getRecommendation(cosine_sim)
# print(recommendation)

# 문장 이용
# okt = Okt()
# sentence = '화려한 액션과 소름 돋는 반전이 있는 영화'
# review = re.sub('[^가-힣 ]', ' ', sentence)
# #
# token = okt.pos(review, stem=True)
# #
# df_token = pd.DataFrame(token, columns=['word', 'class'])
# df_token = df_token[(df_token['class'] == 'Noun') |
#                     (df_token['class'] == 'Verb') |
#                     (df_token['class'] == 'Adjective')]
# words = []
# for word in df_token.word:
#     if 1 < len(word):
#         words.append(word)
# cleaned_sentence = ' '.join(words)
# print(cleaned_sentence)
# sentence_vec = Tfidf.transform([cleaned_sentence])
# cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)
# recommendation = getRecommendation(cosine_sim)
# print(recommendation)