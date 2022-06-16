import plotly
import plotly.graph_objs as go
import pandas as pd

excel_file = 'malachi_data_tracker.xlsx'
df = pd.read_excel(excel_file)
print(df)