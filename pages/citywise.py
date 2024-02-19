import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from app import app
dash.register_page(__name__, path='/citywise', name="Survived Count")
###### DATASET ###########
housing_df = pd.read_csv("Copy of Housing dataset.csv")

####### BARCHART #############


def create_bar_chart(col_name="waterfront"):
    fig = px.histogram(data_frame=housing_df, x="Property location", color=col_name,
                       histfunc="count", barmode='group', height=400)
    fig = fig.update_layout(bargap=0.5)
    return fig


################### WIDGETS #################
columns = ['waterfront', 'view', 'grade', 'bedrooms', 'Condition','price']
dd = dcc.Dropdown(id="sel_col", options=columns, value="waterfront",
                  clearable=False, className='drop_down_list')

################# PAGE LAYOUT ##################
layout = html.Div(children=[
    html.Br(),
    html.Img(src=app.get_asset_url('statistics.png'),
             className='title_image'
             ),
    html.H3('Housing Market Dashboard',
            style={'color': 'white'},
            className='title'
            ),
    html.Div(["Select Columns : ", dd], className='drop'),
    dcc.Graph(id="bar_chart")
], className="box row")

###################### CALLBACKS ##########################


@callback(Output("bar_chart", "figure"), [Input("sel_col", "value"),])
def update_bar_chart(sel_col):
    return create_bar_chart(sel_col)
