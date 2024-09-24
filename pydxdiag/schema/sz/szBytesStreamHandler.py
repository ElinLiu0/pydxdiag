# Author: Elin
# Date: 2024-09-06 09:14:58
# Last Modified by:   Elin
# Last Modified time: 2024-09-06 09:14:58

from pydantic import (
    BaseModel,
    Field,
)

class szBytesStreamHandler(BaseModel):
    """
    Class to represent a szBytesStreamHandler.\n
    :params Name: Name of the szBytesStreamHandler
    :type Name: str
    :params HandlerID: Handler ID
    :type HandlerID: str
    :params SupportedFormat: Supported formats
    :type SupportedFormat: str
    :params IsPreferred: Is preferred
    :type IsPreferred: bool
    """
    Name: str = Field(...)
    HandlerID: str = Field(...)
    SupportedFormat: str = Field(...)
    IsPreferred: bool = Field(...)