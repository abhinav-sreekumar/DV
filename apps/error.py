from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from app import app

layout = html.Div([
    html.Img(src='/assets/error.svg', style={'height': '65%', 'width': 'auto'}, className='mx-auto mt-5 d-block'),
    html.H1('No demons here :P', style={'text-align': 'center'}, className='mt-5'),
], style={'color': 'white', 'height': '100vh'})