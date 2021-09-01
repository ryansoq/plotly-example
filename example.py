import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from dash import Dash

app = Dash()

app.layout = html.Div([
    dcc.Graph(id="graph"),
    dcc.Interval(id='interval-component', interval=60 * 1000, n_intervals=0), # 1 Second
    ])

@app.callback(
    Output("graph", "figure"), 
    Input("interval-component", "n_intervals"))
def display_graph(n_clicks):
    df = pd.read_csv('test.csv')
    x, y, z= 'task', 'cycle', 'time'
    fig = px.scatter(df, x=x, y=y, hover_data=[z])
    return fig

app.run_server(debug=True)
