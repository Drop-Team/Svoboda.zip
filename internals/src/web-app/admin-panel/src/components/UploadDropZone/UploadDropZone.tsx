import { PrimitiveYegorsBullshitCodeButton } from '@components/PrimitiveYegorsBullshitCodeButton';
import * as React from 'react';
import styles from './UploadDropZone.module.scss';

interface UploadDropZoneProps {

}

export const UploadDropZone: React.FunctionComponent<UploadDropZoneProps> = (props) => {
  return <div className={styles["upload-drop-zone"]}>
    <PrimitiveYegorsBullshitCodeButton 
      text='+ Загрузить ZIPP' 
      type='wide' 
      callback={() => {alert("bruh")}}/
    >

    <span> или перетяните zipp сюда </span>
  </div>
}