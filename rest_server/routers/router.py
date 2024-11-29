from fastapi import APIRouter, HTTPException, status

from orm.base_orm import BaseOrm
from schemas.schema import NotesSchema

notes_router = APIRouter(prefix="/notes", tags=["Notes"])

task_router =APIRouter(prefix="/tasks", tags=["Tasks"])


@notes_router.get("", status_code=200, summary="Return all notes")
async def all_notes():
    """Возвращает все записи из таблицы Notes"""
    notes = await BaseOrm.show_all_notes()
    return notes


@notes_router.get("/{item_id}", status_code=200, summary="Returns а note by id")
async def found_notes(item_id:int):
    """Находит notes по id, в случае не находа 404 ошибка """
    data = await BaseOrm.found_one_or_none(id = item_id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return data

@notes_router.post("", status_code=201, summary="Create note")
async def create_notes(data_notes: NotesSchema):
    """Создает notes"""
    id_notes = await BaseOrm.insert_data(note = data_notes.notes, description= data_notes.description)
    return {"id" : id_notes}



@task_router.put("/{item_id}", status_code=200, summary="Update note")
async def update_note(item_id:int, update_data: NotesSchema):
    """Обновляет notes по id"""
    data = await BaseOrm.found_one_or_none(id = item_id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    await BaseOrm.update_data(id = item_id, note= update_data.notes, description= update_data.description)


@task_router.delete("/{item_id}", status_code=200, description="Delete note")
async def delete_tasks(item_id:int):
    """По id удаляет notes"""
    data = await BaseOrm.found_one_or_none(id = item_id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    await BaseOrm.delete_data(id= item_id)

