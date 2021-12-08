from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import home, IPC, scst, Women, children


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("IPC", href="/IPC")),
            dbc.NavItem(dbc.NavLink("Women", href="/Women")),
            dbc.NavItem(dbc.NavLink("SC & ST", href="/SCST")),
            dbc.NavItem(dbc.NavLink("Children", href="/Children")),
        ],
    ),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return html.H1("Test")
    elif pathname == '/IPC':
        return IPC.layout
    elif pathname == '/Women':
        return Women.layout
    elif pathname == '/SCST':
        return scst.layout
    elif pathname == '/Children':
        return children.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)