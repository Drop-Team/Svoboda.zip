from fastapi import APIRouter, Request, HTTPException, responses, File, UploadFile
import urllib
import os

from ..utils import utils
from ..utils import errors

router = APIRouter(prefix="/zipps")


def get_url_safe(url):
    return urllib.parse.quote(url, safe='/:?=&')


@router.get("/")
async def get_zipps(request: Request):
    zipps_data = utils.Utils().get_zipps_list()
    for zipp_data in zipps_data:
        zipp_data["icon"] = str(request.base_url) + "zipps_static/" + zipp_data["icon"]
        zipp_data["start"] = get_url_safe(str(request.base_url) + "zipps/" + zipp_data["directory_name"] + "/start")
        zipp_data["delete"] = get_url_safe(str(request.base_url) + "zipps/" + zipp_data["directory_name"])
        zipp_data["help"] = get_url_safe(str(request.base_url) + "zipps/" + zipp_data["directory_name"] + "/help")
    return {"zipps": zipps_data}


@router.post("/{zipp_directory_name}/start")
async def start_zipp(request: Request, zipp_directory_name):
    try:
        utils.Utils().start_zipp(zipp_directory_name)
        return "success"
    except errors.ZippError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.get("/{zipp_directory_name}/help", response_class=responses.HTMLResponse)
async def get_zipp_md(request: Request, zipp_directory_name):
    try:
        return utils.Utils().get_zipp_markdown(zipp_directory_name)
    except errors.ZippError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.delete("/{zipp_directory_name}")
async def delete_zipp(request: Request, zipp_directory_name):
    try:
        utils.Utils().delete_zipp(zipp_directory_name)
        return "success"
    except errors.ZippError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@router.post("/")
async def add_zipp(request: Request, file: UploadFile):
    contents = await file.read()
    utils.Utils().add_local_zipp(contents)
