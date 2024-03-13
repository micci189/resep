import sqlite3
import pandas as pd

class Query:
    def __init__(self, db:str)->None:
        self.conn = sqlite3.connect(db)

    def get_data(self, ingd:list)->pd.DataFrame:
        filter = ""
        for i in range(len(ingd)):
            if i == 0:
                filter += f'bahan like \'% ' + ingd[i] + ' %\''
            else:
                filter += f' and bahan like \'% ' + ingd[i] + ' %\''

        sql = f"select judul, bahan, bumbu, metode from recipe where {filter}"
        df = pd.read_sql_query(sql, self.conn)
        # print(filter)
        # print(sql)
        # print(df)

        return df