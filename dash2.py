from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./fullbands.csv')
hsp_index = df['hsp_index'].unique()
hsp_names = df['hsp_names'].unique()
print(hsp_index)

singlelength = df[df['spin']=='up'].shape[0]

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Band structure', style={'textAlign':'center'}),
    dcc.Dropdown(df['spin'].unique(), 'up', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df['spin']==value]
    
    fig =  px.line(dff, x=range(singlelength), y=df.columns[100:300],markers='')
    if value == 'up':
        fig.update_traces(line_color='#FF0000',
                        showlegend=False,
                        line_width=0.75)
    elif value == 'down':
        fig.update_traces(line_color='#0000ff',
                showlegend=False,
                line_width=0.75)
    fig.update_layout(margin=dict(l=20, r=60, t=10, b=150),
                      width=500,
                      height=800,
                      xaxis_title="", 
                      xaxis = dict(tickvals=hsp_index,   ticktext=hsp_names),
                      yaxis_title="energy (eV)",
                      yaxis_range=[-1.5,1.5])
    [fig.add_vline(x=v, 
                   line_width=0.75, 
                   line_dash="dash", 
                   line_color="gray") for v in hsp_index ]

    return fig


if __name__ == '__main__':
    app.run(debug=True)
