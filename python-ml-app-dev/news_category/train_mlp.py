import pickle
from keras import optimizers
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt

# 분류할 레이블 수 --- (*1)
n_classes = 4

# TF-IDF 데이터베이스 읽어 들이기 --- (*2)
data = pickle.load(open('source_output/news_category.pickle', 'rb'))
y_data, x_data = data

# 레이블 데이터를 One-hot 형식으로 변환하기 --- (*3)
y_data = keras.utils.to_categorical(y_data, num_classes=n_classes)
in_shape = x_data[0].shape

# 학습 전용과 테스트 전용으로 구분하기 --- (*4)
X_train, X_test, y_train, y_test = train_test_split(
    np.array(x_data), np.array(y_data), test_size=0.2
)

# MLP모델의 구조 정의하기 --- (*5)
model = Sequential([
    Dense(512, activation='relu', input_shape=in_shape),
    Dropout(0.2),
    Dense(512, activation='relu'),
    Dropout(0.2),
    Dense(n_classes, activation='softmax'),
])

# 모델 컴파일하기 --- (*6)
model.compile(optimizer=RMSprop(),
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 학습 실행하기 --- (*7)
hist = model.fit(X_train, y_train, 
                 batch_size=128, epochs=20,
                 verbose=1, validation_data=(X_test, y_test))

# 평가하고 결과 출력하기 --- (*8)
score = model.evaluate(X_test, y_test, verbose=1)
print(f'>>> 정답률 = {score[1]:.4f}')
print(f'>>> loss = {score[0]:.4f}')

# 가중치데이터 저장하기 --- (*9)
model.save_weights('source_output/news_category_model_weights.hdf5')

# 학습 상태를 그래프로 그리기 --- (*10)
learning_curve_dir = 'source_output/train_mlp_learning_curve.png'
plt.plot(hist.history['accuracy'], label='train')
plt.plot(hist.history['val_accuracy'], label='test')
plt.title('Accuracy')
plt.legend(loc='upper left')
plt.savefig(learning_curve_dir, dpi=300)
print(f'>>> Successfully saved learning curve to {learning_curve_dir}')