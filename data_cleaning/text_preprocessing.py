import re, string

from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.stopword import StopWord

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


class TextProcessing:
    def __init__(self) -> None:
        pass
        # self.stopword_en = stopwords.words("english")
        # self.stopword_id = StopWord.get_stopword()
        # self.dataset_path = config["PATH_DATASET"]
    
    def case_folding(self, text:str)->str:
        '''fungsi yang digunakan untuk membersihkan teks'''

        result = text.lower()
        result = re.sub(r'\d+', '', result)
        result = re.sub(r'@[A-Za-z0-9]+', '', result)
        # result = re.sub(r'https?:\/\/\w+.\w+', '', result)
        result = result.translate(str.maketrans('','',string.punctuation))
        result = result.strip()
        result = re.sub(r'  ',' ',result)

        return result
    
    def tokenisasi(self, text:str,mode:str='word')->list:
        '''fungsi yang digunakan untuk tokenisasi teks
        fungsi ini mempunyai dua mode
        word : melakukan token kata
        sentence : melakukan token kalimat 
        '''

        result = None

        if mode == 'word':
            token_ = PhraseTokenizer()
            result = token_.tokenize(text)
        elif mode == 'sentence':
            result = sent_tokenize(text)

        return result
    
    def lemmatisasi(self, text:str)->str:
        '''fungsi yang digunakan untuk lemmatisasi teks'''

        lemmatizer = Lemmatizer()
        result = lemmatizer.lemmatize(text)
        return result
    
    def hapus_stopword(self, text:str)->str:
        '''fungsi yang digunakan untuk menghapus stopword dari teks'''

        stopword = StopWord()
        result = stopword.remove_stopword(text)

        return result

    def camelcase(self, list_words):  
        converted = ", ".join(word[0].upper() + word[1:].lower() for word in list_words)  
        return converted 

    # def clean_text(self, data:str, ):
    #     result = self.tp.case_folding(data)
    #     result = self.tp.hapus_stopword(result)
    #     # result = self.tp.lemmatisasi(result)

    #     return result
    
    

        
