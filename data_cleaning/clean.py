import pandas as pd


def isi_bumbu_kosong(df:pd.DataFrame)->pd.DataFrame:
    '''Mengisi fitur bumbu yang kosong dengan 'tanpa bumbu' '''
    df['bumbu'] = df['bumbu'].fillna('tanpa bumbu')
    return df

def drop_kosong(df:pd.DataFrame)->pd.DataFrame:
    '''menghapus row dengan data kosong'''
    df.dropna(inplace=True)
    return df

