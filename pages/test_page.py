import dash
from dash import html

dash.register_page(__name__, path='/test')

layout = html.Div([
    html.H1('Test page'),
])