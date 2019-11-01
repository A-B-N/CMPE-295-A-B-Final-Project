# reference: http://uc-r.github.io/creating-text-features

import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords, words

### GENERATING BAG OF WORDS ###
tokenizer = RegexpTokenizer(r'\w+')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
english_words = set(words.words())

reviews_df = pd.read_csv("reviews.csv", index_col=0)
all_reviews = reviews_df['Review Text']
all_tokens = list()

for review in all_reviews:
    review_tokens = tokenizer.tokenize(str(review))
    for token in review_tokens:
        if token.isalpha() and token.lower() not in stop_words and token.lower() in english_words:
            all_tokens.append(token.lower())

unique_tokens_and_count = {}
for token in all_tokens:
    token = ps.stem(token)
    if token in unique_tokens_and_count:
        unique_tokens_and_count[token] += 1
    else:
        unique_tokens_and_count[token] = 1

unique_tokens_and_count = dict(filter(lambda elem: elem[1] > 10, unique_tokens_and_count.items()))
unique_tokens = sorted(unique_tokens_and_count.keys(), key=lambda x: x[0])

# print(unique_tokens)
# print(len(unique_tokens))

bow_features = pd.DataFrame(columns=(['Clothing ID'] + unique_tokens))
row = 0

for review in all_reviews:
    bow_features = bow_features.append({'Clothing ID': reviews_df.iloc[row, 1]}, ignore_index=True)
    review_tokens = tokenizer.tokenize(str(review))
    tokens_list = {}
    for token in review_tokens:
        if token.isalpha() and token.lower() not in stop_words and token.lower() in english_words:
            token = ps.stem(token)
            if token in tokens_list:
                tokens_list[token] += 1
            else:
                tokens_list[token] = 1
    for token in tokens_list:
        bow_features = bow_features.append({token: tokens_list[token]}, ignore_index=True)
    row += 1

bow_features = bow_features.replace(np.nan, 0)

print(bow_features)








