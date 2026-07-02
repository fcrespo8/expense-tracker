from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("", response_model=schemas.ExpenseOut, status_code=status.HTTP_201_CREATED)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)


@router.get("", response_model=list[schemas.ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)
