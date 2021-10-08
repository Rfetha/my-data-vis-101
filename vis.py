import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("sales_data.csv")


sales['Unit_Cost'].plot(kind="box", vert=False, figsize=(14,6))
plt.show()

sales["Age_Group"].value_counts().plot(kind="pie", figsize=(6,6))
plt.show()

ax = sales["Age_Group"].value_counts().plot(kind="bar", figsize=(14,6))
ax.set_ylabel("Number Of Sales")
plt.show()


corr = sales.corr()

fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap="RdBu", fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation="vertical")
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()


sales.plot(kind="scatter", x="Customer_Age", y="Revenue", figsize=(6,6))
plt.show()

sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))
plt.show()

ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Profit')
plt.show()
