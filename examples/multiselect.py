import dash_mantine_components as dmc
from dash import Dash, Input, Output, html, State, dcc
from datetime import datetime, timedelta

app = Dash(__name__)


app.layout = html.Div(
    [
        dmc.MultiSelect(
            id="multi",
            options=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
                {"value": "riot", "label": "Riot"},
                {"value": "next", "label": "Next.js"},
                {"value": "blitz", "label": "Blitz.js"},
            ],
        ),
        dmc.Space(h=20),
        dmc.Text(id="text"),
    ]
)


@app.callback(
    Output("text", "children"), Input("multi", "value"), prevent_initial_call=True
)
def modal(value):
    return ", ".join(value) if value else ""


if __name__ == "__main__":
    app.run_server(debug=True)