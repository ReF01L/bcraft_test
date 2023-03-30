from datetime import date, datetime

import typing
from pydantic import BaseModel, validator
from pydantic.utils import GetterDict

from app.core.config import settings
from statistics.enums import ErrorMessage


class StatisticBase(BaseModel):
    event_date: date
    views: int = 0
    clicks: int = 0
    cost: int = 0


class StatisticGetter(GetterDict):
    def get(self, key: str, default: typing.Any = None) -> typing.Any:
        if key == 'cpc':
            if self._obj.clicks == 0:
                return None
            return self._obj.cost / self._obj.clicks
        elif key == 'cpm':
            if self._obj.views == 0:
                return None
            return self._obj.cost / self._obj.views * 1000

        return getattr(self._obj, key)


class Statistic(StatisticBase):
    cpc: float
    cpm: float

    class Config:
        orm_mode = True
        getter_dict = StatisticGetter


class StatisticCreate(StatisticBase):
    @validator("views", pre=True)
    def parse_views(cls, value: int):
        if value < 0:
            raise ValueError(ErrorMessage.NEGATIVE_VALUE.value % 'Views')
        return value

    @validator("clicks", pre=True)
    def parse_clicks(cls, value: int):
        if value < 0:
            raise ValueError(ErrorMessage.NEGATIVE_VALUE.value % 'Clicks')
        return value

    @validator("cost", pre=True)
    def parse_cost(cls, value: int):
        if value < 0:
            raise ValueError(ErrorMessage.NEGATIVE_VALUE.value % 'Cost')
        return value

    @validator("event_date", pre=True)
    def parse_event_date(cls, value: str):
        try:
            return datetime.strptime(value, settings.DATETIME_FORMAT).date()
        except ValueError as ex:
            raise ValueError(ErrorMessage.INVALID_DATETIME_FORMAT.value % value) from ex
