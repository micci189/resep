from nltk import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
import pandas as pd
import numpy as np

class SearchData:
    def __init__(self, tp, data):
        # self.dataset_path = config.get('PATH_DATASET')
        self.tp = tp
        self.data = data[['bahan']].to_numpy()
        # self.raw_file = open(f'{self.dataset_path}/bpjs.txt', 'r', errors='ignore', encoding='utf-8')
        # paragraph = self.raw_file.read()
        # self.sent_tokens = sent_tokenize(paragraph)
        # self.word_tokens = word_tokenize(paragraph)

    def cosine_similarity(self, data:str):
        print("mulai cosine similarity services")
        
        sentences = self.data.flatten()
        sentences = np.append(sentences, data)

        tfidf = TfidfVectorizer()
        model = tfidf.fit_transform(sentences)
        cosine_similarities = cosine_similarity(model[-1], model)

        similarity_result = cosine_similarities.flatten()
        similarity_result.sort()
        # print('nilai maks:',similarity_result[-2])
        # print('nilai maks:',similarity_result[-3])
        # print('nilai maks:',similarity_result[-4])

        # idx = cosine_similarities.argsort()[0][-2]
        # idx_2 = cosine_similarities.argsort()[0][-3]
        # idx_3 = cosine_similarities.argsort()[0][-4]

        print('nilai maks:',similarity_result[-2])
        idx = cosine_similarities.argsort()[0][-2]

        if len(sentences) == 3: # 2 row data query + 1 row data input = 3 row
            print('nilai maks:',similarity_result[-3])
            idx_2 = cosine_similarities.argsort()[0][-3]
            return [idx, idx_2]
        elif len(sentences) > 3:
            print('nilai maks:',similarity_result[-3])
            print('nilai maks:',similarity_result[-4])
            idx_2 = cosine_similarities.argsort()[0][-3]
            idx_3 = cosine_similarities.argsort()[0][-4]
            return [idx, idx_2, idx_3]

        return [idx]

    def clean_text(self, data:str):
        result = self.tp.case_folding(data)
        result = self.tp.hapus_stopword(result)
        # result = self.tp.lemmatisasi(result)

        return result
    
    def query_ingredient(self, ingredient:list):
        '''connect to database to get data by ingredients'''
        connection = sqlite3.connect("recipe.db")
        cursor = connection.cursor()

        df = pd.read_sql_query("select judul, bahan from recipe where bahan like '% ayam %' and bahan like '% kentang %' and bahan like '% jamur %'", connection)
