import pandas as pd
from pprint import pprint
import sqlite3
from sqlalchemy import create_engine

from web_scrapping import web_scrapping
from web_scrapping import web_scrapping_dtl
from web_scrapping import combine

from data_cleaning import clean
from data_cleaning import text_preprocessing

'''get data by web scrapping'''
# web_scrapping.scrap_head(251)
# web_scrapping_dtl.scrap_dtl(0,1000,'data_detail.csv') # 0-999
# web_scrapping_dtl.scrap_dtl(1000,2000,'data_detail2.csv') # 1000-1999
# web_scrapping_dtl.scrap_dtl(2000,3000,'data_detail3.csv') # 2000-2999
# web_scrapping_dtl.scrap_dtl(3000,4000,'data_detail4.csv') # 3000-3999
# web_scrapping_dtl.scrap_dtl(4000,5000,'data_detail5.csv') # 3000-4999
# combine.combine()

'''read data'''
# df = pd.read_csv("data\data_combine.csv")
# df.drop("Unnamed: 0.1", axis=1, inplace=True)
# df.drop("Unnamed: 0", axis=1, inplace=True)

'''clean data'''
# clean.isi_bumbu_kosong(df)
# clean.drop_kosong(df)

# pprint(df.head())
# print(df.shape)
# print(df.info())



'''insert data to database'''
# engine = create_engine('sqlite:///recipe.db', echo=False)
# df.to_sql('recipe', con=engine, if_exists='append')
# df.to_sql('recipe', con=engine, if_exists='replace')

'''connect to database'''
# connection = sqlite3.connect("recipe.db")
# cursor = connection.cursor()

'''check column name'''
# print(cursor.execute("select * from pragma_table_info('recipe') as tblInfo;").fetchall())

'''check table name'''
# print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())

'''query ambil data dari db by ingredients'''
# df2 = pd.read_sql_query("select judul, bahan from recipe where bahan like '% ayam %' and bahan like '% kentang %' and bahan like '% jamur %'", connection)
# print(df2.head())
# print(df2.shape)

'''check isi stopword'''
# from nlp_id.stopword import StopWord

# stopword = StopWord()
# print(stopword.get_stopword())