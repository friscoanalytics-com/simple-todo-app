from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from app.app_db import get_db, engine, Base
from app.models import Todos
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Todo Service API",
    description="APIs related to todo service",
    docs_url=f"/docs",
    redoc_url=f"/redoc",
    openapi_url=f"/openapi.json",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"], 
    allow_headers=["*"],
)

db = get_db()

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(TodoCreate):
    id: int

@app.get("/", include_in_schema=False)
async def original_endpoint():
    return RedirectResponse(url=f"/docs")

@app.get("/todos", response_model=List[TodoResponse])
async def get_todos(db: Session = Depends(get_db)):
    return db.query(Todos).all()

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todos(title=todo.title, completed=todo.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db_todo.title = todo.title
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted"}


Base.metadata.create_all(bind=engine)