import pandas as pd
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from app import app

Crimes_Against_SC_ST = pd.read_csv('Test_CSVs/Crimes_Against_SC_ST_Test.csv')
Police_Strength = pd.read_csv('Test_CSVs/Police_Strength_Test.csv')

x = Crimes_Against_SC_ST.AREA_NAME.unique()
options = []
for i in x:
    options.append({'label': i, 'value': i})

crimeOptions=[]
for i in Crimes_Against_SC_ST.columns[2:]:
    crimeOptions.append({'label': i, 'value': i})

years = []
for i in Crimes_Against_SC_ST.YEAR.unique():
    years.append({'label': i, 'value': i})

caipc = Crimes_Against_SC_ST
caipc.sort_values(by=['AREA_NAME', 'YEAR'], inplace=True)
caipc.reset_index(drop=True, inplace=True)

ps = Police_Strength
ps.sort_values(by=['AREA_NAME', 'YEAR'], inplace=True)
ps.reset_index(drop=True, inplace=True)

layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='state',
            options=options,
            placeholder="Select a state",
            style={'margin-bottom': '20px'}
        ),
        
        dcc.Dropdown(
            id='crime',
            options=crimeOptions,
            placeholder="Select a Crime"
        ),
    ], style={'margin': '20px'}),

    html.Div([
        dcc.Graph(id="scst1")
    ], style={'margin': '20px'}),

    html.Div([
        dcc.Graph(id="scst2")
    ], style={'margin': '20px'}),

    html.Div([
        dcc.Dropdown(
            id='year',
            options=years,
            placeholder="Select a year",
            value='2001',
            style={'margin-bottom': '20px'}
        ), 
    ], style={'margin': '20px'}),

    html.Div([
        dcc.Graph(id="scst3")
    ], style={'display': 'flex', 'justify-content': 'center'}),
])

@app.callback(
    [
        Output('scst1', 'figure'),
        Output('scst2', 'figure'),
        Output('scst3', 'figure')
    ], 
    [
        Input('state', 'value'),
        Input('crime', 'value'),
        Input('year', 'value')
    ],
)
def update_figure(value, crimeValue, yearValue):
    # Bar-line Graph of Area+Crime vs Police Strength from 2001-2010
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=Police_Strength[Police_Strength.AREA_NAME.str.contains(value)].YEAR,
            y=Police_Strength[Police_Strength.AREA_NAME.str.contains(value)].RANK_ALL_RANKS_TOTAL,
            name="Police Strength",
        ),
        secondary_y=True,
    ) 

    fig.add_trace(
        go.Bar(
            x=Crimes_Against_SC_ST[Crimes_Against_SC_ST.AREA_NAME.str.contains(value)].YEAR,
            y=Crimes_Against_SC_ST[Crimes_Against_SC_ST.AREA_NAME.str.contains(value)][crimeValue],
            name=crimeValue+" Cases"
        ),
        secondary_y=False,
    )

    fig.update_layout(title_text = "Number of " + crimeValue + " cases Against IPC vs Police Strength")
    fig.update_xaxes(title_text="Year", dtick=1)
    fig.update_yaxes(title_text="Cases", secondary_y=False)
    fig.update_yaxes(title_text="Police Strength", secondary_y=True)
    fig.update_layout(autotypenumbers='convert types') 

    # Bubble Chart of Police Strength vs Crime Rate
    df2 = pd.merge(caipc, ps, on=['AREA_NAME', 'YEAR'])
    df2 = df2[['AREA_NAME', 'YEAR', crimeValue, 'RANK_ALL_RANKS_TOTAL']]
    df2.rename(columns={crimeValue: 'CRIME', 'RANK_ALL_RANKS_TOTAL': 'STRENGTH'}, inplace=True)

    df2['CRIME'] = pd.to_numeric(df2['CRIME'], errors='coerce')
    df2 = df2.dropna(subset=['CRIME'])
    df2['CRIME'] = df2['CRIME'].astype(int)

    fig2 = px.scatter(df2, x="STRENGTH", y="CRIME", color="AREA_NAME",
            animation_frame="YEAR", animation_group="AREA_NAME",
            size='CRIME', hover_name="AREA_NAME",
            size_max=50, height=800
            )

    fig2.update_layout(autotypenumbers='convert types', title_text="Police Strength vs Crime Rate", transition={"duration": 500})
    fig2.update_xaxes(title_text="Police Strength")
    fig2.update_yaxes(title_text="Total Cases")

    # Pie chart of Different types of Crimes 
    caipc2 = Crimes_Against_SC_ST
    caipc2 = caipc2[caipc2['YEAR'] == int(yearValue)]
    caipc2 = caipc2[caipc2['AREA_NAME'] == value]

    test = caipc2.columns[1:-2]

    pulls=[]
    for i in test:
        if(i==crimeValue):
            pulls.append(0.1)
        else:
            pulls.append(0)

    df3 = pd.DataFrame({'crimeOptions': test, 'numbers': caipc2.iloc[:, 1:-2].values[0]})
    
    fig3 = px.pie(
        data_frame=df3,
        values='numbers',
        names='crimeOptions',            
        title='Different types of Crimes',   
        template='presentation',
        width=1000,
        height=1000,                            
    )  
    fig3.update_traces(textposition='inside', marker=dict(line=dict(color='#000000', width=2)),
                        pull=pulls, opacity=0.8,)
    fig3.update_layout(title_text="Different types of Crimes in "+ value + " in year " + yearValue,
    uniformtext_minsize=14, 
    uniformtext_mode='hide',
    legend = dict(font = dict(size = 10, color = "black")),)
     
    return fig, fig2, fig3