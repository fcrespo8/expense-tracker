from sqlalchemy.orm import Session
from app import models, schemas


def create_expense(db: Session, expense: schemas.ExpenseCreate) -> models.Expense:
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)  # recarga el objeto con el id que generó la BD
    return db_expense


def get_expenses(db: Session) -> list[models.Expense]:
    return db.query(models.Expense).all()
