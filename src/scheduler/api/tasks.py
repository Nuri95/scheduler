from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Response
)
from starlette import status

from scheduler.models.auth import User
from scheduler.models.tasks import (
    Task,
    TaskCreate,
    TaskUpdate,
)
from scheduler.services.auth import get_current_user
from scheduler.services.tasks import TasksService

tasks_router = APIRouter(
    prefix='/tasks',
    tags=['tasks'],
)


@tasks_router.get('/', response_model=List[Task])
def get_tasks(
    service: TasksService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.get_list(user.id)


@tasks_router.post('/', response_model=Task)
def create_task(
    task_data: TaskCreate,
    user: User = Depends(get_current_user),
    service: TasksService = Depends()
):
    return service.create(user.id, task_data)


@tasks_router.put('/{task_id}')
def update_task(
    task_id: int,
    task_data: TaskUpdate = Depends(),
    user: User = Depends(get_current_user),
    service: TasksService = Depends(),
):
    return service.update(user.id, task_id, task_data)


@tasks_router.delete('/{task_id}')
def delete_task(
    task_id: int,
    user: User = Depends(get_current_user),
    service: TasksService = Depends()
):
    service.delete(user.id, task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
