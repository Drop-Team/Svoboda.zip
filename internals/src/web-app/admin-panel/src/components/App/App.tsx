import { Dashboard } from "@components/Dashboard";
import * as React from 'react';
import styles from './App.module.scss';

interface AppProps {

}

export const App: React.FunctionComponent<AppProps> = (props) => {
  return (<div className={styles["App"]}>
    <Dashboard />

  </div>);
}