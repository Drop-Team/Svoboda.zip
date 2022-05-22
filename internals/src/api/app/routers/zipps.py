from fastapi import APIRouter, Request, HTTPException
import urllib

from ..utils import utils
from ..utils import errors

router = APIRouter(prefix="/zipps")


def get_url_safe(url):
    return urllib.parse.quote(url, safe='/:?=&')


@router.get("/")
def get_zipps(request: Request):
    zipps_data = utils.Utils().get_zipps_list()
    for zipp_data in zipps_data:
        zipp_data["icon"] = str(request.base_url) + "zipps_static/" + zipp_data["icon"]
        zipp_data["start"] = get_url_safe(str(request.base_url) + "zipps/" + zipp_data["directory_name"] + "/start")
        zipp_data["delete"] = get_url_safe(str(request.base_url) + "zipps/" + zipp_data["directory_name"])
    return {"zipps": zipps_data}


@router.post("/{zipp_directory_name}/start")
def start_zipp(request: Request, zipp_directory_name):
    try:
        utils.Utils().start_zipp(zipp_directory_name)
        return "success"
    except errors.ZippError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.post("/{zipp_directory_name}/help")
def get_zipp_md(request: Request, zipp_directory_name):
    try:
        return utils.Utils().get_zipp_markdown(zipp_directory_name)
    except errors.ZippError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.delete("/{zipp_directory_name}")
def delete_zipp(request: Request, zipp_directory_name):
    try:
        utils.Utils().delete_zipp(zipp_directory_name)
        return "success"
    except errors.ZippError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)