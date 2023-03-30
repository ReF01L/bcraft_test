from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy import func

from statistics import models, schemas


def create_statistic(db: Session, statistic: schemas.StatisticCreate) -> models.Statistic:
    db_stat = models.Statistic(**statistic.dict())  # type: ignore
    db_stat.save(db, is_new=True)

    return db_stat

def get_statistics(db: Session, from_at: date, to: date) -> list[models.Statistic]:
    query = db.query(
        models.Statistic.event_date,
        func.sum(models.Statistic.cost).label('cost'),
        func.sum(models.Statistic.views).label('views'),
        func.sum(models.Statistic.clicks).label('clicks')
    )

    query = query.filter(
        models.Statistic.event_date.between(from_at, to)  # type: ignore
    ).order_by(models.Statistic.event_date.desc()).group_by(models.Statistic.event_date)  # type: ignore

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