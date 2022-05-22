import React from "react"

export const useFileUpload = () => {
  return React.useCallback((acceptedFiles: File[]) => {
    const formData = new FormData();
    formData.append("file", acceptedFiles[0]);

    return fetch('http://localhost:8000/zipps', { method: 'POST', body: formData })
  }, [])
}