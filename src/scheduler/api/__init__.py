from fastapi import APIRouter

from scheduler.api.auth import auth_router
from scheduler.api.tasks import tasks_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(tasks_router)