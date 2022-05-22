import React, {useState} from "react";
import styles from "./HelpPage.module.scss";
import useFetch from "@hooks/useFetch";
import {useHelpContent} from "@hooks/useHelpContent";

interface HelpPageProps {
  opened: boolean;
  linkToContent: string | null;
  title: string | null;

  closeCallback: CallableFunction;
}

export const HelpPage:React.FunctionComponent<HelpPageProps> = (props) => {

  let content = useHelpContent(props.linkToContent === null ? "" : props.linkToContent);
  const style = props.opened ? styles["helpPage"] : styles["hidden"];

  return <div className={style}>

    <button onClick={() => {props.closeCallback()}} className={styles["close-button"]}>X</button>
    <div className={styles["content"]}>
      <h1>{ props.title }</h1>
      <div dangerouslySetInnerHTML={{ __html: content === null ? "<p>Лоадинг</p>" : content }}></div>
    </div>
  </div>;
}


