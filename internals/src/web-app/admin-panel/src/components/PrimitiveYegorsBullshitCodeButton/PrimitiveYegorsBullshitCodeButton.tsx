import React from "react";
import styles from "./PrimitiveYegorsBullshitCodeButton.module.scss";

interface BullshitCodeButtonProps {
  text: string;
  type: string;

  callback: CallableFunction;
}

export const PrimitiveYegorsBullshitCodeButton:React.FunctionComponent<BullshitCodeButtonProps> =
    (props) => {

  return <button className={styles["button-" + props.type]} onClick={() => {props.callback()}}>
      {props.text}
    </button>;
}
