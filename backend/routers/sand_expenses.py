from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.sand_expenses_schema import SandExpenses
from services.sand_expenses_service import (
    add_sand_expenses_service,get_sand_expenses_service,get_sand_metrics)

router = APIRouter(prefix="/sand_expenses", tags=["sand_expenses"])

@router.post("/")
def add_send_expenses(
        request: SandExpenses,
        db : Session = Depends(get_db)
):
    print(f'Router:add_sand_expenses={request}')
    return add_sand_expenses_service(db, request)

@router.get("/")
def get_sand_expenses(
     db : Session = Depends(get_db)
):
    return get_sand_expenses_service(db=db)

@router.get("/metrics")
def get_sand_metrics_api(
    start_date: str = None,
    end_date: str = None,
    stage: str = None,
    vendor: str = None,
    db: Session = Depends(get_db)
):
    return get_sand_metrics(
        db=db,
        start_date=start_date,
        end_date=end_date,
        stage=stage,
        vendor=vendor,
    )