import uvicorn

from scheduler.settings import settings

uvicorn.run(
    'scheduler.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
