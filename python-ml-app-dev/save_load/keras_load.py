import sklearn
from sklearn import datasets
import keras
from keras.models import load_model
from keras.utils.np_utils import to_categorical

# sklearn : 0.22.2.post1, keras : 2.5.0
f'sklearn : {sklearn.__version__}, keras : {keras.__version__}'


# 붓꽃 데이터 읽어 들이기
iris = datasets.load_iris()
in_size = len(iris.feature_names)  # 4
nb_classes = len(iris.target_names)  # 3
x_data = iris.data
y_data = to_categorical(iris.target, nb_classes)  # one-hot encoding


# 모델 읽어 들이기
model = load_model('iris_model.h5')

# 가중치 데이터 읽어 들이기
model.load_weights('iris_weight.h5')

# 모델 평가하기
score = model.evaluate(x_data, y_data, verbose=1)
for name, val in zip(model.metrics_names, score):
  print(f">>>{name:>5} = {val:.4f}")