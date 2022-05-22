import { SvobodaZipLogo } from "@components/SvobodaZipLogo";
import { TextField } from "@components/TextField";
import { UploadDropZone } from "@components/UploadDropZone";
import { ZippCard } from "@components/ZippCard";
import { useFetchZipps } from "@hooks/useFetchZipps";
import { Zipp } from "@typings/index";

import React, {useCallback, useEffect, useReducer, useState} from "react";
import styles from './Dashboard.module.scss';

interface DashboardProps {

}

export const Dashboard: React.FunctionComponent<DashboardProps> = (props) => {
  const [zipps, updateZipps] = useFetchZipps();

  console.log("Render")

  const zippCards:JSX.Element[] = [];
  if (zipps !== undefined) {

    zipps.forEach((item, index) => {

      const startCallback = () => {

        const options = {
          method: "POST"
        }

        fetch(item.start, options)
            .then((res) => {
              return res.json();
            })
      }

      const deleteCallback = () => {
        const options = {
          method: "DELETE"
        }

        fetch(item.delete, options)
              .then(() => {
                updateZipps();
              });
      }

      zippCards.push(
          <ZippCard key={index}
                    zippName={item.name}
                    zippDescription={item.description}
                    zippVersion={item.version}
                    zippType={item.type}
                    zippIcon={item.icon}
                    zippSize={item.size}

                    zippStartCallback={startCallback}
                    zippDeleteCallback={deleteCallback}/>
      );
    });
  } else {
    zippCards.push(
        <h1 key={0}>Лоадинг</h1>
    );
  }

  return <div className={styles["dashboard"]}>
    <div className={styles["header"]}>

      <SvobodaZipLogo />

      <div className={styles["menu"]}>
        <button className={styles["button"]}>Помощь</button>
        <button className={styles["button"]}>Настройки</button>
        <button className={styles["button"]}>Остановить</button>
      </div>
    </div>

    <div className={styles["content"]}>
      <TextField placeholder="Hello" type="wide"/>

      <UploadDropZone onUploadSuccess={ updateZipps }/>

      <div className={styles["zipp-cards-list"]}>
        { zippCards }
      </div>
    </div>
  </div>;
}
