from sklearn.preprocessing import StandardScaler, MinMaxScaler, QuantileTransformer
import pandas as pd
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
    print(path)
    df = pd.read_csv(path)
    df.info()

    df['money'].replace(['없음'],[0],inplace=True)
    df['money'] = df['money'].astype('int')
    df.info()

    minmaxscaler = MinMaxScaler()
    df_money = df[['money']]
    scaler_money = minmaxscaler.fit_transform(df_money)
    print(scaler_money)
    df['scaler_money'] = scaler_money
    df.to_csv(f'./wanted/clear_data/{str(cnt).zfill(2)}_{job_list[cnt]}_data_scaler.csv', index=False)
    cnt += 1