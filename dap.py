# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_8IBupFew7jyOVrIhQacjIq8BTlRxJ8p
"""

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
x=np.zeros((3,3),dtype=int)
print(x)
y=np.ones((2,2),dtype=int)
print(y)
arange_arr=np.arange(10)
print(arange_arr)
reshape_arr=arr.reshape(5,1)
print(reshape_arr)
sliced_arr=arr[2:4]
print(sliced_arr)

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
c=np.vstack(arr1+arr2)
print(c)

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
d=np.stack(arr1+arr2)
print(d)

a=np.array([1,2,3,4])
a=np.split(a,2)
print(a)

arr1=np.array([1,2,3,4,5])
a=arr1+3
print(a)
arr2=np.array([5,4,3,2,1])
print(arr2)
result=arr1+arr2
print(result)

a=np.array([[1,2,3,4],[5,6,7,8,]])
b =a.T
print(b)

m1=np.array(([1,2],[3,4]))
m2=np.array(([5,6],[7,8]))
result=np.dot(m1,m2)
print(result)
d=np.linalg.eig(result)
print(d)

import numpy as np
a=np.array([[2,4,6],[1,3,5]])
b=np.sum(a)
print(b)

a=np.array([1,2,3,4,5])
b=np.mean(a)
c=np.median(a)
d=np.var(a)
e=np.std(a)
print(a)
print(b)
print(c)
print(d)
print(e)

data=np.loadtxt("/content/note.txt",dtype=int)
g=np.savetxt("/content/data.txt",data)
print(data)
print(g)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5])
plt.plot(a)

import pandas as pd
a=['Aakhil','Swarjan','Umesh','Mukesh','Prasad','Umar','Purna']
r=pd.Series(a,index=[94,56,66,78,81,59,92])
print(r)

d=pd.read_csv("/content/food_prices_watch.csv")
print(d)

d=pd.read_csv("/content/ai.txt",sep=" ")
print(d)

d=pd.read_excel("/content/p1.xlsx")
print(d)

d=pd.read_excel("/content/p1.xlsx",sheet_name=1)
print(d.loc[1:4])

import pandas as pd
d=pd.read_csv("/content/food_prices_watch.csv")
a=d.head(5)
b=d.tail(5)
c=pd.concat([a,b], axis=0)
c.to_csv("Aakhil.csv")

d.head(5)



d.tail(5)

from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
runs = np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='orange')
plt.title('INDvsAUS_Score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
tigar=np.linspace(-2*np.pi, 2*np.pi,100)
print(tigar)
plt.plot(tigar, np.sin(tigar) ,color='red')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='MI')
plt.plot(overs_a,runs_a,color='red',label='RCB')
plt.legend(loc='best')
plt.show()

import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
pt_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
pt_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,pt_a,color='hotpink',linewidth='3',label='CompanyA',marker='>',ms='15',mec='k')
plt.subplot(2,1,1)
plt.plot(years,pt_b,color='black',linestyle='dotted',label='CompanyB',marker='H')
plt.show()

a = np.array([25, 60, 5, 10])
labels = ["AIML", "Python", "Pandas", "Numpy"]
c=['pink','blue','purple','grey']
explode = [0.2, 0, 0, 0]
plt.pie(a, labels=labels,colors=c, explode=explode, startangle=180, textprops={'fontsize': 14})
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel("/content/Book 5.xlsx")
print(df)
print("Average of temperature")
mv=df['temperature'].mean()
print(mv)
print("Highest temperature")
x=df['temperature'].max()
y= df.loc[df['temperature'].idxmax(), 'date']
print(x ,"on", y)
print("Lowest temperature")
a=df['temperature'].min()
b=df.loc[df['temperature'].idxmin(), 'date']
print(a ,"on" ,b)
threshold=32
print("Temperature above a given threshold of",threshold)
ab=(df['temperature'] > threshold).sum()
print(ab)
plt.plot(df['date'],df['temperature'],color='black',marker='o',linewidth='2')
plt.xlabel("date")
plt.ylabel("temperature")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data = tips)
plt.title("Scatter plot of total bill vs tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.ylabel("Tip ($)")
plt.show

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.violinplot(x="day",y="total_bill",data=tips)
plt.title("Distribution of  Total Bill by day")
plt.xlabel("Day of the week")
plt.ylabel("Total Bills")
plt.show()
tips.head(20)

iris =sns.load_dataset("iris")
corrleation_martix=iris.corr()
sns.heatmap(corrleation_martix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of iris dataset")
plt.show()
print(iris)

iris =sns.load_dataset("titanic")
corrleation_martix=iris.corr()
sns.heatmap(corrleation_martix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of iris dataset")
plt.show()
print(titanic)

