import { PrimitiveYegorsBullshitCodeButton } from '@components/PrimitiveYegorsBullshitCodeButton';
import * as React from 'react';
import styles from './UploadDropZone.module.scss';
import { useDropzone } from 'react-dropzone'
import { useFileUpload } from '@hooks/useFileUpload';

interface UploadDropZoneProps {
  onUploadSuccess?: CallableFunction;
}

export const UploadDropZone: React.FunctionComponent<UploadDropZoneProps> = (props) => {
  const onFileUpload = useFileUpload();

  const onDrop = async (acceptedFiles : File[]) => {
    await onFileUpload(acceptedFiles);
    props.onUploadSuccess?.();
  }

  const {getRootProps, getInputProps, isDragActive} = useDropzone({ onDrop })

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