
from dash import html
from dash import dcc
from app import app


layout = html.Div([
    html.Img(src=app.get_asset_url('statistics.png'),
             className='title_image', style={'height': '70px', 'width': '100px', 'margin-left': '600px','margin-top': '5px'}
             ),
    html.H1('Housing Market Dashboard',
            style={'color': 'white', 'margin-left': '500px'},
            className='title'
            ),
    html.Div([
        html.Div([
            html.P([html.P(dcc.Markdown('''Welcome to the **Housing Market Dashboard**!''',
                                        style={"color": "#0084d6",
                                               "font-size": "15px",
                                               'margin-left': '15px',
                                               'margin-top': '15px'})),
                    html.P(dcc.Markdown(
                        '''
                        Here, I have designed the dashboard with the Python libraries Plotly dash for data visualizations 
                        and dash for web framework. I examined the housing markets of several cities in the United States using
                          graphs and key performance indicators with a drop down list.
                        ''',
                        style={"color": "#ffffff",
                               "font-size": "15px",
                               'margin-left': '15px',
                               'margin-right': '15px',
                               'margin-bottom': '15px',
                               'line-height': '1.2',
                               'text-align': 'justify'}
                    )),




                    html.H3('  Data Variables : ',
                            style={"color": "#0084d6",
                                   'margin-left': '15px',
                                   'margin-right': '15px',
                                   'margin-bottom': '10px',
                                   'line-height': '1.2',
                                   'text-align': 'left',
                                   'margin-top': '-15px'}
                            ),
                    html.P([dcc.Markdown(
                        '''
                        **Price** : Price of house

                        **bedrooms**: Number

                        **sqft_living, sqft_lot** : The Original square footage of the living and lot space when the house was built

                        **floors **: Total floors in the house

                        **waterfront**: Whether the house is on a waterfront(1: yes, 0: no)

                        **view** : special view?

                        **condition** : Condition of the house

                        **grade** : Simply put, the grade or grading around your house is the level of the ground. The ground level and how it's graded is the 
                                     deciding factor of where storm water will flow

                        **yr_built** : Built year

                        **yr_renovated** : Year when the house was renovated
                        
                        ''',
                        style={"color": "#ffffff",
                               "font-size": "15px",
                               'margin-left': '15px',
                                              'margin-right': '15px',
                                              'margin-bottom': '15px',
                                              'line-height': '1.2',
                                              'text-align': 'justify'},
                    ),
                    ])
                    ])
        ], className='intro_bg eight columns')
    ], className='intro_row row')
])
