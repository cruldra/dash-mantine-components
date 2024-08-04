import {DashBaseProps} from "../../props/dash";
import React, {FC} from "react";

interface Props extends DashBaseProps {
    input?: React.ReactNode;
    output?: React.ReactNode;
}

const FunctionCall: FC<Props> = ({
                                     input,
                                     output,
                                     ...rest
                                 }) => {
    return <div style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "row",
        gap: "1rem",
    }} {...rest}>

        <div style={{
            display: "flex",
            flexDirection: "column",
            rowGap: "1rem",
        }}>
            {input}
        </div>

        <div style={{
            display: "flex",
            flexDirection: "column",
            rowGap: "1rem",
            flex: 1,
        }}>
            {output}
        </div>
    </div>
};


export default FunctionCall;
