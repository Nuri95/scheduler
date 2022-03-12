from typing import List

from fastapi import (
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from starlette import status

from scheduler.models.tasks import TaskUpdate
from scheduler.sql_app import tables
from scheduler.sql_app.database import get_session


class TasksService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, task_id: int):
        task = (
            self
            .session
            .query(tables.Task)
            .filter_by(
                id=task_id,
                user_id=user_id
            )
            .first()
        )
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return task

    def get_list(self, user_id: int) -> List[tables.Task]:
        return (
            self
            .session
            .query(tables.Task)
            .filter_by(user_id=user_id)
            .all()
        )

    def create(self, user_id: int, task_data) -> tables.Task:
        task = tables.Task(
            **task_data.dict(),
            user_id=user_id,
        )
        self.session.add(task)
        self.session.commit()

        return task

    def update(self, user_id: int, task_id: int, task_data: TaskUpdate) -> tables.Task:
        task = self._get(user_id, task_id)

        for field, value in task_data:
            setattr(task, field, value)

        self.session.commit()

        return task

    def delete(self, user_id: int, task_id: int):
        task = self._get(user_id, task_id)

        self.session.delete(task)
        self.session.commit()
