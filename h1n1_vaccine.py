# -*- coding: utf-8 -*-
"""h1n1_vaccine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uevNNG-TLqez0tRRP6_N-sOJh_4Iz1IK
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/Datasets/main/h1n1_vaccine_prediction.csv")

df.head()

df.shape

df.describe()

df.info()

df.isnull().sum()

df.dtypes

sns.countplot(x="employment",data=df)

pd.crosstab(df["employment"],df["sex"])

sns.countplot(x="h1n1_vaccine",hue="sex",data=df)

sns.boxplot(x="h1n1_vaccine",y="no_of_children",data=df)

df.isnull().sum()

df.drop("has_health_insur",axis=1,inplace=True)

df.dropna(inplace=True)

df.shape

df=pd.get_dummies(df,columns=["sex","no_of_adults","no_of_children"])

df.head()

df.isnull().sum()

df=df.drop(["unique_id","age_bracket","qualification","race","income_level","marital_status","housing_status","employment","census_msa"],axis=1)

df.info()

x=df.drop("h1n1_vaccine",axis=1)
y=df["h1n1_vaccine"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=1)

model=LogisticRegression()

model.fit(x_train,y_train)

model.score(x_train,y_train)

model.score(x_test,y_test)

df.shape

predictions=model.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictions)

from sklearn import metrics

cm=metrics.confusion_matrix(y_test,predictions,labels=[1,0])
df_cm=pd.DataFrame(cm,index=[i for i in ["1", "0"]],
                   columns=[i for i in [" Predict 1", "Predict 0"]])
plt.figure(figsize=(7,5))
sns.heatmap(df_cm,annot=True,fmt="g")

print(metrics.classification_report(y_test,predictions))

from sklearn.tree import DecisionTreeClassifier

model2=DecisionTreeClassifier()

model2.fit(x_train,y_train)

model2.score(x_train,y_train)

model2.score(x_test,y_test)

model3=DecisionTreeClassifier(max_depth=5,criterion="entropy")

model3.fit(x_train,y_train)

model3.score(x_train,y_train)

model3.score(x_test,y_test)

from sklearn.ensemble import BaggingClassifier

model4=BaggingClassifier(n_estimators=100,base_estimator=model3)

model4.fit(x_train,y_train)

model4.score(x_train,y_train)

model4.score(x_test,y_test)

from sklearn.ensemble import GradientBoostingClassifier

model6=GradientBoostingClassifier()

model6.fit(x_train,y_train)

model6.score(x_train,y_train)

model6.score(x_test,y_test)

from sklearn.ensemble import RandomForestClassifier

model7=RandomForestClassifier()

model7.fit(x_train,y_train)

model7.score(x_train,y_train)

model7.score(x_test,y_test)

from sklearn.svm import SVC

model8=SVC()

model8.fit(x_train,y_train)

model8.score(x_train,y_train)

model8.score(x_test,y_test)