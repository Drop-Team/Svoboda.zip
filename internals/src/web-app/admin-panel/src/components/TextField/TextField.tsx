import React from "react";
import styles from "./TextField.module.scss";

interface TextFieldProps {
  placeholder: string;
  type: string;
}

export const TextField: React.FunctionComponent<TextFieldProps> = (props) => {
  return <input placeholder="Search..." className={styles["text-field"]}></input>;
}


