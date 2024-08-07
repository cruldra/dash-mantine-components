from datetime import date, datetime

from dash import html, callback, Output, Input
from dash.exceptions import PreventUpdate

import dongjak_dash_components as dmc

simple_ui = html.Div(
    [
          dmc. UsernamePasswordLogin(),
        dmc.DatePicker(
            id="date-picker-input",
            label="Start Date",
            description="You can also provide a description",
            minDate=date(2020, 8, 5),
            value=datetime.now().date(),  # or string in the format "YYYY-MM-DD"
            w=250,
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-input"),
    ]
)


@callback(
    Output("selected-date-input", "children"),
    Input("date-picker-input", "value")
)
def update_output(d):
    prefix = "You have selected: "
    if d:
        return prefix + d
    else:
        raise PreventUpdate
