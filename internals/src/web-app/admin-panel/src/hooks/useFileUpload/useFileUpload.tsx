import React from "react"

export const useFileUpload = () => {
  return React.useCallback((acceptedFiles: File[]) => {
    const formData = new FormData();
    formData.append("file", acceptedFiles[0]);

    fetch('http://10.91.10.20:8000/zipps', { method: 'POST', body: formData })
      .then(res => res.json())
  }, [])
}