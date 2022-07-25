import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./wanted/clear_data/wanted_data_preprocessing_all.csv')
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['page_url'])
print(Tfidf_matrix.shape)
# (3182, 84461)
print(Tfidf_matrix[0].shape)
# (1, 84461)
with open('./wanted/model/Tfidf_wanted.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

mmwrite('./wanted/model/Tfidf_wanted.mtx', Tfidf_matrix)