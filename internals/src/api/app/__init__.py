import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .utils.utils import Utils

web_app = FastAPI()


def start():
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

    uvicorn.run(
        "app:web_app",
        host="0.0.0.0", port=8000,
        forwarded_allow_ips="*"
    )
