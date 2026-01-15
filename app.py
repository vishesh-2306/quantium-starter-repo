import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px


df = pd.read_csv("processed_data.csv")


df['date'] = pd.to_datetime(df['date'])


df = df.sort_values(by='date')


fig = px.line(df, x='date', y='Sales', title='Pink Morsel Sales Over Time')


app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualiser'),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

