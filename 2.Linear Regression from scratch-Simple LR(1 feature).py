#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn import model_selection
import numpy as np
data=np.loadtxt('data.csv',delimiter=',')
x=data[:,0]
y=data[:,1]
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.3)

def fit(x_train,y_train):
    numerator=(x_train*y_train).mean()-x_train.mean()*y_train.mean()
    denominator=(x_train**2).mean()-x_train.mean()**2
    m=numerator/denominator
    c=y_train.mean()-m*x_train.mean()
    return m,c

def predict(x,m,c):
    return m*x+c

def score(y_true,y_predict):
    u=((y_true-y_predict)**2).sum()
    v=((y_true-y_true.mean())**2).sum()
    return 1-u/v

def cost(x,y,m,c):
    return ((y-(m*x+c))**2).mean()

m,c=fit(x_train,y_train)

#test data
y_test_predict=predict(x_test,m,c)
print('test score:',score(y_test,y_test_predict))

#train data
y_train_predict=predict(x_train,m,c)
print('train score:',score(y_train,y_train_predict))

#parameters
print("M,C:",m,c) 

#cost
print('cost on training data:',cost(x_train,y_train,m,c))

