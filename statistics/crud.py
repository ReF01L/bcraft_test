from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from statistics import models, schemas
from statistics.enums import SortingMethod


def create_statistic(db: Session, statistic: schemas.StatisticCreate) -> models.Statistic:
    db_stat = models.Statistic(**statistic.dict())  # type: ignore
    db_stat.save(db, is_new=True)

    return db_stat

def get_statistics(
        db: Session,
        from_at: date,
        to: date,
        sorting_method: SortingMethod
) -> list[models.Statistic]:
    query = db.query(
        models.Statistic.event_date,
        func.sum(models.Statistic.cost).label(SortingMethod.COST.value),
        func.sum(models.Statistic.views).label(SortingMethod.VIEWS.value),
        func.sum(models.Statistic.clicks).label(SortingMethod.CLICKS.value),
        (func.sum(models.Statistic.cost) / func.sum(models.Statistic.clicks)).label(SortingMethod.CPC.value),
        (func.sum(models.Statistic.cost) / func.sum(models.Statistic.views)).label(SortingMethod.CPM.value)
    )

    query = query.filter(
        models.Statistic.event_date.between(from_at, to)  # type: ignore
    ).group_by(models.Statistic.event_date).order_by(desc(sorting_method.value))

    return query.all()


def drop_table(db: Session):
    try:
        db.query(models.Statistic).delete()
        db.commit()

        return {'status': 'Success'}
    except Exception as ex:
        return {
            'status': 'Error',
            'detail': ex
        }
