import React, {useEffect, useState} from "react";

export const useHelpContent = (url: string) => {
    const [data, setData] = useState<string|null> (null);

    const fetchData = () => {
        fetch(url)
            .then((res) => {
                return res.text();
            })
            .then((res) => {
                setData(res);
            });
    }

    useEffect(() => {
       fetchData();
    }, [url]);

    return data;
}