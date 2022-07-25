import pandas as pd
from gensim.models import Word2Vec

review_word = pd.read_csv('./wanted/clear_data/wanted_data_preprocessing_all.csv')
review_word.info()

cleaned_token_sentence = list(review_word['first_cleaned_all'])
print(cleaned_token_sentence[0])

cleaned_tokens = []
for sentence in cleaned_token_sentence:
    token = sentence.split()
    cleaned_tokens.append(token)
print(cleaned_tokens[0])

embedding_model = Word2Vec(cleaned_tokens, vector_size=100,
                           window=4, min_count=20,
                           workers=8, epochs=100, sg=1)
embedding_model.save('./wanted/model/post_rec_model.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))

