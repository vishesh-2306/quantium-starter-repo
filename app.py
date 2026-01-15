import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


df = pd.read_csv("processed_data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')


app = Dash(__name__)

regions = ['all', 'north', 'east', 'south', 'west']

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#333', 'marginBottom': '20px'}
    ),

    html.Div(
        children=[
            html.Label("Select Region:"),
            dcc.RadioItems(
                id='region-selector',
                options=[{'label': r.title(), 'value': r} for r in regions],
                value='all',
                inline=True
            ),
        ],
        className='RegionFilter'
    ),

    dcc.Graph(
        id='sales-line-chart'
    )
], style={'fontFamily': 'Arial', 'padding': '20px'})


@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df
        region_label = "All"
    else:
        filtered = df[df['region'] == selected_region.lower()]
        region_label = selected_region.title()

    fig = px.line(
        filtered,
        x='date',
        y='Sales',
        title=f'Pink Morsel Sales Over Time — {region_label} Region',
        labels={'date': 'Date', 'Sales': 'Sales ($)'}
    )

    fig.update_layout(title_x=0.5)
    return fig


if __name__ == '__main__':
    app.run(debug=True)

