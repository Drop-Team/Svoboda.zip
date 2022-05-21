import * as React from 'react';
import styles from './ZippCard.module.scss';
import {PrimitiveYegorsBullshitCodeButton} from "@components/PrimitiveYegorsBullshitCodeButton";

interface ZippCardProps {
    zippName: string;
    zippDescription: string;
    zippVersion: string;
    zippType: string;
    zippIcon: string;
    zippSize: string;

    zippStartCallback: CallableFunction;
    zippDeleteCallback: CallableFunction;
}

export const ZippCard: React.FunctionComponent<ZippCardProps> = (props) => {
  return <div className={styles["zipp-card"]}>
      <div className={styles["picture-container"]}>
          <img className={styles["img"]} src={props.zippIcon}></img>
      </div>
      
      <div className={styles["header"]}>
        <span className={styles["name"]}> {props.zippName} </span>
        <span className={styles["version"]}> v.{props.zippVersion} </span>
      </div>

      <div className={styles["type"]}>
          {props.zippType} zipp
      </div>
      
      <div className={styles["description"]}>
          {props.zippDescription}
      </div>
      
      <div className={styles["controls"]}>
          <PrimitiveYegorsBullshitCodeButton callback={props.zippStartCallback} text="Start" type="wide" />
          <PrimitiveYegorsBullshitCodeButton callback={props.zippDeleteCallback} text="D" type="normal" />
          <PrimitiveYegorsBullshitCodeButton callback={props.zippStartCallback} text="?" type="normal" />
      </div>

      <div className={styles["info"]}>
          {props.zippSize}
      </div>
  </div>
}