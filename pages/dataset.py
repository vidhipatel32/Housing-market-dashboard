import pandas as pd
import dash
from dash import html,dash_table,dcc
import plotly.graph_objects as go
dash.register_page(__name__,path='/dataset',name="Dataset")
########### DATASET ######################
housing_df=pd.read_csv("Copy of Housing dataset.csv")

####### Layout #########
layout = html.Div(children=[
    html.H3('Data Table', style={"color": "#0084d6", }),
                    dcc.Markdown('''
                    The below data in the table has been used in this **dashboard**.
                    ''', style={'margin-top': '10px',
                                'color': '#ffffff',
                                'line-height': '1.2'}),
                    html.Hr(),
    html.Br(),
    dash_table.DataTable(data=housing_df.to_dict('records'),
                         page_size=15,
                         style_cell={"background-color": "black","border":"solid 1px white","color":"white","font-size":"11px","text-align":"left"},
                         style_header={"background-color":"black","font-weight":"bold","color":"white","padding":"10px","font-size":"10px"},
                         )
],className="box row")

