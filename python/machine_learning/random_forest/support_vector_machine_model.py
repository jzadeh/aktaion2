import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.svm import SVC

#df1 = pd.read_csv('data/exploit.csv')
# df2 = pd.read_csv('data/benign.csv')
df1 = pd.read_csv('data/logs_normalized_format/exploit_bro_timing_microbehaviors.csv')
df1['Type'] = "exploit"
df2 = pd.read_csv('data/logs_normalized_format/benign_bro_timing_microbehaviors.csv')
df2['Type'] = "benign"

frame = [df1, df2]
df = pd.concat(frame)


X = df

for column in df.columns:
    if df[column].dtype == type(object):
        le = LabelEncoder()

        df[column] = le.fit_transform(df[column])

nanColumns = df.columns[df.isnull().any()].tolist()

for nanColumn in nanColumns:
    df = df.drop(nanColumn, axis = 1)

featureList = []
X = df.drop('Type', axis=1)
for feature in X:
    featureList.append(feature)

featureList = np.array(featureList)
y = df['Type']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(X_train, y_train)
SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)


y_predict = clf.predict(X_test)
print accuracy_score(y_test, y_predict)



