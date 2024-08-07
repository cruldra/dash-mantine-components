
from typing import Callable
import dash
from flask import Flask, jsonify, redirect, request

import dongjak_dash_components as ddc
def create_auth_app(flask_server:Flask,
                    login_handler:Callable[[str, str], str] ,
                    auth_app_routes_pathname_prefix:str="/auth/",
                    main_app_routes_pathname_prefix:str="/app/",
                    login_url:str="/login" 
                    ):

    with flask_server.app_context():
        auth_app = dash.Dash( server=flask_server , routes_pathname_prefix=auth_app_routes_pathname_prefix, )
        auth_app.layout =  ddc.MantineProvider(
        ddc. UsernamePasswordLogin(login_url)
        )
        @flask_server.before_request
        def before_request_func():
            # 1. 如果请求的是 /login 且 方法是GET，则直接返回
            if request.path.startswith(auth_app_routes_pathname_prefix) :
                return
            # if request.path == '/login/' and request.method == 'GET':
            #     return

            # 2. 如果请求的是/login 且方法是POST，则从request.form中获取用户名和密码，然后调用 login 函数进行登录验证,返回一个token，通过cookie的方式返回给客户端
            if request.path == login_url and request.method == 'POST':
                form = request.get_json()
                sessionId = login_handler(form['username'], form['password'])
                if sessionId is None:
                    return {
                        'message': '用户名或密码错误',
                        "success": False 
                    }, 401
                response = flask_server.make_response(jsonify({
                    'message': 'success',
                    'success': True,
                    "redirectUrl":main_app_routes_pathname_prefix
                }))
                response.set_cookie('sessionId', sessionId)
                return response

            # 3. 如果请求的是其他路径，则判断cookie中是否有token，如果没有则返回401，如果有则继续执行
            if 'sessionId' not in request.cookies:
                response = flask_server.make_response(redirect(auth_app_routes_pathname_prefix))
                return response, 401
    return flask_server