from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./bandsup.csv')
# print(df['Unnamed: 0'])
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Band structure', style={'textAlign':'center'}),
    dcc.Dropdown(df['Unnamed: 0'].unique(), 'b0_up', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df #[df['Unnamed: 0']==value]
    
    fig =  px.line(dff, x='Unnamed: 0', y=df.columns[100:300],markers='')
    fig.update_traces(line_color='#FF0000',
                      showlegend=False,
                      line_width=0.75)
    fig.update_layout(margin=dict(l=20, r=60, t=10, b=150),
                      width=500,
                      height=800,
                      xaxis_title="", 
                      xaxis = dict(tickvals=[50,150],   ticktext=['G','X']),
                      yaxis_title="energy (eV)",
                      yaxis_range=[-1.5,1.5])
    return fig


if __name__ == '__main__':
    app.run(debug=True)
