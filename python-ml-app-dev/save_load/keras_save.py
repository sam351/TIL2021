import sklearn
from sklearn import datasets
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical

# sklearn : 0.22.2.post1, keras : 2.5.0
f'sklearn : {sklearn.__version__}, keras : {keras.__version__}'


# 붓꽃 데이터 읽어 들이기
iris = datasets.load_iris()
in_size = len(iris.feature_names)  # 4
nb_classes = len(iris.target_names)  # 3
x_data = iris.data
y_data = to_categorical(iris.target, nb_classes)  # one-hot encoding


# 모델 정의하기
model = Sequential([
    Dense(512, activation='relu', input_shape=(in_size,)),
    Dense(512, activation='relu'),
    Dropout(rate=0.2),
    Dense(nb_classes, activation='softmax')
])

# 컴파일하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
# model.summary()

# 학습 실행하기
model.fit(x_data, y_data, batch_size=20, epochs=50)

# 모델 저장하기
model.save('iris_model.h5')

# 학습 가중치 데이터 저장하기
model.save_weights('iris_weight.h5')