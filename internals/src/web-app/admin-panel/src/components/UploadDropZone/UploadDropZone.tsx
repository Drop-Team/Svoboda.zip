import { PrimitiveYegorsBullshitCodeButton } from '@components/PrimitiveYegorsBullshitCodeButton';
import * as React from 'react';
import styles from './UploadDropZone.module.scss';
import { useDropzone } from 'react-dropzone'
import { useFileUpload } from '@hooks/useFileUpload';

interface UploadDropZoneProps {

}

export const UploadDropZone: React.FunctionComponent<UploadDropZoneProps> = (props) => {
  const onFileUpload = useFileUpload();

  const {getRootProps, getInputProps, isDragActive} = useDropzone({ onDrop: onFileUpload })

  return <div 
    className={styles["upload-drop-zone"]}
    {...getRootProps()}
  >
    <input {...getInputProps()}/>
    <PrimitiveYegorsBullshitCodeButton 
      text='+ Загрузить ZIPP' 
      type='wide' 
      callback={() => {}}
    />

    <span> или перетяните zipp сюда </span>
  </div>
}