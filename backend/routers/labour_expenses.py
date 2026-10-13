from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.labour_expenses_schema import LabourExpenses
from services.labour_expenses_service import (
    add_labour_expenses_service,
    get_labour_expenses_service,
    get_labour_metrics,
)

router = APIRouter(prefix="/labour_expenses", tags=["labour_expenses"])

@router.post("/")
def add_labour_expenses(
        request: LabourExpenses,
        db : Session = Depends(get_db)
):
    print(f'Router:add_labour_expenses={request}')
    return add_labour_expenses_service(db, request)

@router.get("/")
def get_labour_expenses(
     db : Session = Depends(get_db)
):
    return get_labour_expenses_service(db=db)


@router.get("/metrics")
def get_labour_expenses_metrics(
    start_date: str = None,
    end_date: str = None,
    stage: str = None,
    labour_type: str = None,
    db: Session = Depends(get_db)
):
    return get_labour_metrics(
        db=db,
        start_date=start_date,
        end_date=end_date,
        stage=stage,
        labour_type=labour_type
    )