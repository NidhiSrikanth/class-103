import pandas as pd 
import plotly.express as px

df= pd.read_csv("C:\Srinidhi\class 103\Data-visualization-master\csv files\line_chart.csv")
print(df)
fig= px.line(df, x="Year", y="Per capita income", color= "Country", title= "Per capita income")
fig.show()