import * as React from 'react';
import styles from './Button.module.scss';

const defaultColors = {
  "blue": "0x00AEE0",
  "gray": "0xA4A4A4",
}

interface ButtonProps {
  color: keyof typeof defaultColors | string;
}

export const Button: React.FunctionComponent<ButtonProps> = (props) => {
  return (
    <button 
      className={styles["button"]}
      style={computeColorStyle(props)}>
      
    </button>
  );
}

function computeColorStyle(props: ButtonProps): React.CSSProperties | undefined {
  let colorValue = defaultColors[props.color as keyof typeof defaultColors] ?? props.color;

  return 
}
