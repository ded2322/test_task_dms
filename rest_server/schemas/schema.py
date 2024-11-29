from pydantic import BaseModel, Field


class NotesSchema(BaseModel):
    notes:str = Field(max_length=120)
    description:str = Field(max_length=1024)