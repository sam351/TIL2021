# TF-IDF로 텍스트를 벡터로 변환하는 모듈
from konlpy.tag import Okt
import pickle
import numpy as np

# 전역 변수 --- ( ※ 2)
word_dic = {'_id': 0} # 단어 사전
dt_dic = {} # 문장 전체에서의 단어 출현 횟수
files = [] # 문서들을 저장할 리스트

# KoNLPy의 Okt객체 초기화 ---- ( ※ 1)
okt = Okt()


def tokenize(text):
    '''KoNLPy로 형태소 분석하기''' # --- ( ※ 3) 
    word_s = okt.pos(text, norm=True, stem=True)
    result = [n for n, h in word_s if h in ('Noun', 'Verb ', 'Adjective')]
    return result


def words_to_ids(words, auto_add = True):
    ''' 단어를 ID로 변환하기 ''' # --- ( ※ 4)
    result = []
    for w in words:
        if w in word_dic:
            result.append(word_dic[w])
        elif auto_add:
            word_dic[w] = word_dic['_id']
            word_dic['_id'] += 1
            result.append(word_dic[w])
    return result


def add_text(text):
    '''텍스트를 ID 리스트로 변환해서 추가하기''' # --- (*5)
    ids = words_to_ids(tokenize(text), auto_add = True)
    files.append(ids)


def add_file(path):
    '''텍스트 파일을 학습 전용으로 추가하기''' # --- (*6)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        add_text(text)


def calc_files():
    '''추가한 파일 계산하기''' # --- (*7)
    global dt_dic
    result = []
    doc_count = len(files)
    dt_dic = {}
    
    # 단어 출현 횟수 세기 --- (*8)
    for words in files:
        used_word = {}
        data = np.zeros(word_dic['_id'])
        for id in words:
            data[id] += 1
            used_word[id] = 1
        
        # 단어 t가 사용되고 있을 경우 dt_dic의 수를 1 더하기 --- (*9)
        for id in used_word:
            if id not in dt_dic:
                dt_dic[id] = 0
            dt_dic[id] += 1
        
        # 정규화하기 --- (*10)
        data = data / len(words) 
        result.append(data)
    
    # TF-IDF 계산하기 --- (*11)
    for i, doc in enumerate(result):
        for id, v in enumerate(doc):
            idf = np.log(doc_count / dt_dic[id]) + 1
            doc[id] = min(doc[id]*idf, 1.0)
        result[i] = doc
    
    return result


def save_dic(fname):
    '''사전을 파일로 저장하기''' # --- (*12)
    pickle.dump([word_dic, dt_dic, files], open(fname, "wb"))


def load_dic(fname):
    '''사전 파일 읽어 들이기''' # --- (*13)
    global word_dic, dt_dic, files
    word_dic, dt_dic, files = pickle.load(open(fname, 'rb'))


def calc_text(text):
    ''' 문장을 벡터로 변환하기 ''' # --- ( ※ 14)
    data = np.zeros(word_dic['_id'])
    words = words_to_ids(tokenize(text), False)
    for w in words:
        data[w] += 1
    data = data / len(words)
    for id, v in enumerate(data):
        idf = np.log(len(files) / dt_dic[id]) + 1
        data[id] = min([data[id] * idf, 1.0])
    return data


# 모듈 테스트하기 --- ( ※ 15)
if __name__ == '__main__':
    print('>>> Running test code...\n')
    docs = ['비', '오늘은 비가 내렸어요.', '오늘은 더웠지만 오후부터 비가 내렸다.', '비가 내리는 일요일이다.']
    for doc in docs:
        add_text(doc)
    print(calc_files())
    print(word_dic)