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
from django.shortcuts import render
from .models import *
import os

def cosin_sim_calculation(category, url):
    # 절대경로 변경
    df_reviews = pd.DataFrame(list(post.objects.filter(category=category).values()))
    Tfidf_matrix1 = mmread(f'D:/work/python/AI_exam_asia2204/job_posting_recommendation9/rec_sys_model/wanted/TFIDF_model_welfare/{category}.mtx').tocsr()
    Tfidf_matrix2 = mmread(f'D:/work/python/AI_exam_asia2204/job_posting_recommendation9/rec_sys_model/wanted/TFIDF_model_work/{category}.mtx').tocsr()
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
    recommendation = recommendation[1:7]
    return recommendation