import pandas as pd
import plotly.express as px

df= pd.read_csv("Data-visualization-master\csv files\data.csv")
fig= px.scatter(df,x="Country", y="Per capita", color="Country", size="Percentage", size_max=30)
fig.show()