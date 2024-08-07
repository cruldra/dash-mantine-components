import os
from flask import Flask, jsonify, redirect, request
import dash
from dash import html, dcc
import json
import hashlib
import dongjak_dash_components as ddc
from dongjak_dash_components.auth_plugin import create_auth_app
flask_server = Flask(__name__, instance_relative_config=False)


def login(username, password):
    if  username=="dongjak" and  password == '123394':
        user_info = {
            'username': username 
        }
        user_info_json = json.dumps(user_info)
        hashed_user_info = hashlib.md5(user_info_json.encode()).hexdigest()
        return hashed_user_info

flask_server =create_auth_app(flask_server, login, auth_app_routes_pathname_prefix="/auth/", main_app_routes_pathname_prefix="/app/", login_url="/login")
 



#region 用于主应用的Dash应用
main_app = dash.Dash(
        server=flask_server,
        routes_pathname_prefix="/app/",
    )
main_app.layout = html.Div(
    children=[
        dcc.Input(
            id="input-1-state",
            type="text",
            value="Montréal",
        ),
        dcc.Input(
            id="input-2-state",
            type="text",
            value="Canada",
        ),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Div(id='output-state'),
    ]
)

@main_app.callback(
    dash.dependencies.Output('output-state', 'children'),
    dash.dependencies.Input('submit-button-state', 'n_clicks') 
)
def update_output(n_clicks):
    session_id = request.cookies.get('sessionId')
    msg = f"当前会话ID是{session_id}"
    return msg
#endregion

# @app.route('/')
# def hello():
#     print(f"当前请求的路径是{request.url}")
#     # Check if authentication header exists
#     if 'Authorization' not in request.headers:
#         # Redirect to login page
#         return redirect('/login')

#     return 'Hello, World!'

if __name__ == '__main__':
    os.environ["REACT_VERSION"] = "18.2.0"
    flask_server.run(host='0.0.0.0', debug=True)
