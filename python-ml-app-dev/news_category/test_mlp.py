import pickle, tfidf

from keras import optimizers
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.models import model_from_json


# 텍스트 준비하기 --- ( ※ 1)
text1 = """
대통령이 북한과 관련된 이야기로 한미 정상회담을 준비하고 있습니다.
"""
text2 = """
iPhone과 iPad를 모두 가지고 다니므로 USB를 2개 연결할 수 있는 휴대용 배터리를 선호합니다.
"""
text3 = """
이번 주에는 미세먼지가 많을 것으로 예상되므로 노약자는 외출을 자제하는 것이 좋습니다.
"""

# TF-IDF 사전 읽어 들이기 --- (*2)
tfidf.load_dic('source_output/news_category_tdidf.dic')

# Keras 모델 정의하고 가중치 데이터 읽어 들이기 --- (*3)
n_classes = 4  # 분류할 레이블 수
model = Sequential([
    Dense(512, activation='relu', input_shape=(14806,)),
    Dropout(0.2),
    Dense(512, activation='relu'),
    Dropout(0.2),
    Dense(n_classes, activation='softmax'),
])
model.compile(
    optimizer=RMSprop(),
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)
model.load_weights('source_output/news_category_model_weights.hdf5')

# 텍스트 지정해서 판별하기 --- (*4)
def check_genre(text):
    # 레이블 정의하기
    LABELS = ["정치", "경제", "생활 ", "IT/과학"]

    # TF-IDF 벡터로 변환하기 -- (*5)
    data = tfidf.calc_text(text)

    # MLP로 예측하기 --- (*6)
    pred = model.predict(np.array([data]))[0]
    n = pred.argmax()

    print(f'>>> {LABELS[n]} ({pred[n]})')
    return LABELS[n], float(pred[n]), int(n)


if __name__ == '__main__':
    for tmp_txt in [text1, text2, text3]:
        check_genre(tmp_txt)