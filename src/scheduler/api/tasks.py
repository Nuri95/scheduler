from typing import List

from fastapi import (
    APIRouter,
    Depends,
)


from scheduler.models.tasks import (
    Task,
    TaskCreate,
)
from scheduler.services.tasks import TasksService

tasks_router = APIRouter(
    prefix='/tasks',
    tags=['tasks'],
)


@tasks_router.get('/', response_model=List[Task])
def get_tasks(service: TasksService = Depends()):
    return service.get_list()


@tasks_router.post('/', response_model=Task)
def create_task(
    task_data: TaskCreate,
    user_id: int,
    service: TasksService = Depends()
):
    return service.create(user_id, task_data)