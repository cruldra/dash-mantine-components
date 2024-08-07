import os
from flask import Flask, jsonify, redirect, request
import dash
from dash import html, dcc
import json
import hashlib
import dongjak_dash_components as ddc
app = Flask(__name__, instance_relative_config=False)

#region  用于认证的Dash应用
auth_app = dash.Dash(
        server=app ,
          routes_pathname_prefix="/auth/",
    )
auth_app.layout =  ddc.MantineProvider(
   ddc. UsernamePasswordLogin()
)
 

@auth_app.callback(
    dash.dependencies.Output ('url', 'pathname'),
    dash.dependencies.Input('submit-button', 'n_clicks'),
    dash.dependencies.State('username-input', 'value'),
    dash.dependencies.State('password-input', 'value')
)
def update_output(n_clicks, username, password):
    if n_clicks > 0:
        token = login(username, password)
        a =f"token={token}"
        print(a)
        if token is None:
            return 'Unauthorized'
        #response = app.make_response(redirect('/app/'))
        #response.set_cookie('token', token)
        return "/app/"
    return 'Submit'

#endregion


# region 全局请求拦截器 
# @app.before_request
# def before_request_func():
    # 1. 如果请求的是 /login 且 方法是GET，则直接返回
    # if request.path.startswith('/auth/') :
    #     return
    # if request.path == '/login/' and request.method == 'GET':
    #     return

    # # 2. 如果请求的是/login 且方法是POST，则从request.form中获取用户名和密码，然后调用 login 函数进行登录验证,返回一个token，通过cookie的方式返回给客户端
    # if request.path == '/login' and request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     token = login(username, password)
    #     if token is None:
    #         return 'Unauthorized', 401
    #     response = app.make_response(redirect('/'))
    #     response.set_cookie('token', token)
    #     return response

    # 3. 如果请求的是其他路径，则判断cookie中是否有token，如果没有则返回401，如果有则继续执行
    # if 'token' not in request.cookies:
    #     return 'Unauthorized', 401

# endregion

def login(username, password):
    if  username=="dongjak" and  password == '123394':
        user_info = {
            'username': username 
        }
        user_info_json = json.dumps(user_info)
        hashed_user_info = hashlib.md5(user_info_json.encode()).hexdigest()
        return hashed_user_info

#region 用于主应用的Dash应用
main_app = dash.Dash(
        server=app,
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
    app.run(host='0.0.0.0', debug=True)
