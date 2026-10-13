from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.site_expenses_schema import SiteExpenses
from services.site_expenses_service import (
    add_site_expenses_service,get_site_expenses_service,get_site_metrics)

router = APIRouter(prefix="/site_expenses", tags=["site_expenses"])

@router.post("/")
def add_site_expenses(
        request: SiteExpenses,
        db : Session = Depends(get_db)
):
    print(f'Router:add_site_expenses={request}')
    return add_site_expenses_service(db, request)

@router.get("/")
def get_site_expenses(
     db : Session = Depends(get_db)
):
    return get_site_expenses_service(db=db)

@router.get("/metrics")
def get_site_metrics_api(
    start_date: str = None,
    end_date: str = None,
    stage: str = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    return get_site_metrics(
        db=db,
        start_date=start_date,
        end_date=end_date,
        stage=stage,
        category=category,
    )