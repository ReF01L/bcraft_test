from enum import Enum

class ErrorMessage(Enum):
    NEGATIVE_VALUE = '%s cannot be less than zero'
    INVALID_DATE_FORMAT = 'Invalid date format: %s'

class ResponseDescription(Enum):
    BAD_REQUEST = 'Bad request'


class ResponseDetail(Enum):
    INVALID_DATE_FORMAT = 'Invalid date format'


class SortingMethod(Enum):
    EVENT_DATE = 'event_date'
    VIEWS = 'views'
    CLICKS = 'clicks'
    COST = 'cost'
    CPC = 'cpc'
    CPM = 'cpm'
