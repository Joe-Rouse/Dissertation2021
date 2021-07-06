import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.title = 'COVID-19 and Sustainability'

df = pd.read_csv('dataset.csv')

available_countries = df['Country'].unique()

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#B1AFAF",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

PILL_STYLE = {
    "background-color" : "#434242",
    "color" : "#FFFFFF",
    "textAlign" :"center",
}

HEAD_STYLE = {
    "textAlign" :"center"
}

CENTRETEXT_STYLE = {
    "textAlign" :"center"
}

REGTEXT_STYLE = {
    
}

GRAPH_STYLE = {
    "color" : "#434242",
}

LINK_STYLE = {
    "text-decoration": "underline"
}

sidebar = html.Div(
    [
        html.H2("COVID-19 and Sustainability Dashboard", className="display-5", style=CENTRETEXT_STYLE),
        html.Hr(),
        html.P("An interactive dashboard for COVID-19 and Sustainability data", className="lead", style=CENTRETEXT_STYLE),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Cases and Fatalities", href="/", active="exact",style=PILL_STYLE),
                html.Br(),
                dbc.NavLink("Sustainability", href="/sustainability", active="exact",style=PILL_STYLE),
                html.Br(),
                dbc.NavLink("COVID-19 & Sustainability", href="/covidsustainability", active="exact",style=PILL_STYLE),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('COVID-19 Cases, Deaths and Recoveries',style=HEAD_STYLE),
                html.Hr(),

                html.P('Select what to view on the graph: ',style=CENTRETEXT_STYLE),
                dcc.Dropdown(
                    id='covidDropdown',
                    options=[{'label':'Cases','value':'Cases'},
                             {'label':'Deaths','value':'Deaths'},
                             {'label':'Recoveries','value':'Recovered'},
                             ],
                    value='Cases'
                    ),
                dcc.Graph(id='covidBar'),
                html.Br(),
                html.P('This graph compares Country (X) data with whatever is selected from the dropdown (Y). This can be Cases, Deaths or Recoveries.', style=CENTRETEXT_STYLE),
                html.Hr(),

                html.H1('COVID-19 Country Compare', style=HEAD_STYLE),
                html.P('Use the graph below to compare countries of your choice: ', style = CENTRETEXT_STYLE),

                html.P('Select a Country from the X Axis:', style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='xCountrySelect',
                    options=[{'label':i , 'value':i} for i in available_countries],
                    multi=True,
                    ),
                html.Br(),

                html.P('Select COVID data from the Y Axis:', style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='yCountrySelect',
                    options=[{'label':'Cases','value':'Cases'},
                             {'label':'Deaths','value':'Deaths'},
                             {'label':'Recoveries','value':'Recovered'},
                             ],
                    value='Cases'
                    ),
                dcc.Graph(id='countrySelectBar', ),
                html.Br(),
                html.P('This graph allows you to compare COVID-19 data (Y) from countries (X) of your choice.', style=CENTRETEXT_STYLE),
                html.Hr(),

                html.P("The data used in this section is sourced from Worldometers. You can access their work by clicking the link below: ", style=REGTEXT_STYLE),
                dcc.Link('Worldometers', href ='https://www.worldometers.info/coronavirus/#countries', style = LINK_STYLE, target ="_blank"),

               ]
            
    elif pathname == "/sustainability":
        return [

                html.H1('Sustainability', 
                        style=HEAD_STYLE),
                html.Hr(),

                html.P('The purpose of this page is to investigate the sustainability of the countries studied in the COVID-19 section of the dashboard. Doing so can help understand the economic, human and ' +
                       'environmental situations of those countries.', style=CENTRETEXT_STYLE),
                html.Hr(),

                html.P("Select an option for the Y axis: ", style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='wellbeingDropdown',
                    options=[
                        {'label': 'Human Wellbeing', 'value': 'Human Wellbeing'},
                        {'label': 'Economic Wellbeing', 'value': 'Economic Wellbeing'},
                        {'label': 'Environmental Wellbeing', 'value': 'Environmental Wellbeing'},
                        {'label': 'Total Average', 'value': 'Total Average'},
                        {'label': 'Total Average GDP', 'value': 'Total Average GDP'},
                        ],
                    value='Human Wellbeing'
                    ),
                html.Br(),
                dcc.Graph(id='customSusBar'),
                html.Br(),
                html.P('This graph shows the SSI indicator scores (Y) of countries (X).', style=CENTRETEXT_STYLE),
                html.P('NOTE: The indicator Total Average GDP is calculated the average of the 3 main indicators, but using GDP instead of Economic Wellbeing.', style=CENTRETEXT_STYLE),
                html.Hr(),

                
                html.H3('SSI Custom Scatter Graph', style=HEAD_STYLE),
                html.P("Use the dropdowns below to select your indicators, and the graph will automatically update.", style=CENTRETEXT_STYLE),

                html.P("Select an option for the X axis: ", style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='xDropdown',
                    options=[
                        {'label': 'Sufficient Food', 'value': 'Sufficient Food'},
                        {'label': 'Safe Sanitation', 'value': 'Safe Sanitation'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'Healthy Life', 'value': 'Healthy Life'},
                        {'label': 'Gender Equality', 'value': 'Gender Equality'},
                        {'label': 'Income Distribution', 'value': 'Income Distribution'},
                        {'label': 'Population Growth', 'value': 'Population Growth'},
                        {'label': 'Good Governance', 'value': 'Good Governance'},
                        {'label': 'Biodiversity', 'value': 'Biodiversity'},
                        {'label': 'Renewable Water Resources', 'value': 'Renewable Water Resources'},
                        {'label': 'Consumption', 'value': 'Consumption'},
                        {'label': 'Energy Use', 'value': 'Energy Use'},
                        {'label': 'Energy Savings', 'value': 'Energy Savings'},
                        {'label': 'Greenhouse Gases', 'value': 'Greenhouse Gases'},
                        {'label': 'Renewable Energy', 'value': 'Renewable Energy'},
                        {'label': 'Organic Farming', 'value': 'Organic Farming'},
                        {'label': 'Genuine Savings', 'value': 'Genuine Savings'},
                        {'label': 'GDP', 'value': 'GDP'},
                        {'label': 'Employment', 'value': 'Employment'},
                        {'label': 'Public Debt', 'value': 'Public Debt'},
                        {'label': 'Basic Needs', 'value': 'Basic Needs'},
                        {'label': 'Personal Development & Health', 'value': 'Personal Development & Health'},
                        {'label': 'Well-Balanced Society', 'value': 'Well-Balanced Society'},
                        {'label': 'Natural Resources', 'value': 'Natural Resources'},
                        {'label': 'Climate & Energy', 'value': 'Climate & Energy'},
                        {'label': 'Transistion', 'value': 'Transistion'},
                        {'label': 'Economy', 'value': 'Economy'},
                        ],
                    value='GDP'
                    ),
                html.Br(),
                html.P("Select an option for the Y axis: ", style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='yDropdown',
                    options=[
                        {'label': 'Sufficient Food', 'value': 'Sufficient Food'},
                        {'label': 'Safe Sanitation', 'value': 'Safe Sanitation'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'Healthy Life', 'value': 'Healthy Life'},
                        {'label': 'Gender Equality', 'value': 'Gender Equality'},
                        {'label': 'Income Distribution', 'value': 'Income Distribution'},
                        {'label': 'Population Growth', 'value': 'Population Growth'},
                        {'label': 'Good Governance', 'value': 'Good Governance'},
                        {'label': 'Biodiversity', 'value': 'Biodiversity'},
                        {'label': 'Renewable Water Resources', 'value': 'Renewable Water Resources'},
                        {'label': 'Consumption', 'value': 'Consumption'},
                        {'label': 'Energy Use', 'value': 'Energy Use'},
                        {'label': 'Energy Savings', 'value': 'Energy Savings'},
                        {'label': 'Greenhouse Gases', 'value': 'Greenhouse Gases'},
                        {'label': 'Renewable Energy', 'value': 'Renewable Energy'},
                        {'label': 'Organic Farming', 'value': 'Organic Farming'},
                        {'label': 'Genuine Savings', 'value': 'Genuine Savings'},
                        {'label': 'GDP', 'value': 'GDP'},
                        {'label': 'Employment', 'value': 'Employment'},
                        {'label': 'Public Debt', 'value': 'Public Debt'},
                        {'label': 'Basic Needs', 'value': 'Basic Needs'},
                        {'label': 'Personal Development & Health', 'value': 'Personal Development & Health'},
                        {'label': 'Well-Balanced Society', 'value': 'Well-Balanced Society'},
                        {'label': 'Natural Resources', 'value': 'Natural Resources'},
                        {'label': 'Climate & Energy', 'value': 'Climate & Energy'},
                        {'label': 'Transistion', 'value': 'Transistion'},
                        {'label': 'Economy', 'value': 'Economy'},
                        ],
                    value='Safe Sanitation'
                    ),
                dcc.Graph(id='customAxisScatter'),
                html.Br(),
                html.P('The graph below allows you to choose two indicators from the SSI to see how a country performs in both of them. Countries towards the top-right score highly in both. ', style=CENTRETEXT_STYLE),
                html.Hr(),

                html.P("The data used in this section is sourced from the Sustainable Society Index (SSI). You can access their work by clicking the link below: ", style=REGTEXT_STYLE),
                dcc.Link('Sustainable Society Index', href ='https://ssi.wi.th-koeln.de/', style = LINK_STYLE, target ="_blank"),

               ]

    elif pathname == "/covidsustainability":
        return [

                html.H1('COVID 19 & Sustainability',
                        style=HEAD_STYLE),
                html.Hr(),

                html.P('The purpose of this section is to link both sustainability and COVID-19 Data together. This can be used to analyse how sustainability factors can influence how a country has '+ 
                       'dealt with the pandemic.', style=CENTRETEXT_STYLE),
                html.Hr(),

                html.P('Select an SSI Indicator:', style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='xSusDropdown',
                    options=[
                        {'label': 'Sufficient Food', 'value': 'Sufficient Food'},
                        {'label': 'Safe Sanitation', 'value': 'Safe Sanitation'},
                        {'label': 'Education', 'value': 'Education'},
                        {'label': 'Healthy Life', 'value': 'Healthy Life'},
                        {'label': 'Gender Equality', 'value': 'Gender Equality'},
                        {'label': 'Income Distribution', 'value': 'Income Distribution'},
                        {'label': 'Population Growth', 'value': 'Population Growth'},
                        {'label': 'Good Governance', 'value': 'Good Governance'},
                        {'label': 'Biodiversity', 'value': 'Biodiversity'},
                        {'label': 'Renewable Water Resources', 'value': 'Renewable Water Resources'},
                        {'label': 'Consumption', 'value': 'Consumption'},
                        {'label': 'Energy Use', 'value': 'Energy Use'},
                        {'label': 'Energy Savings', 'value': 'Energy Savings'},
                        {'label': 'Greenhouse Gases', 'value': 'Greenhouse Gases'},
                        {'label': 'Renewable Energy', 'value': 'Renewable Energy'},
                        {'label': 'Organic Farming', 'value': 'Organic Farming'},
                        {'label': 'Genuine Savings', 'value': 'Genuine Savings'},
                        {'label': 'GDP', 'value': 'GDP'},
                        {'label': 'Employment', 'value': 'Employment'},
                        {'label': 'Public Debt', 'value': 'Public Debt'},
                        {'label': 'Basic Needs', 'value': 'Basic Needs'},
                        {'label': 'Personal Development & Health', 'value': 'Personal Development & Health'},
                        {'label': 'Well-Balanced Society', 'value': 'Well-Balanced Society'},
                        {'label': 'Natural Resources', 'value': 'Natural Resources'},
                        {'label': 'Climate & Energy', 'value': 'Climate & Energy'},
                        {'label': 'Transistion', 'value': 'Transistion'},
                        {'label': 'Economy', 'value': 'Economy'},
                        {'label': 'Human Wellbeing', 'value': 'Human Wellbeing'},
                        {'label': 'Environmental Wellbeing', 'value': 'Environmental Wellbeing'},
                        {'label': 'Economic Wellbeing', 'value': 'Economic Wellbeing'},
                        {'label': 'Total Average', 'value': 'Total Average'},
                        {'label': 'Total Average GDP', 'value': 'Total Average GDP'},
                        ],
                    value='Economy'
                    ),
                html.Br(),
                html.P('Select a COVID-19 indicator:', style=REGTEXT_STYLE),
                dcc.Dropdown(
                    id='yCovidDropdown',
                    options=[
                        {'label': 'Cases', 'value': 'Cases'},
                        {'label': 'Deaths', 'value': 'Deaths'},
                        {'label': 'Recoveries', 'value': 'Recovered'},
                        ],
                    value='Cases'
                    ),
                dcc.Graph(id='customCovidAxisScatter'),
                html.Br(),
                html.P('This graph allows you to compare COVID-19 data (Y) against an SSI indicator (X). Countries scoring highly in both will be located at the top-right of the graph.', style=CENTRETEXT_STYLE),
                html.Hr(),

                html.P("The data used in this section is sourced from the Sustainable Society Index (SSI) and Worldometers. You can access their work by using the links below: ", style=REGTEXT_STYLE),
                dcc.Link('Sustainable Society Index', href ='https://ssi.wi.th-koeln.de/', style = LINK_STYLE, target ="_blank"),
                html.Br(),
                html.Br(),
                dcc.Link('Worldometers', href ='https://www.worldometers.info/coronavirus/#countries', style = LINK_STYLE, target ="_blank"),
                
               ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    dash.dependencies.Output('covidBar', 'figure'),
    [dash.dependencies.Input('covidDropdown', 'value')])
def update_covidBar(covidDropdown):
    fig = px.bar(df,'Country',covidDropdown, hover_name='Country')
    return fig

@app.callback(
    dash.dependencies.Output('countrySelectBar', 'figure'),
    [dash.dependencies.Input('xCountrySelect', 'value'),
    dash.dependencies.Input('yCountrySelect', 'value')])
def update_countrySelectBar(xCountrySelect, yCountrySelect):
    fig = px.bar(df,xCountrySelect,yCountrySelect, hover_name='Country')
    return fig

@app.callback(
    dash.dependencies.Output('customSusBar', 'figure'),
    [dash.dependencies.Input('wellbeingDropdown', 'value')])
def update_customSusBar(wellbeingDropdown):
    fig = px.bar(df,'Country',wellbeingDropdown,hover_name="Country")
    return fig

@app.callback(
    dash.dependencies.Output('customAxisScatter', 'figure'),
    [dash.dependencies.Input('xDropdown', 'value'),
    dash.dependencies.Input('yDropdown', 'value')])
def update_customAxisScatter(xDropdown,yDropdown):
    fig = px.scatter(df,xDropdown,yDropdown,hover_name="Country")
    return fig

@app.callback(
    dash.dependencies.Output('customCovidAxisScatter', 'figure'),
    [dash.dependencies.Input('xSusDropdown', 'value'),
    dash.dependencies.Input('yCovidDropdown', 'value')])
def update_customCovidAxisScatter(xSusDropdown,yCovidDropdown):
    fig = px.scatter(df,xSusDropdown,yCovidDropdown,hover_name="Country")
    return fig

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)