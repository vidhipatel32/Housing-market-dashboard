import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from app import app
dash.register_page(__name__, path='/relationship', name="Realationship")
####### DATASET #############
housing_df = pd.read_csv("Copy of Housing dataset.csv")
####### SCATTER CHART ##########


def create_scatter_chart(x_axis="sqft_lot", y_axis="price"):
    return px.scatter(data_frame=housing_df, x=x_axis, y=y_axis, height=400)


###### WIDGETS ##########
columns = ["sqft_lot", "price", "yr_built", "sqft_living",
           "sqft_lot", "yr_renovated", "bedrooms", "floors"]
x_axis = dcc.Dropdown(id="x_axis", options=columns, value="sqft_lot",
                      clearable=False, className='drop_down_list')
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="price",
                      clearable=False, className='drop_down_list')

################### PAGE LAYOUT ##########################
layout = html.Div(children=[
    html.Br(),
    html.Img(src=app.get_asset_url('statistics.png'),
             className='title_image'
             ),
    html.H3('Housing Market Dashboard',
            style={'color': 'white'},
            className='title'
            ),
            html.Div( ["X-Axis : ", x_axis,
    "Y-Axis : ", y_axis] , className='drop'),
   
    dcc.Graph(id="scatter")
], className="box row")

############## CALLBACKS ###############
@callback(Output("scatter", "figure"), [Input("x_axis", "value"), Input("y_axis", "value"),])
def upadte_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)
