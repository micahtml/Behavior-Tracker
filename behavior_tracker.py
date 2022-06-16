import plotly
import plotly.graph_objs as go
import pandas as pd

excel_file = 'malachi_data_tracker.xlsx'
df = pd.read_excel(excel_file)
print(df)

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]

data = [go.Scatter( x=df['Behavior'], y=df['Possible Trigger'], mode='markers',
        marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4))]


fig = go.Figure(data)
fig.show()