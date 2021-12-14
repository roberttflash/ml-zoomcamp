import pandas as pd
import numpy as np
from numpy import loadtxt

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score

# data preparation

df = pd.read_csv('php0iVrYT.csv')

df.columns = ['recency', 'frequency', 'total_donated', 'months_since_beginning', 'class']

df['class'] = np.where(df['class'] == 2, 1, 0)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1212)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1212)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = (df_full_train['class'] == 1).astype('int').values
y_train = (df_train['class'] == 1).astype('int').values
y_val = (df_val['class'] == 1).astype('int').values
y_test = (df_test['class'] == 1).astype('int').values



del df_val['class']
del df_train['class']
del df_test['class']
del df_full_train['class']


# training

def train (df, y, w=10):
    cat = df.to_dict(orient = 'records')

    dv = DictVectorizer(sparse=False)
    X = dv.fit_transform(cat)

    model = XGBClassifier(max_depth=None, min_child_weight=w)
    model.fit(X, y)

    return dv, model


def predict(df, dv, model):
    cat = df.to_dict(orient = 'records')

    dv = DictVectorizer(sparse=False)
    X = dv.fit_transform(cat)

    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# Training the final model


##del df_full_train['class']
##del df_train['class']
##del df_test['class']

dv, model = train(df_full_train, y_full_train, 10)
y_pred = predict(df_test, dv, model)

auc = roc_auc_score(y_test, y_pred)
print('auc = %.3f' % auc)

