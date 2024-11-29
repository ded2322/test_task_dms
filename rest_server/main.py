from fastapi import FastAPI
from routers.router import notes_router, task_router

app = FastAPI(title="Rest server")

app.include_router(notes_router)
app.include_router(task_router)
