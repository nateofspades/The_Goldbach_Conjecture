import pandas as pd
import prime_functions as pf

# Below we generate the Goldbach pair counts for the evens from 6 to 15000000.
# The data is broken into multiple dataframes because there are many rows (~7.5 million total),
# which causes issues with Excel if we try to stuff everything into a single dataframe.

df1 = pf.goldbach_pair_counts_for_interval(6, 1000000)
df2 = pf.goldbach_pair_counts_for_interval(1000000, 2000000)
df3 = pf.goldbach_pair_counts_for_interval(2000000, 3000000)
df4 = pf.goldbach_pair_counts_for_interval(3000000, 4000000)
df5 = pf.goldbach_pair_counts_for_interval(4000000, 5000000)
df6 = pf.goldbach_pair_counts_for_interval(5000000, 6000000)
df7 = pf.goldbach_pair_counts_for_interval(6000000, 7000000)
df8 = pf.goldbach_pair_counts_for_interval(7000000, 8000000)
df9 = pf.goldbach_pair_counts_for_interval(8000000, 9000000)
df10 = pf.goldbach_pair_counts_for_interval(9000000, 10000000)
df11 = pf.goldbach_pair_counts_for_interval(10000000, 11000000)
df12 = pf.goldbach_pair_counts_for_interval(11000000, 12000000)
df13 = pf.goldbach_pair_counts_for_interval(12000000, 13000000)
df14 = pf.goldbach_pair_counts_for_interval(13000000, 13500000)
df15 = pf.goldbach_pair_counts_for_interval(13500000, 14000000)
df16 = pf.goldbach_pair_counts_for_interval(14000000, 14500000)
df17 = pf.goldbach_pair_counts_for_interval(14500000, 15000000)

# Save each dataframe to a .csv file. These .csv files are found in the Goldbach_Conjecture_Data folder.

df1.to_csv("df1.csv")
df2.to_csv("df2.csv")
df3.to_csv("df3.csv")
df4.to_csv("df4.csv")
df5.to_csv("df5.csv")
df6.to_csv("df6.csv")
df7.to_csv("df7.csv")
df8.to_csv("df8.csv")
df9.to_csv("df9.csv")
df10.to_csv("df10.csv")
df11.to_csv("df11.csv")
df12.to_csv("df12.csv")
df13.to_csv("df13.csv")
df14.to_csv("df14.csv")
df15.to_csv("df15.csv")
df16.to_csv("df16.csv")
df17.to_csv("df17.csv")