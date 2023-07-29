import pandas as pd
 
 

merged_data = pd.read_csv('./merged_data.csv')
df = pd.DataFrame(merged_data)
df.drop(columns=["luminosity","App.mag.","Spectraltype","Unnamed: 0" ],inplace = True)
df = df.loc[:, ~df.T.duplicated()]
df.replace('?', pd.NA, inplace=True)
names = df["Brown dwarf"].to_list()
radius =  df["Radius"].to_list()
mass=   df["Mass"].to_list()
print(mass)
radius_mass_list = []
 
df2 = df.loc[df['Radius'] != 0]
df2 = df.loc[df['Mass'] != 0]
 
# a = df.loc[ . [6]!= 0]
# b = df.loc[ . [7] != 0]

 
 
 
nan_rem = df2.fillna(0)
 
print(df2.head(30))
df2.to_csv('final_Merged_data.csv')