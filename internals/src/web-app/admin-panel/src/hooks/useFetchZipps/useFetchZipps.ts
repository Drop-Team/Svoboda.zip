import { Zipp, Zipps } from "typings/index";
import useFetch from "@hooks/useFetch";

export const useFetchZipps = () : [Zipp[] | undefined, CallableFunction] => {
  const [zipps, updateZipps] = useFetch<Zipps>("http://10.91.10.20:8000/zipps/");

  return [zipps?.zipps, updateZipps]
}