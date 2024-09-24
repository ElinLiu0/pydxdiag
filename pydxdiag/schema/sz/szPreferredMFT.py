# Author: Elin
# Date: 2024-09-06 09:26:51
# Last Modified by:   Elin
# Last Modified time: 2024-09-06 09:26:51

from pydantic import (
    BaseModel,
    Field,
)

class szPreferredMFT(BaseModel):
    """
    Class to represent a preferred MFT of a sz file.\n
    :params Name: Name of the preferred MFT
    :type Name: str
    :params EngineID: Engine ID of the preferred MFT
    :type EngineID: str
    :params EngineType: Engine type of the preferred MFT
    :type EngineType: str
    """
    Name: str = Field(...)
    EngineID: str = Field(...)
    EngineType: str = Field(...)