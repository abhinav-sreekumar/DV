import json
import pandas as pd
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

from app import app
from apps import map_ipc
# , map_women, map_scst, map_children

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("IPC", href="/map-ipc")),
            dbc.NavItem(dbc.NavLink("Women", href="/map-women")),
            dbc.NavItem(dbc.NavLink("SC & ST", href="/map-scst")),
            dbc.NavItem(dbc.NavLink("Children", href="/map-children")),
        ], 
    ),
    html.Div(id='map-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/map-ipc':
        return map_ipc.layout
    # elif pathname == '/map-women':
    #     return map_women.layout
    # elif pathname == '/map-scst':
    #     return map_scst.layout
    # elif pathname == '/map-children':
    #     return map_children.layout