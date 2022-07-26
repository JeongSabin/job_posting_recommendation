import pandas as pd
from konlpy.tag import Okt
import re
# import nltk
# nltk.download("book", quiet=True)
import nltk
# nltk.download()
from nltk.tokenize import word_tokenize
import glob

df = pd.DataFrame()
data_paths = glob.glob('./wanted/clear/*')
data_paths = sorted(data_paths)
job_list = ['웹', '서버', '프론트엔드', '소프트웨어', '자바', '안드로이드', 'iOS', 'Nodejs', 'C++', '데이터엔지니어', 'DevOps', '파이썬', '시스템관리자', '머신러닝엔지니어',
                '데이터사이언티스트', '빅데이터엔지니어', 'QA', '기술지원', '개발매니저', '보안엔지니어', '프로덕트매니저', '블록체인엔지니어', 'PHP개발자', '임베디드개발자', '웹퍼블리셔',
                '크로스플랫폼', '하드웨어엔지니어', 'DBA', 'NET개발자', '영상음성엔지니어', 'CTO', '그래픽스엔지니어', 'VR엔지니어', 'BI 엔지니어', 'ERP전문가', '루비온레일즈개발자',
                'CIO']
cnt = 0
for path in data_paths:
    print(path)
    df = pd.read_csv(path)
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
        words = []
        for english in token2:
            if 1 < len(english) < 10:
                if english not in stopwords:
                    words.append(english)
        for word in df_token.word:
            if 1 < len(word) < 10 :
                if word not in stopwords :
                    words.append(word)
        cleaned_sentence = ' '.join(words)
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
        for english in token2:
            if 1 < len(english) < 10:
                if english not in stopwords:
                    words.append(english)
        for word in df_token.word:
            if 1 < len(word) < 10 :
                if word not in stopwords :
                    words.append(word)
        cleaned_sentence = ' '.join(words)
        first_cleaned_welfare.append(cleaned_sentence)
    first_cleaned_all = []
    for i in range(len(first_cleaned_welfare)):
        first_cleaned_all.append(first_cleaned_welfare[i] + first_cleaned_works[i])
    df['first_cleaned_all'] = first_cleaned_all
    # df['first_cleaned_welfares'] = first_cleaned_welfare
    df.dropna(inplace=True)

    df.to_csv(f'./wanted/clear_data/{job_list[cnt]}_data_preprocessing_02.csv', index=False)
    print(df)
    df.info()
    cnt += 1