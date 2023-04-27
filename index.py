import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv(
    '/Users/biorgan/Development/development/dash_plot_proyetc/Covid19VacunasAgrupadas.csv')

# print(df)
# print(df.vacuna_nombre.nunique())
# print(df.vacuna_nombre.nunique())


app = dash.Dash(__name__)

colors = {
    'background': '#E2EE38',
    'text': '#111111'
}

app.layout = html.Div([
    html.Div([
        html.H1('Vacunados por covid', style={
                'backgroundColor': colors['background'],
                'textAlign': 'center',
                'color': colors['text']
                }),
        html.Img(src='assets/images.jpeg',
                 style={'margin-bottom': '5px',
                        'display': 'inline-block',
                        'width': '9%', 'border': 'none'})
    ], className='banner'),
    # this is a box selection
    html.Div([
        html.Div([
            html.P('Selecciona la dosis', className='fix_label',
                   style={
                       'float': 'lefth',
                       'color': 'black', 'margin-top': '2px'}),
            dcc.RadioItems(id='dosis-radioitems',
                           labelStyle={'display': 'inline-block'},
                           options=[
                               {'label': 'Primera dosis',
                                'value': 'primera_dosis_cantidad'},
                               {'label': 'Segunda dosis',
                                'value': 'segunda_dosis_cantidad'}
                           ], value='primera_dosis_cantidad',
                           style={'text-aling': 'center',
                                  'color': 'black'},
                           className='dcc_compon'),
        ], className='create_container_1', style={'margin-bottom': '2px'}),
    ], className='row'),
    # this is a first grafic
    html.Div([
        html.Div([
            dcc.Graph(id='my_graph', figure={}, style={
                'height': '500px', 'width': '100%'})
        ], className='create_container_1'),

        # this is a second grafic
        html.Div([
            dcc.Graph(id='pie_graph', figure={}, style={
                'height': '500px', 'width': '100%'})
        ], className='create_container_1')
    ], className='row'),

], id='mainContainer', style={'width': '100%', 'flex-direction': 'column', 'display': 'flex'})


@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph(value):

    if value == 'primera_dosis_cantidad':
        fig = px.bar(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='primera_dosis_cantidad',
            color_discrete_sequence=['#1f77b4'])  # Cambia el color de las barras
    else:
        fig = px.bar(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='segunda_dosis_cantidad',
            color_discrete_sequence=['#3341FF'])  # Cambia el color de las barras
    return fig


@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph_pie(value):
    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame=df,
            names='jurisdiccion_nombre',
            values='primera_dosis_cantidad'
        )
    else:
        fig2 = px.pie(
            data_frame=df,
            names='jurisdiccion_nombre',
            values='segunda_dosis_cantidad')
    return fig2


# Agrega un enlace al archivo CSS
app.css.append_css({
    'external_url': '/dash_plot_proyetc/stylesheet.css'
})

# app.css.append_css(dict(external_url='http://localhost/style.css'))

if __name__ == ('__main__'):
    app.run_server(debug=True)
