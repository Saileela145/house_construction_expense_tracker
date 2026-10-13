from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.painting_expenses_schema import PaintingExpenses
from services.painting_expenses_service import (
    add_painting_expenses_service,get_painting_expenses_service,get_painting_metrics)

router = APIRouter(prefix="/painting_expenses", tags=["painting_expenses"])

@router.post("/")
def add_painting_expenses(
        request: PaintingExpenses,
        db : Session = Depends(get_db)):
    print(f'Router:add_painting_expenses={request}')
    return add_painting_expenses_service(db, request)

@router.get("/")
def get_painting_expenses(
     db : Session = Depends(get_db)):
    return get_painting_expenses_service(db=db)


@router.get("/metrics")
def get_painting_metrics_api(
    start_date: str = None,
    end_date: str = None,
    stage: str = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    return get_painting_metrics(
        db=db,
        start_date=start_date,
        end_date=end_date,
        stage=stage,
        category=category
    )