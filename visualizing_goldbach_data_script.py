import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("Goldbach_Conjecture_Data/df1.csv")
df2 = pd.read_csv("Goldbach_Conjecture_Data/df2.csv")
df3 = pd.read_csv("Goldbach_Conjecture_Data/df3.csv")
df4 = pd.read_csv("Goldbach_Conjecture_Data/df4.csv")
df5 = pd.read_csv("Goldbach_Conjecture_Data/df5.csv")
df6 = pd.read_csv("Goldbach_Conjecture_Data/df6.csv")
df7 = pd.read_csv("Goldbach_Conjecture_Data/df7.csv")
df8 = pd.read_csv("Goldbach_Conjecture_Data/df8.csv")
df9 = pd.read_csv("Goldbach_Conjecture_Data/df9.csv")
df10 = pd.read_csv("Goldbach_Conjecture_Data/df10.csv")
df11 = pd.read_csv("Goldbach_Conjecture_Data/df11.csv")
df12 = pd.read_csv("Goldbach_Conjecture_Data/df12.csv")
df13 = pd.read_csv("Goldbach_Conjecture_Data/df13.csv")
df14 = pd.read_csv("Goldbach_Conjecture_Data/df14.csv")
df15 = pd.read_csv("Goldbach_Conjecture_Data/df15.csv")
df16 = pd.read_csv("Goldbach_Conjecture_Data/df16.csv")
df17 = pd.read_csv("Goldbach_Conjecture_Data/df17.csv")

# Combine df1 to df17 into a single dataframe.

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17])
df = df[['even', 'goldbach_pair_count']].drop_duplicates().reset_index(drop=True)

# Generate the scatter plot which has the evens from 6 to 15000000 along the x-axis, and the Goldbach pair counts along
# the y-axis. The resulting scatter plot can be seen is found in visualizing_goldbach_data_graph_6_15000000.png.

fig = plt.figure(figsize=[15,8])
ax = fig.add_subplot()
sns.scatterplot(ax=ax, x="even", y="goldbach_pair_count", data=df, alpha=0.4)
ax.set_xlabel("Even", size=16)
ax.set_ylabel("Goldbach Pair Count", size=16)
ax.set_title( "Goldbach Pair Counts for Evens From 6 to 15000000", size=18)
plt.show()