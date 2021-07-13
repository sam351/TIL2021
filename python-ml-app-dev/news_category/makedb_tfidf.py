import os, glob, pickle
import tfidf
import sys

# 명령행 인자 검증
if len(sys.argv) not in [2, 3]:
    print('Incorrect number of arguments (requires 1 or 2 arguments)')
    sys.exit()
elif not os.path.isdir(sys.argv[1]):
    print('Incorrect argument (requires directory to corpus)')
    sys.exit()


# 전역 변수
x_data = []
y_data = []


# 디렉터리 내부의 파일 목록 불러와 데이터셋에 추가하기 --- (*1)
def read_files(path, label, n_limit=None):
    limit_str = '' if n_limit is None else f'(Limit to {n_limit} samples)'
    print(f">>> read_files from {path} {limit_str}")
    files = glob.glob(path + "/*.txt")[:n_limit]
    for f in files:
        if os.path.basename(f) == 'LICENSE.txt': continue
        tfidf.add_file(f)
        y_data.append(label)


# 기사를 넣은 디렉터리 읽어 들이기 --- ( ※ 2)
text_labels  = sorted(glob.glob(sys.argv[1]+'/*'))  # path to each label's directory
n_limit = int(sys.argv[2]) if len(sys.argv)==3 else None  # number of samples per class (limitation)
for idx, path in enumerate(text_labels):
    read_files(path=path, label=idx, n_limit=n_limit)

# TF-IDF 벡터로 변환하기 --- (*3)
x_data = tfidf.calc_files()

# 저장하기 --- (*4)
os.makedirs('source_output/', exist_ok=True)
pickle.dump([y_data, x_data], open('source_output/news_category.pickle', 'wb'))
tfidf.save_dic('source_output/news_category_tdidf.dic')
print('ok')