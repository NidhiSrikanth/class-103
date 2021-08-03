import pandas as pd
import plotly.express as px

df= pd.read_csv("Data-visualization-master\csv files\line_chart.csv")
fig=px.scatter(df,x= "Year", y="Per capita income", color= "Country", size= "Per capita income")
fig.show()