from fastapi import APIRouter, Request

from ..utils import utils

router = APIRouter(prefix="/zipps")


@router.get("/")
def get_zipps(request: Request):
    zipps_data = utils.Utils().get_zipps_list()
    for zipp_data in zipps_data:
        zipp_data["icon"] = str(request.base_url) + "zipps_static/" + zipp_data["icon"]
    return {"zipps": zipps_data}


@router.post("/{zipp_directory_name}/start")
def start_zipp(request: Request, zipp_directory_name):
    utils.Utils().start_zipp(zipp_directory_name)
