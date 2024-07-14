import pandas as pd
import numpy as np
df = pd.read_csv('advertising.csv')
data = df.to_numpy ()
max = np.max(data[:, 3])
index = np.argmax(data[:, 3])
mean_tv = np.mean(data[:, 0])
count_sale_than_20 = (data[:, 3] >= 20).sum()
filtered_data = data[data[:, 3] >= 15]
radio_mean = np.mean(filtered_data[:, 1])
filtered_newspaper = data[data[:, 2] > np.mean(data[:, 2])]
sum_sales = np.sum(filtered_newspaper[:, 3])
print(sum_sales)