
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from app import app
dash.register_page(__name__, path='/overview', name="overview")
# Load the dataset
df = pd.read_csv("Copy of Housing dataset.csv")
df_1 = [df.groupby("Property location")["price"].min(),
        df.groupby("Property location")["price"].max()]
df_1 = pd.DataFrame(df_1).round()
df_1.index = ['Min Price', 'Max Price']

layout = html.Div([
    html.Br(),
    html.Img(src=app.get_asset_url('statistics.png'),
             className='title_image'
             ),
    html.H3('Housing Market Dashboard',
            style={'color': 'white'},
            className='title'
            ),

    dcc.Graph(
        id='price-bar-chart',
        figure={
            'data': [
                {'x': df_1.columns,
                    'y': df_1.loc['Min Price'], 'type': 'bar', 'name': 'Min Price'},
                {'x': df_1.columns,
                    'y': df_1.loc['Max Price'], 'type': 'bar', 'name': 'Max Price'},
            ],
            'layout': {
                'title': 'Property Price Range by Location',
                'xaxis': {'title': 'Location'},
                'yaxis': {'title': 'Price'},
            }
        }
    )
], className="box row")
