import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle
import glob

df = pd.DataFrame()
data_paths = glob.glob('./rec_sys_model/wanted/preprocessing_data/*')
data_paths = sorted(data_paths)
job_list = ['웹 개발자', '서버 개발자', '프론트엔드 개발자', '소프트웨어 엔지니어', '자바 개발자', '안드로이드 개발자', 'iOS 개발자', 'Node.js 개발자', 'C,C++ 개발자', '데이터 엔지니어', 'DevOps', '파이썬 개발자', '시스템,네트워크 관리자', '머신러닝 엔지니어',
                '데이터 사이언티스트', '빅데이터 엔지니어', 'QA,테스트 엔지니어', '기술지원', '개발 매니저', '보안 엔지니어', '프로덕트 매니저', '블록체인 플랫폼 엔지니어', 'PHP 개발자', '임베디드 개발자', '웹 퍼블리셔',
                '크로스플랫폼 앱 개발자', '하드웨어 엔지니어', 'DBA', 'NET 개발자', '영상,음성 엔지니어', 'CTO,Chief Technology Officer', '그래픽스 엔지니어', 'VR엔지니어', 'BI 엔지니어', 'ERP전문가', '루비온레일즈 개발자',
                'CIO,Chief Information Officer']
job_list = sorted(job_list)
print(job_list)
# exit()
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
    with open(f'./rec_sys_model/wanted/TFIDF_model_welfare/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_welfare.pickle', 'wb') as f:
        pickle.dump(Tfidf, f)

    mmwrite(f'./rec_sys_model/wanted/TFIDF_model_welfare/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_welfare.mtx', Tfidf_matrix)
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
    print(df_reviews['first_cleaned_works'])
    exit()
    print(Tfidf_matrix.shape)
    # (3182, 84461)
    print(Tfidf_matrix[0].shape)
    # (1, 84461)
    with open(f'./rec_sys_model/wanted/TFIDF_model_work/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_work.pickle',
              'wb') as f:
        pickle.dump(Tfidf, f)
    mmwrite(f'./rec_sys_model/wanted/TFIDF_model_work/{str(cnt).zfill(2)}_{job_list[cnt]}_Tfidf_wanted_work.mtx', Tfidf_matrix)
    cnt += 1