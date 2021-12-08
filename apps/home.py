from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from app import app

cards = html.Div([
    dbc.Row([
            dbc.Col(dbc.Card(
                dbc.CardBody([
                    html.H5("Abhinav Sreekumar", className="card-title"),
                    html.P("20BCE0486", className="card-text"),
                ]), color="#EDEDF4")),
            dbc.Col(dbc.Card(
                dbc.CardBody([
                    html.H5("Gauri Gupta", className="card-title"),
                    html.P("20BCE0495", className="card-text"),
                ]), color="#EDEDF4")),
        ],
        className="m-4",
    ),
    dbc.Row(
        [
            dbc.Col(dbc.Card(
                dbc.CardBody([
                    html.H5("Mrinal Agarwal", className="card-title"),
                    html.P("20BCE0485", className="card-text"),
                ]), color="#EDEDF4")),
            dbc.Col(dbc.Card(
                dbc.CardBody([
                    html.H5("Shashank Suresh", className="card-title"),
                    html.P("20BCE0484", className="card-text"),
                ]), color="#EDEDF4")),
        ],
        className="m-4",
    )
], style={'color': 'black'})

layout = html.Div([
    html.Div([
        html.H1('Objective'),
        html.P('''Our aim is to represent the change in crime rate against SC’s and ST’s, 
        juveniles, women and in general with respect to the police strength in a given area.
        This helps us understand how effectively increasing the numbers of police personnel in 
        an area helps in controlling the crime rate.''', style={'width': '80%', 'text-align': 'center', 'margin': 'auto'}),
    ], style={"text-align": "center"}),
    html.Div([
        html.H1('Team Members'),
        html.Div([cards], style={'width': '80%', 'margin': 'auto'})
    ], style={"margin-top": "80px", "text-align": "center"}),
    html.A(children=[
        html.Div([
            html.P("Go to source code", style={"font-style": "italic", 'font-size': '20px'}),
            html.I(className="bi bi-chevron-double-right", style={'font-size': '50px'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'margin-top': '55px', 'text-align': 'center'}),
    ], href="https://github.com/ASKOFFICIAL/DV", style={'color': 'white', 'text-decoration': 'none'}),
], style={"margin-top": "100px", "color": "white"})