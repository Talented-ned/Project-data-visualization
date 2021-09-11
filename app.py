import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, external_stylesheets=external_stylesheets ,suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
server = app.server