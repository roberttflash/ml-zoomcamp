import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score

# data preparation

df = pd.read_csv('dataset_31_credit-g.csv', decimal=',')


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=10)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=10)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = (df_train['class'] == 'bad').astype('int').values
y_val = (df_val['class'] == 'bad').astype('int').values



del df_val['class']



# training

def train (df, y, d, s):
    cat = df.to_dict(orient = 'records')

    dv = DictVectorizer(sparse=False)
    X = dv.fit_transform(cat)

    model = DecisionTreeClassifier(max_depth=d, min_samples_leaf=s)
    model.fit(X, y)

    return dv, model


def predict(df, dv, model):
    cat = df.to_dict(orient = 'records')

    X = dv.fit_transform(cat)

    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# Training the final model
y_train = (df_train['class'] == 'bad').astype('int').values
y_test = (df_test['class'] == 'bad').astype('int').values

del df_full_train['class']
del df_train['class']
del df_test['class']

dv, model = train(df_train, y_train, 10, 10)
y_pred = predict(df_test, dv, model)

auc = roc_auc_score(y_test, y_pred)
print('auc = %.3f' % auc)

