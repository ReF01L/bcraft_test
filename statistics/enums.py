from enum import Enum

class ErrorMessage(Enum):
    NEGATIVE_VALUE = '%s cannot be less than zero'
    INVALID_DATETIME_FORMAT = 'Invalid date format: %s'