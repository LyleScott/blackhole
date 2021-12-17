import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from blackhole.controllers import router

# Initialize logging.
logging.basicConfig(format="[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s")
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)


# Initialize FastAPI.
app = FastAPI(
    title="Blackhole",
    version=".007",
    description="Send anything in, never see it again!",
    docs_url=None,
    redoc_url="/docs",
    debug=True,
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Add URL routers.
app.include_router(router)

# Add middlewares.
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
