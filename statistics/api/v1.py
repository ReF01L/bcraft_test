from datetime import datetime, date

from fastapi import APIRouter, Depends, HTTPException, status, Query
from pydantic import Required
from sqlalchemy.orm import Session

from app import dependency as global_dependency
from app.core.config import settings
from statistics import schemas, crud
from statistics.enums import ErrorMessage, SortingMethod

router = APIRouter(prefix='/api/v1/stat', tags=['stat', 'web'])


@router.post(
    '/',
    response_model=schemas.Statistic,
    description='Метод сохранения статистики'
)
async def create_statistics(
        statistic: schemas.StatisticCreate,
        db: Session = Depends(global_dependency.get_db)
):
    return crud.create_statistic(db, statistic)


@router.get(
    '/',
    response_model=list[schemas.Statistic],
    description='Метод показа статистики'
)
async def get_statistics(
        from_at: str = Query(default=Required),
        to: str = Query(default=Required),
        sorting: SortingMethod = Query(default=SortingMethod.EVENT_DATE),
        db: Session = Depends(global_dependency.get_db)
):
    try:
        starting_at: date = datetime.strptime(from_at, settings.DATETIME_FORMAT).date()
        finishing_at: date = datetime.strptime(to, settings.DATETIME_FORMAT).date()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorMessage.INVALID_DATETIME_FORMAT.value % f'{from_at} \ {to}'
        )

    stats = crud.get_statistics(db, starting_at, finishing_at, sorting)

    return stats

@router.delete(
    '/',
    response_model=dict[str, str],
    description='Метод сброса статистики'
)
async def drop_statistics(db: Session = Depends(global_dependency.get_db)):
    return crud.drop_table(db)
