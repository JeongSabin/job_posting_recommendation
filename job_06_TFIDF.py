import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle
import glob

df = pd.DataFrame()
data_paths = glob.glob('./wanted/preprocessing_data/*')
data_paths = sorted(data_paths)
job_list = ['웹', '서버', '프론트엔드', '소프트웨어', '자바', '안드로이드', 'iOS', 'Nodejs', 'C++', '데이터엔지니어', 'DevOps', '파이썬', '시스템관리자', '머신러닝엔지니어',
                '데이터사이언티스트', '빅데이터엔지니어', 'QA', '기술지원', '개발매니저', '보안엔지니어', '프로덕트매니저', '블록체인엔지니어', 'PHP개발자', '임베디드개발자', '웹퍼블리셔',
                '크로스플랫폼', '하드웨어엔지니어', 'DBA', 'NET개발자', '영상음성엔지니어', 'CTO', '그래픽스엔지니어', 'VR엔지니어', 'BI 엔지니어', 'ERP전문가', '루비온레일즈개발자',
                'CIO']
cnt = 0
for path in data_paths:
    df_reviews = pd.read_csv(path)
    df_reviews.info()
    # nan 값 제거
    df_reviews.dropna(inplace=True)
    df_reviews.reset_index(inplace=True)
    df_reviews.info()
    Tfidf = TfidfVectorizer(sublinear_tf=True)
    Tfidf_matrix = Tfidf.fit_transform(df_reviews['first_cleaned_welfare'])
    print(Tfidf_matrix.shape)
    # (3182, 84461)
    print(Tfidf_matrix[0].shape)
    # (1, 84461)
    with open(f'./wanted/TFIDF_model_welfare/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_welfare.pickle', 'wb') as f:
        pickle.dump(Tfidf, f)

    mmwrite(f'./wanted/TFIDF_model_welfare/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_welfare.mtx', Tfidf_matrix)
    cnt += 1
cnt = 0
for path in data_paths:
    df_reviews = pd.read_csv(path)
    df_reviews.info()
    # nan 값 제거
    df_reviews.dropna(inplace=True)
    df_reviews.reset_index(inplace=True)
    df_reviews.info()
    Tfidf = TfidfVectorizer(sublinear_tf=True)
    Tfidf_matrix = Tfidf.fit_transform(df_reviews['first_cleaned_works'])
    print(Tfidf_matrix.shape)
    # (3182, 84461)
    print(Tfidf_matrix[0].shape)
    # (1, 84461)
    with open(f'./wanted/TFIDF_model_work/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_work.pickle',
              'wb') as f:
        pickle.dump(Tfidf, f)
    mmwrite(f'./wanted/TFIDF_model_work/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_work.mtx', Tfidf_matrix)
    cnt += 1