# Author: Elin
# Date: 2024-09-06 09:04:56
# Last Modified by:   Elin
# Last Modified time: 2024-09-06 09:04:56

from pydantic import (
    BaseModel,
    Field,
)

class szMFFileVersion(BaseModel):
    """
    Class to represent a file version of a szm file.\n
    :params Name: Name of the file
    :type Name: str
    :params Version: Version of the file
    :type Version: str
    """
    Name: str = Field(...)
    Version: str = Field(...)