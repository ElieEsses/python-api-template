import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.config import APP_NAME, APP_VERSION, settings
from src.app.routes import auth, example, health

logging.basicConfig(
    level=logging.DEBUG if settings.debug_mode else logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


app = FastAPI(title=APP_NAME, version=APP_VERSION, port=settings.port)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(example.router, prefix="/api", tags=["Example"])
