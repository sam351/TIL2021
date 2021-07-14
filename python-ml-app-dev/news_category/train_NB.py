import pickle
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import numpy as np
from sklearn.naive_bayes import GaussianNB

# TF-IDF 데이터베이스 읽어 들이기 --- (*1)
data = pickle.load(open('source_output/news_category.pickle', 'rb'))
y_data, x_data = data

# 학습 전용과 테스트 전용으로 구분하기 --- (*2)
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)

# 나이브 베이즈로 학습하기 --- (*3)
model = GaussianNB()
model.fit(X_train, y_train)

# 평가하고 결과 출력하기 --- (*4)
y_pred = model.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred)
rep = metrics.classification_report(y_test, y_pred)

print('>>> 정답률 =', acc)
print('>>> 분류 성능표 :\n', rep)