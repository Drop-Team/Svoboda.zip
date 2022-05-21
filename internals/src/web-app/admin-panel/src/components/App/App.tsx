import { Button } from '@components/Button';
import { ZippCard } from '@components/ZippCard';
import * as React from 'react';
import styles from './App.module.scss';

interface AppProps {

}

export const App: React.FunctionComponent<AppProps> = (props) => {
  return <div className={styles["showcase"]}>
    <Button color={"blue"}/>
  </div>
}