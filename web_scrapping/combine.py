import pandas as pd
from pprint import pprint

def combine():
    '''menggabungkan header dan detail'''
    detail1 = pd.read_csv("data\data_detail.csv")
    # detail1.drop("Unnamed: 0", axis=1, inplace=True)
    detail1.drop("link", axis=1, inplace=True)

    detail2 = pd.read_csv("data\data_detail2.csv")
    # detail2.drop("Unnamed: 0", axis=1, inplace=True)
    detail2.drop("link", axis=1, inplace=True)
    detail2['Unnamed: 0'] = detail2['Unnamed: 0'] +1000

    detail3 = pd.read_csv("data\data_detail3.csv")
    # detail3.drop("Unnamed: 0", axis=1, inplace=True)
    detail3.drop("link", axis=1, inplace=True)
    detail3['Unnamed: 0'] = detail3['Unnamed: 0'] +2000

    detail4 = pd.read_csv("data\data_detail4.csv")
    # detail4.drop("Unnamed: 0", axis=1, inplace=True)
    detail4.drop("link", axis=1, inplace=True)
    detail4['Unnamed: 0'] = detail4['Unnamed: 0'] +3000

    detail5 = pd.read_csv("data\data_detail5.csv")
    # detail5.drop("Unnamed: 0", axis=1, inplace=True)
    detail5.drop("link", axis=1, inplace=True)
    detail5['Unnamed: 0'] = detail5['Unnamed: 0'] +4000

    frames = [detail1, detail2, detail3, detail4, detail5]
    
    details = pd.concat(frames)
    # print(details.shape)

    header = pd.read_csv("data\data_awal.csv")
    # header.drop("Unnamed: 0", axis=1, inplace=True)

    df = pd.merge(header, details, on="Unnamed: 0", how="left")
    # pprint(df.head())
    # print(df.shape)
    # print(df.info())
    # pprint(df.tail())

    df.to_csv("data\data_combine.csv")
