import dongjak_dash_components as dmc

ui = dmc.FunctionCall(
    [
        dmc.NumberInput(
            id="input-tokens",
            label="输入token数量",
            value=1,
            min=1,
            placeholder="输入token数量"
        ),
        dmc.DatePicker(
            id="date-picker-input",
            label="Start Date",
            description="You can also provide a description",
            w=250,
        )
    ], 2,"11111"
)
