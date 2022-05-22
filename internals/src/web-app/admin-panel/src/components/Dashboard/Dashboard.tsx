import { SvobodaZipLogo } from "@components/SvobodaZipLogo";
import { TextField } from "@components/TextField";
import { UploadDropZone } from "@components/UploadDropZone";
import { ZippCard } from "@components/ZippCard";
import { useFetchZipps } from "@hooks/useFetchZipps";
import { Zipp, Zipps } from "@typings/index";

import React, {useCallback, useEffect, useReducer, useState} from "react";
import styles from './Dashboard.module.scss';
import { HelpPage } from "@components/HelpPage";

interface DashboardProps {

}

export const Dashboard: React.FunctionComponent<DashboardProps> = (props) => {
  const [zipps, updateZipps] = useFetch<Zipps>("http://10.91.10.20:8000/zipps/");
  
  const [helpPage, setHelpPage] = useState<HelpPageType>({
    opened: false,
    linkToContent: null,
    title: null,
  });

  const zippCards:JSX.Element[] = [];
  if (zipps !== undefined) {

    zipps.zipps.forEach((item, index) => {

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

      const helpCallback = () => {
        setHelpPage({
          opened: true,
          linkToContent: item.help,
          title: item.name + " - Справка по ZIPP",
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
                    zippDeleteCallback={deleteCallback}
                    zippHelpCallback={helpCallback}/>
      );
    });
  } else {
    zippCards.push(
        <h1 key={0}>Лоадинг</h1>
    );
  }

  const closeCallback = () => {
    setHelpPage({
      opened: false,
      linkToContent: null,
      title: null,
    });
  }
  const helpPageJSX = <HelpPage opened={helpPage.opened}
                                linkToContent={helpPage.linkToContent}
                                closeCallback={closeCallback}
                                title={helpPage.title}/>;

  return <div className={styles["dashboard"]}>
    <div className={styles["header"]}>

      <SvobodaZipLogo />

      <div className={styles["menu"]}>
        <button className={styles["button"]}>Помощь</button>
        <button className={styles["button"]}>Настройки</button>
        <button className={styles["button"]}>Остановить</button>
      </div>
    </div>

    { helpPageJSX }

    <div className={styles["content"]}>
      <TextField placeholder="Hello" type="wide"/>

      <UploadDropZone onUploadSuccess={ updateZipps }/>

      <div className={styles["zipp-cards-list"]}>
        { zippCards }
      </div>
    </div>
  </div>;
}

type HelpPageType = {
  opened: boolean,
  linkToContent: string | null,
  title: string | null,
}
