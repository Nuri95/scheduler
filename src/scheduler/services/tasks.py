from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from scheduler.sql_app import tables
from scheduler.sql_app.database import get_session


class TasksService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Task]:
        return self.session.query(tables.Task).all()

    def create(self, user_id: int, task_data):
        task = tables.Task(
            **task_data.dict(),
            user_id=user_id,
        )
        self.session.add(task)
        self.session.commit()

        return task
