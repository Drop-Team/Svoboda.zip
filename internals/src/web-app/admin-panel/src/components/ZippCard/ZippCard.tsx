import * as React from 'react';
import styles from './ZippCard.module.scss';

interface ZippCardProps {

}

export const ZippCard: React.FunctionComponent<ZippCardProps> = (props) => {
  return <div className={styles["zipp-card"]}>
      <div className={styles["picture-container"]}>
        pic
      </div>
      
      <div className={styles["header"]}>
        <span className={styles["name"]}> Wikipedia </span>
        <span className={styles["version"]}> v0.0.1 </span>
      </div>

      <div className={styles["type"]}>
        web zipp
      </div>
      
      <div className={styles["description"]}>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pellentesque
      </div>
      
      <div className={styles["controls"]}>
        controls
      </div>

      <div className={styles["info"]}>
        info
      </div>
  </div>
}