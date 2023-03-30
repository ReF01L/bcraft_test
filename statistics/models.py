from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.orm import Session

from app.database import Base


class Statistic(Base):
    event_date = Column(Date)
    views = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    cost = Column(Float(2), default=0)

    def save(self, db: Session, is_new: bool = False):
        if is_new:
            db.add(self)

        db.commit()
        db.refresh(self)

        return self