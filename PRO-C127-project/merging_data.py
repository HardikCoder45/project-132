import pandas as pd

brown_dwarfs = pd.read_csv('./new_scraped_data.csv')
stars = pd.read_csv('./scraped_data.csv')
df1= pd.DataFrame(stars)
df = pd.DataFrame(brown_dwarfs)
nan_removed = df.fillna(0)
nan_removed["Radius"] =  nan_removed["Radius"].astype(float)
nan_removed["Mass"] =  nan_removed["Mass"].astype(float)
nan_removed["Radius"] =  nan_removed["Radius"]*0.102763
nan_removed["Mass"] =  nan_removed["Mass"]*0.000954588
merged_data = pd.merge(nan_removed,df1)
merged_data.to_csv('merged_data.csv')