import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmread
from .models import *

def Make_Tfidf_model(category_lst, post_list):
    def getRecommendation(cosin_sim, category_lst):
        df_reviews = pd.DataFrame(list(post.objects.filter(category__in=category_lst).values()) )
        simScore = list(enumerate(cosin_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
        simScore = simScore[:16]
        movieIdx = [i[0] for i in simScore]
        recMovieList = df_reviews.iloc[movieIdx, 0]
        return recMovieList
    concat_df = pd.DataFrame()
    for i in category_lst:
        this_df = pd.read_csv(f'/Library/work/python/job_posting_recommendation_git/rec_sys_model/wanted/web_using_data/{i}.csv')
        concat_df = pd.concat([concat_df, this_df], ignore_index=True)
    concat_df.drop_duplicates(['page_url'], inplace=True)
    bookmark_df = pd.DataFrame()
    for i in post_list:
        data_ = concat_df[concat_df['page_url'] == i.page_url]
        bookmark_df = pd.concat([data_, bookmark_df], ignore_index=True)
    bookmark_df.drop_duplicates(inplace=True)

    Tfidf_welfare = TfidfVectorizer(sublinear_tf=True)
    Tfidf_matrix_welfare = Tfidf_welfare.fit_transform(concat_df['first_cleaned_welfare'])
    Tfidf_work = TfidfVectorizer(sublinear_tf=True)
    Tfidf_matrix_work = Tfidf_work.fit_transform(concat_df['first_cleaned_works'])

    df_one = pd.DataFrame()
    texts_welfare = ''
    for title in bookmark_df['first_cleaned_welfare']:
        texts_welfare += ' '
        texts_welfare += title

    texts_work = ''
    for title in bookmark_df['first_cleaned_works']:
        texts_work += ' '
        texts_work += title
    df_one['first_cleaned_welfare'] = [texts_welfare]
    df_one['first_cleaned_work'] = [texts_work]

    welfare_vector = Tfidf_welfare.transform(df_one['first_cleaned_welfare'])
    work_vector = Tfidf_work.transform(df_one['first_cleaned_work'])

    cosine_sim1 = linear_kernel(welfare_vector, Tfidf_matrix_welfare)
    cosine_sim2 = linear_kernel(work_vector, Tfidf_matrix_work)

    cosine_sim = cosine_sim1 * 0.25 + cosine_sim2 * 0.6 + np.array(concat_df['scaler_money'], np.float) * 0.15
    recommendation = getRecommendation(cosine_sim, category_lst)
    recommendation = recommendation[6:]
    return recommendation
def cosin_sim_calculation(category, url):
    # 절대경로 변경
    df_reviews = pd.DataFrame(list(post.objects.filter(category=category).values()))
    Tfidf_matrix1 = mmread(f'/Library/work/python/job_posting_recommendation_git/rec_sys_model/wanted/TFIDF_model_welfare_/{category}_Tfidf_wanted_welfare.mtx').tocsr()
    Tfidf_matrix2 = mmread(f'/Library/work/python/job_posting_recommendation_git/rec_sys_model/wanted/TFIDF_model_work_/{category}_Tfidf_wanted_work.mtx').tocsr()
    job_idx = df_reviews[df_reviews['page_url'] == url].index[0]
    cosine_sim1 = linear_kernel(Tfidf_matrix1[job_idx], Tfidf_matrix1)
    cosine_sim2 = linear_kernel(Tfidf_matrix2[job_idx], Tfidf_matrix2)
    cosine_sim = cosine_sim1 * 0.25 + cosine_sim2 * 0.6 + np.array(df_reviews['scaler_money'], np.float) * 0.15
    return cosine_sim

def getRecommendation(category, cosin_sim):
    df_reviews = pd.DataFrame(list(post.objects.filter(category=category).values()))

    simScore = list(enumerate(cosin_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:11]
    postIdx = [i[0] for i in simScore]
    recPostList = df_reviews.iloc[postIdx, 0]
    return recPostList

def recommendation_(category, cosine_sim):
    recommendation = getRecommendation(category, cosine_sim)
    recommendation = recommendation[1:]
    return recommendation