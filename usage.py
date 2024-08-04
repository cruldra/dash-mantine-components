import os
from datetime import date, datetime

from dash import Dash, html, dcc, callback, Output, Input
import dongjak_dash_components as dmc
from dash_iconify import DashIconify

from demos.date_picker import simple_ui as date_picker_simple_ui
from demos.function_call import ui as function_call_ui


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]
app = Dash(__name__, external_stylesheets=stylesheets, suppress_callback_exceptions=True)
server = app.server
menus = html.Div(
    style={"width": 240,
           "background": "#313131",
           },
    children=[

        dmc.NavLink(
            label="日期时间",
            leftSection=get_icon(icon="iconoir:user"),
            children=[
                dmc.NavLink(
                    label="日期选择框",
                    leftSection=get_icon(icon="iconoir:user"),
                    href="/date-picker",
                )
            ],
        ),
        dmc.NavLink(
            label="布局",
            leftSection=get_icon(icon="iconoir:user"),
            children=[
                dmc.NavLink(
                    label="函数调用",
                    leftSection=get_icon(icon="iconoir:user"),
                    href="/function-call",
                )
            ],
        )
    ],
)

main_content = html.Div(
    style={"flex": 1,

           # "border": "1px solid",
           },
    children=dmc.DatesProvider(
        id="main-content",
        settings={"locale": "zh-cn", "firstDayOfWeek": 0, "weekendDays": [0]}
    ),

)

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    theme={
        "primaryColor": "indigo",
        "fontFamily": "'Inter', sans-serif",
        "components": {
            "Button": {"defaultProps": {"fw": 400}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
            "Badge": {"styles": {"root": {"fontWeight": 500}}},
            "Progress": {"styles": {"label": {"fontWeight": 500}}},
            "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
            "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
            "Table": {
                "defaultProps": {
                    "highlightOnHover": True,
                    "withTableBorder": True,
                    "verticalSpacing": "sm",
                    "horizontalSpacing": "md",
                }
            },
        },
    },
    children=[
        dmc.NotificationProvider(position="top-right"),
        dcc.Location(id='url', refresh=False),
        html.Div(
            style={
                "display": "flex",
                "direction": "row",
                "margin": "20px",
                "gap": "20px",

            },
            children=[menus, main_content]
        )
    ]

)


@callback(
    Output('main-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/date-picker':
        return date_picker_simple_ui
    elif pathname == '/function-call':
        return function_call_ui


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG", "True").lower() == "true", port=8090)
