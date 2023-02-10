import pandas as pd

df = pd.read_csv('all_wires.csv')
# print(df)

data = df.sort_values('Провод')
# print(data)

data.to_csv('all_wires_sort_by_name.csv', index=False)
