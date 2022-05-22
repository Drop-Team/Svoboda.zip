import React, {useEffect, useState} from "react";

export default function useFetch<D> (url:string) : [D|null, CallableFunction] {
    const [data, setData] = useState <D | null> (null);

    const fetchData = () => {
        fetch(url)
            .then((res) => {
                return res.json();
            })
            .then((res) => {
                setData(res);
            })
    }

    useEffect(() => {
        fetchData();
    }, []);

    return [data, fetchData];
}

