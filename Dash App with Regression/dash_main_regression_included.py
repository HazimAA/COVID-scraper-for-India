# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import datetime as dt
from dash.dependencies import Input, Output


pd.set_option('display.max_columns',None)
pd.set_option('display.width', 250)

#Reading data from JSON stored in Local

df2 = pd.read_json('C:\\Users\\HP\\Documents\\Total COVID data accumulated by someone, scraped by me\\JSON Daily_Totals_Latest_Country')
df2.index.name = 'State Code'
df2 = df2.sort_index(axis = 1, ascending=True)

#List of dates
dates = df2.columns
#To convert from Timestamp format, to dates
labels = dates.map(pd.Timestamp.date)
#To ordinal for enabling Regression Analysis
xx = dates.map(dt.datetime.toordinal)


# #List of States
available_indicators = list(df2.index.values)
drop_down_opts = [{'label': i, 'value': i} for i in available_indicators]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#CCFFFF',
    'text': '#336666',
    'white': '#d4ffff',
    'black': '#CCFFFF'
}

##Cleaning up null values so that all entries in the record can be read
df2.loc['AN'] = df2.loc['AN'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['AP'] = df2.loc['AP'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['AR'] = df2.loc['AR'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['AS'] = df2.loc['AS'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['BR'] = df2.loc['BR'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['CH'] = df2.loc['CH'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['CT'] = df2.loc['CT'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['DL'] = df2.loc['DL'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['DN'] = df2.loc['DN'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['GA'] = df2.loc['GA'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['GJ'] = df2.loc['GJ'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['HP'] = df2.loc['HP'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['HR'] = df2.loc['HR'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['JH'] = df2.loc['JH'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['JK'] = df2.loc['JK'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['KA'] = df2.loc['KA'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['KL'] = df2.loc['KL'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['LA'] = df2.loc['LA'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['MH'] = df2.loc['MH'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['ML'] = df2.loc['ML'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['MN'] = df2.loc['MN'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['MP'] = df2.loc['MP'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['MZ'] = df2.loc['MZ'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['NL'] = df2.loc['NL'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['OR'] = df2.loc['OR'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['PB'] = df2.loc['PB'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['PY'] = df2.loc['PY'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['RJ'] = df2.loc['RJ'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['SK'] = df2.loc['SK'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['TG'] = df2.loc['TG'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['TN'] = df2.loc['TN'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['TR'] = df2.loc['TR'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['TT'] = df2.loc['TT'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['UN'] = df2.loc['UN'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['UP'] = df2.loc['UP'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['UT'] = df2.loc['UT'].apply(lambda x: {} if pd.isna(x) else x)
df2.loc['WB'] = df2.loc['WB'].apply(lambda x: {} if pd.isna(x) else x)

df3 = pd.json_normalize(df2.loc['TT'], max_level= 1)

# #Plotting the figure (confirmed vs recovered
data =["delta.confirmed","delta.recovered"]
fig = px.scatter(df3, x=xx, y=data,trendline= "ols")
layout_1 = dict(
    xaxis=dict(
        tickvals=dates
    )
)
fig.update_layout(
    layout_1,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['white'],
    font_color=colors['text'],
    transition_duration=500
)

fig.update_xaxes(title_text='Dates')
fig.update_yaxes(title_text='Count of Confirmed/Recovered')
#fig.show()

#Plotting the figure (Tested)
data_tested =["delta.tested"]
fig_tested = px.scatter(df3, x=xx, y=data_tested, trendline="ols")
layout_2 = dict(
    xaxis=dict(
        tickvals=dates
    )
)
fig_tested.update_layout(
    layout_2,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['white'],
    font_color=colors['text'],
    transition_duration=500
)
fig_tested.update_xaxes(title_text='Dates')
fig_tested.update_yaxes(title_text='Count of Tested')



app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(children='COVID-19 Dashboard',
        style = {
            'textAlign': 'center',
            'color': colors['text']
        }
        ),

        html.Div(children='''
            A Dashboard for viewing daily COVID Cases in India
        ''', style={
            'textAlign': 'center',
            'color': colors['text']
            }
            ),

        html.Div([
            dcc.Dropdown(
                        id='state-selector',
                        options=drop_down_opts,
                        # multi=True,
                        value='TT',
                        style={'height': '30px', 'width': '100px'}
                    )
            ],
            style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
        ,

        html.Div([
            dcc.Dropdown(
                id='state-selector-2',
                options=drop_down_opts,
                # multi=True,
                value='TT',
                style={'height': '30px', 'width': '100px'}
            )
        ],
            style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

        dcc.Graph(
            id='example-graph-testing',
            figure=fig_tested
        )

    ]
)

#
@app.callback(
    Output('example-graph', 'figure'),
    Output('example-graph-testing','figure'),
    [Input('state-selector', 'value')]
        ,
     [Input('state-selector-2', 'value')]
)
#
def update_figure(selected_state, selected_state_2):

    data = ["delta.confirmed", "delta.recovered"]
    x = selected_state
    df4 = pd.json_normalize(df2.loc[x], max_level= 1)
#     # print(df3)
    fig2 = px.scatter(df4, x=xx, y=data, trendline="ols")
    fig2.update_xaxes(title_text='Dates')
    fig2.update_yaxes(title_text='Count')
    fig2.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['white'],
        font_color=colors['text'],
        transition_duration=500
    )
    # fig.show()

    data_tested = ["delta.tested"]
    t = selected_state_2
    df5 = pd.json_normalize(df2.loc[t], max_level=1)
    fig_tested = px.scatter(df5, x=xx, y=data_tested, trendline="ols")
    fig_tested.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['white'],
        font_color=colors['text'],
        transition_duration=500
    )
    fig_tested.update_xaxes(title_text='Dates')
    fig_tested.update_yaxes(title_text='Count of Tested')

    return fig2, fig_tested

if __name__ == '__main__':
    app.run_server(debug=True)
