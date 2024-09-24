# Author: Elin
# Date: 2024-09-06 09:16:38
# Last Modified by:   Elin
# Last Modified time: 2024-09-06 09:16:38

from pydantic import (
    BaseModel,
    Field,
)

class szSchemeHandlers(BaseModel):
    """
    Class to represent a scheme handler of a sz file.\n
    :params Name: Name of the scheme handler
    :type Name: str
    :parmas HandlerID: Handler ID of the scheme handler
    :type HandlerID: str
    :params SupportedFormat: Supported format of the scheme handler
    :type SupportedFormat: str
    :params IsPreferred: Is the scheme handler preferred
    :type IsPreferred: bool
    """
    Name: str = Field(...)
    HandlerID: str = Field(...)
    SupportedFormat: str = Field(...)
    IsPreferred: bool = Field(...)