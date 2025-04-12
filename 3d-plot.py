import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html

df = pd.read_csv('data.csv', sep=';')

fig = px.line_3d(df, x="x", y="z", z="y")

# Данные для точек
df_points = pd.DataFrame({
    'x': [0, 1600, 5600, 4000, 8000, 6400,4000],
    'z': [0, 0,0,0,0,0, 0],
    'y': [0, 8000, 9600, 6400, 2000, 5600, 4000]
})

# Добавление точек к графику
fig.add_scatter3d(
    x=df_points['x'],
    y=df_points['y'],
    z=df_points['z'],
    mode='markers',
    marker=dict(size=5, color='red'),
    showlegend=False
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
