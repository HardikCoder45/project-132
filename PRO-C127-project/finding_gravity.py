import pandas as pd
import numpy as np
import plotly.express as px

 

final_csv = pd.read_csv('./final_merged_data.csv')
final_csv_data = pd.read_csv('./gravity_conating_data.csv')
df = pd.DataFrame(final_csv)
df1 = pd.DataFrame(final_csv_data)
 

radius =  df["Radius"].to_list()
mass=   df["Mass"].to_list()
 
final_gravity = []
names = df['Brown dwarf'].to_list()

for index, name in enumerate(names):
    if radius[index] != 0.0:
     gravity = 6.674e-11 * (mass[index] * 1.989e+30) / (radius[index] * 6.957e+8)**2
     print(gravity)

    else:
     gravity = 0
     print(gravity)
    final_gravity.append(gravity)
  
   
    # gravity = 6.674e-11*( mass[index]*1.989e+30) / (radius[index]*6.957e+8)*(radius[index]*6.957e+8) 
    # print(gravity)
    # final_gravity.append(gravity)

 
df["gravity"] = final_gravity
df.to_csv('gravity_conating_data.csv')
#6.082445040272639e+18

fig = px.scatter(x=df1["Radius"], y=df1["Mass"], size=df1["gravity"], hover_data=[df1["Brown dwarf"]])
fig.show()

 