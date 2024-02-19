import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from app import app
dash.register_page(__name__, path='/distribution', name='Distribution')
################ LOAD DATASET #####################
housing_df = pd.read_csv('Copy of Housing dataset.csv')
########## HISTOGRAM #################


def create_distribution(col_name='bedrooms'):
    return px.histogram(data_frame=housing_df, x=col_name, height=400)


############################ WIDGETS ######################
columns = ["bedrooms", "floors", "waterfront", "view",
           "Condition", "grade", "yr_built", "yr_renovated"]

dd = dcc.Dropdown(id="dist_column", options=columns,
                  value="bedrooms", clearable=False, className='drop_down_list')

###################### PAGE LAYOUT ###################


layout = html.Div(children=[html.Br(),
                                html.Img(src=app.get_asset_url('statistics.png'),
                                         className='title_image'
                                         ),
                                html.H3('Housing Market Dashboard',
                                        style={'color': 'white'},
                                        className='title'
                                        ),
                                          html.Div( [ "Select Columns : ", dd],className='drop') , 
                            
                                        
                            dcc.Graph(id="histogram")], className="box row")
###################### CALLBACKS ######################


@callback(Output("histogram", "figure"), [Input("dist_column", "value"),])
def update_histogram(dist_column):
    return create_distribution(dist_column)
