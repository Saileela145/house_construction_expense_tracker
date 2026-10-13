from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.plumbing_expenses_schema import PlumbingExpenses
from services.plumbing_expenses_service import (
    add_plumbing_expenses_service,
    get_plumbing_expenses_service,
    get_plumbing_metrics)

router = APIRouter(prefix="/plumbing_expenses", tags=["plumbing_expenses"])

@router.post("/")
def add_plumbing_expenses(
        request: PlumbingExpenses,
        db : Session = Depends(get_db)
):
    print(f'Router:add_plumbing_expenses={request}')
    return add_plumbing_expenses_service(db, request)

@router.get("/")
def get_plumbing_expenses(
     db : Session = Depends(get_db)
):
    return get_plumbing_expenses_service(db=db)


@router.get("/metrics")
def get_plumbing_metrics_api(
    start_date: str = None,
    end_date: str = None,
    stage: str = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    return get_plumbing_metrics(
        db=db,
        start_date=start_date,
        end_date=end_date,
        stage=stage,
        category=category
    )
