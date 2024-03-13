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
        # print(self.data)
        sentences = self.data.flatten()
        sentences = np.append(sentences, data)
        # # sentences.insert(data)
        # print(f"sent: {sentences}")
        # print(f"sent shape : {sentences.shape}")

        tfidf = TfidfVectorizer()
        model = tfidf.fit_transform(sentences)
        cosine_similarities = cosine_similarity(model[-1], model)
        
        # print(f"cs = {cosine_similarities[-5:]}")
        # print(f"cs shape = {cosine_similarities.shape}")

        similarity_result = cosine_similarities.flatten()
        similarity_result.sort()
        print('nilai maks:',similarity_result[-2])
        print('nilai maks:',similarity_result[-3])
        print('nilai maks:',similarity_result[-4])

        idx = cosine_similarities.argsort()[0][-2]
        idx_2 = cosine_similarities.argsort()[0][-3]
        idx_3 = cosine_similarities.argsort()[0][-4]

        # print('idx:',idx)
        # print('idx_2:',idx_2)
        # print('idx_3:',idx_3)

        # print('ck:',sentences)
        # print('ck2:',sentences[idx_2])
        # print('ck3:',sentences[idx_3])

        # print('teks:',self.data[idx])
        # print('teks_2:',self.data[idx_2])
        # print('teks_3:',self.data[idx_3])

        # return f"{self.data[idx]}. {self.data[idx_2]}. {self.data[idx_3]}"
        return [idx, idx_2, idx_3]

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
