from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import home, IPC, scst, Women, children, map_ipc, map_women, map_scst, map_children, error

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("IPC", href="/map-ipc"),
                dbc.DropdownMenuItem("Women", href="/map-women"),
                dbc.DropdownMenuItem("SC & ST", href="/map-scst"),
                dbc.DropdownMenuItem("Children", href="/map-children"),
            ],
            nav=True,
            in_navbar=True,
            label="Maps",
            ),
            dbc.NavItem(dbc.NavLink("IPC", href="/IPC")),
            dbc.NavItem(dbc.NavLink("Women", href="/Women")),
            dbc.NavItem(dbc.NavLink("SC & ST", href="/SCST")),
            dbc.NavItem(dbc.NavLink("Children", href="/Children")),
        ], brand="DataVizDemons", brand_href="/"
    ),
    html.Div(id='page-content')
], style={"background-color": "#374a67", 'min-height': '100vh'})

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/IPC':
        return IPC.layout
    elif pathname == '/Women':
        return Women.layout
    elif pathname == '/SCST':
        return scst.layout
    elif pathname == '/Children':
        return children.layout
    elif pathname == '/map-ipc':
        return map_ipc.layout
    elif pathname == '/map-women':
        return map_women.layout
    elif pathname == '/map-scst':
        return map_scst.layout
    elif pathname == '/map-children':
        return map_children.layout
    else:
        return error.layout

if __name__ == '__main__':
    app.run_server()
