import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df1 = pd.read_csv('data/exploits_proxy_logs.csv')
df1['Type'] = "exploit"
df2 = pd.read_csv('data/benign_proxy_logs.csv')
df2['Type'] = "benign"
frame = [df1, df2]
df = pd.concat(frame)
print(df.head())

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

random_forest = RandomForestClassifier(n_estimators=30, max_depth=10, random_state=1)

random_forest.fit(X_train, y_train)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=10, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=30, n_jobs=1, oob_score=False, random_state=1,
            verbose=0, warm_start=False)



y_predict = random_forest.predict(X_test)
print accuracy_score(y_test, y_predict)


from sklearn.metrics import confusion_matrix

print pd.DataFrame(
    confusion_matrix(y_test, y_predict),
    columns=['Predicted Benign', 'Predicted Exploit'],
    index=['True Benign', 'True Exploit']
)

importances = random_forest.feature_importances_
importances = [x for x in importances if x != 0.0]
importances = np.array(importances)
#print importances
std = np.std([tree.feature_importances_ for tree in random_forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")



for f in range(len(importances)):
   print("%d. feature %s (%f)" % (f + 1, featureList[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(len(importances)), importances[indices],
       color="b", yerr=std[indices], align="center")
plt.xticks(range(len(importances)), featureList[indices], rotation=90)
plt.xlim([-1, len(importances)])
plt.show()
