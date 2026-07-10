import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
def health():
    logger.info("Health check initiated")
    return {"message": "Health check passed", "status": "ok"}
