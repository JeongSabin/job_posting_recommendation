import pandas as pd
from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
import glob

df = pd.DataFrame()
data_paths = glob.glob('./rec_sys_model/wanted/clear/*')
data_paths = sorted(data_paths)
job_list = ['웹', '서버', '프론트엔드', '소프트웨어', '자바', '안드로이드', 'iOS', 'Nodejs', 'C++', '데이터엔지니어', '파이썬', 'DevOps', '시스템관리자', '머신러닝엔지니어',
                '데이터사이언티스트', '빅데이터엔지니어', 'QA', '기술지원', '개발매니저', '보안엔지니어', '프로덕트매니저', '블록체인엔지니어', 'PHP개발자', '임베디드개발자', '웹퍼블리셔',
                '하드웨어엔지니어', '크로스플랫폼', 'DBA', 'NET개발자', '영상음성엔지니어', '그래픽스엔지니어', 'CTO', 'VR엔지니어', 'BI엔지니어', 'ERP전문가', '루비온레일즈개발자',
                'CIO']
cnt = 0
for path in data_paths[:10]:
    print(path)
    df = pd.read_csv(path)
    df.info()

    okt = Okt()
    df_stopwords = pd.read_csv('stopwords.csv')
    stopwords = list(df_stopwords['stopword'])
    stopwords = stopwords + ['지원', '운영', '직책', '근무', '가다', '조직', '제도', '입사', '제공', '개발', '서비스', '출퇴근', '그룹',
                             '단체', '해요', '업무에요', '경우', '직원', '통해', '업무', '구성원', '활용', '프로그램', '진행', '인재', '수행',
                             '지급', '관련', '사내', '제품', '퇴근', '보장', '선택', '직원', '사용', '면접', '활용', '따름', '가능', '개월',
                             '근무', '최근', '사무실', '기반', '부서', '해드리다', '드리다', '기업', 'IT', '회사', '채용', '동료', '본사', '베이스',
                             '제도', '모든', '필요하다', '사용', '협의', '이내', '법인', '전원', '본인', '또는', '현재', '서비스', '활동', '기술',
                             '갈다', '코딩', '따르다', '급여', '대다', '관리', '맞다', '관련', '무조건', '위치', '참여', '문화', '쓰다', '이면', '처리',
                             '통한', '포함', '최종', '근로', '합격', '기본', '담당', '만원', '환경', '오늘', '올해', '내년', '조직', '높다', '상승', '어떠하다',
                             '운용', '원하다', '이렇다', '정규직', '총괄', '적극', '떠나다', '사업', '사옥', '나누다', '넘다', '허다', '의하다', '괜찮다', '보지',
                             '고민', '결과', '가능하다', '참고', '패스트', '미팅', 'on', 'and', 'of', 'to', 'the', 'our', 'with', 'in', 'we', 'are', 'nbt',
                             'publ', 'to', '인터뷰', '반환', '슈퍼', '서류', '제출', '사이', '제너', '만들다', '경우', '없이', '기능', '되어다', '피플러', '내다', '전사',
                             '출근', '수립', '관계자', '고객', '부여', '호선', '합류', '확실하다', '모범', '사례', '센티', '시차', '사항', '안내', '룰루', '전형',
                             '최종', '절차', '비다', '열심히', '인간', '어떻다', '추다']


# count = 0
    first_cleaned_works = []
    first_cleaned_welfare = []

    for work in df.work:
        # count += 1
        # if count % 10 == 0 :
        #     print('.', end='')
        # if count % 100 == 0 :
        #     print()

        work1 = re.sub('[^가-힣 ]', ' ', work)
        work2 = re.sub('[^a-zA-Z ]', ' ', work)

        # review = review.split()
        token = okt.pos(work1, stem=True)

        # 영어 단어 단위 토크나이징
        sentence = work2
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

        welfare1 = re.sub('[^가-힣 ]', ' ', welfare)
        welfare2 = re.sub('[^a-zA-Z ]', ' ', welfare)
        # review = review.split()
        token = okt.pos(welfare1, stem=True)

        # 영어 단어 단위 토크나이징
        sentence = welfare2
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
    # first_cleaned_all = []
    # for i in range(len(first_cleaned_welfare)):
    #     first_cleaned_all.append(first_cleaned_welfare[i] + first_cleaned_works[i])
    df['first_cleaned_welfare'] = first_cleaned_welfare
    df['first_cleaned_works'] = first_cleaned_works
    # df['first_cleaned_welfares'] = first_cleaned_welfare
    df.dropna(inplace=True)
    df.to_csv(f'./rec_sys_model/wanted/preprocessing_data/{str(cnt).zfill(2)}_{job_list[cnt]}_preprocessing_01.csv', index=False)
    print(df)
    df.info()
    cnt += 1