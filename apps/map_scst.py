import pandas as pd
import json
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

df = pd.read_csv("Map_CSVs/Crimes_Against_SC_ST_Test.csv")
json1 = json.load(open("states_india.geojson"))

candidates = df.columns[3:-1] 
years = df.YEAR.unique()

layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='crime', 
            options=[{'value': x, 'label': x} 
                    for x in candidates],
            placeholder = "Choose a crime",
            style={'margin-bottom': '20px'}
        ),
        dcc.Dropdown(
            id='year', 
            options=[{'value': y, 'label': y} 
                    for y in years],
            placeholder = "Choose a year",
        ),
    ], style={'margin': '20px'}),
    dcc.Graph(id="choropleth3"),
])

@app.callback(
    Output("choropleth3", "figure"), 
    [Input("crime", "value"), Input("year", "value")])
def display_choropleth(crime, year):
    finaldata = df.loc[df["YEAR"] == year]

    fig = px.choropleth(
        finaldata, geojson=json1, color=crime,
        locations="state_code", featureidkey="properties.state_code", hover_data=["AREA_NAME"])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig