import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv('Sepsis1.csv')

X1=data[['Respiratory','Heartrate','Wbc','Temp']]
X2=data[['Urine','Spo','Respiratory','Heartrate','Wbc','Temp']]
X3=data

a=[]
for i in range(len(X1)):
    if X1['Respiratory'][i]>20 and X1['Heartrate'][i]>90 and X1['Wbc'][i]<4 or X1['Wbc'][i]>12 and X1['Temp'][i]<36 or X1['Temp'][i]>38.3:
        a.append('Sepsis')
    else:
        a.append('Normal')
X1['Class']=a

b=[]
for i in range(len(X2)):
    if X2['Urine'][i]>0.5 and (X2['Heartrate'][i]>94 and X2['Heartrate'][i]<98) or (X2['Heartrate'][i]>88 and X2['Heartrate'][i]<92):
        b.append('Severe Sepsis')
    else:
        b.append('Normal')
X2['Class']=b

c=[]
for i in range(len(X3)):
    if X3['Blood'][i]<90 and X3['Lactate'][i]<2 and X3['Urine'][i]<.5 and X3['Glucose'][i]>7.7 and X3['Creatin'][i]>1.7 and X3['Bilirubin'][i]> and X3['Inr'][i]>1.5 and X3['Platelets'][i]<10:
        c.append('Severe Sepsis')
    else:
        c.append('Normal')
X3['Class']=c
