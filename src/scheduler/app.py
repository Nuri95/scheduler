from typing import Optional

from fastapi import FastAPI

from scheduler.api import router

app = FastAPI(
    title='Schedule',
    description='Сервис для планирования задач',
    version='1.0.0'
)
app.include_router(router)


@app.get('/')
def read_root():
    return {'Hello': 'World'}
