import React from "react";
import styles from './Dashboard.module.scss';

interface DashboardProps {

}

export const Dashboard: React.FunctionComponent<DashboardProps> = (props) => {
  return <div className={styles["dashboard"]}>
    Свобода zip
  </div>;
}
