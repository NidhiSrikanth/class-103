import pandas as pd
import plotly.express as px

df= pd.read_csv("Data-visualization-master\csv files\data.csv")
print(df)
fig= px.bar(df, x= "InternetUsers", y= "Population", color= "Country")
fig.show()