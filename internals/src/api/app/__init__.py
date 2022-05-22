import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .utils.utils import add_local_zipp
from .utils.utils import Utils
from .utils.func import get_config_data


web_app = FastAPI()


def start():
    add_local_zipp('qdqw', "C:/Projects/Programming/Svoboda.zip/internals/src/api/run.zip")
    web_app.mount("/zipps_static", StaticFiles(directory=Utils().zipp_dir), name="zipps")

    web_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from .routers import zipps

    web_app.include_router(zipps.router)

    config = get_config_data()

    uvicorn.run(
        "app:web_app",
        host=config['host'], port=config['port'],
        forwarded_allow_ips="*"
    )
