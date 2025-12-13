import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

url = r"https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"


names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(url,names=names)
#print(df)

#EDA

X = df.iloc[:,:-1]
Y=df.loc[:,['class']]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print("shape of x_train",x_train.shape)
print("shape of y_train",y_train.shape)
print("shape of x_test",x_test.shape)
print("shape of y_test",y_test.shape)


lg=LogisticRegression()
lg.fit(x_train,y_train)
result = lg.score(x_test,y_test)
#print(result)
joblib.dump(lg, 'Project/model.pkl')
print('model is saved')
y_pred = lg.predict(x_test)
