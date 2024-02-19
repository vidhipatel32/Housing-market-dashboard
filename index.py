from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


# Connect to main app.py file
from app import app

# Connect to your pages
from pages import dataset, distribution, intro, realtionship, citywise, main

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content', children=[]),

    html.Div(
        [
            html.Div([
                html.Div([
                    html.Img(src="/assets/statistics.png",
                             style={"width": "4.9rem"}),
                    html.H5(" Housing Market Dashboard", style={
                        'color': 'white', 'margin-top': '20px'}),
                ], className='image_title')
            ], className="sidebar-header"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-house"),
                        html.Span("Home", style={'margin-top': '3px'})], className='icon_title')],
                        href="/",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("Overview", style={'margin-top': '3px'})], className='icon_title')],
                        href="/pages/overview",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("Distribution", style={'margin-top': '3px'})], className='icon_title')],
                        href="/pages/distribution",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("relationship", style={'margin-top': '3px'})], className='icon_title')],
                        href="/pages/relationship",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("Citywise", style={'margin-top': '3px'})], className='icon_title')],
                        href="/pages/citywise",
                        active="exact",
                        className="pe-3"
                    ),

                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-database"),
                        html.Span("Data", style={'margin-top': '3px'})], className='icon_title')],
                        href="/pages/dataset",
                        active="exact",
                        className="pe-3"
                    ),

                ],
                vertical=True,
                pills=True,
            ),
        ],
        id="bg_id",
        className="sidebar",
    )

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return intro.layout
    elif pathname == '/pages/dataset':
        return dataset.layout
    elif pathname == '/pages/distribution':
        return distribution.layout
    elif pathname == '/pages/relationship':
        return realtionship.layout
    elif pathname == '/pages/citywise':
        return citywise.layout
    elif pathname == '/pages/overview':
        return main.layout


if __name__ == '__main__':
    app.run_server(debug=True)
