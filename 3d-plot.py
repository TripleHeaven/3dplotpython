import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html

df = pd.read_csv('data.csv', sep=';')

fig = px.line_3d(df, x="x", y="z", z="y")
fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        bgcolor='rgba(0,0,0,0)'
    ),
    paper_bgcolor='white'
)

app = Dash()

app.layout = html.Div(
    children=[
        dcc.Graph(
            id='graph',
            figure=fig,
            style={
                'position': 'absolute',
                'top': 0,
                'bottom': 0,
                'left': 0,
                'right': 0,
                'height': '100%',
                'width': '100%',
            },
            config={
                'responsive': True
            }
        )
    ],
    style={
        'position': 'absolute',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'right': 0,
        'height': '100%',
        'width': '100%',
        'overflow': 'hidden',
        'margin': 0,
        'padding': 0
    }
)

app.run()
