import React from "react";
import styles from "./SvobodaZipLogo.module.scss";

interface SvobodaZipLogoProps {}

export const SvobodaZipLogo: React.FunctionComponent<SvobodaZipLogoProps> = (props) => {
  return <span className={styles["logo-text"]}>
    Свобода<span className={styles["blue"]}>.zip</span>
  </span>;
}
