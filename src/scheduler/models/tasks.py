from typing import Optional

from pydantic.main import BaseModel


class TaskBase(BaseModel):
    header: str
    is_finished: bool
    description: Optional[str]


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass
