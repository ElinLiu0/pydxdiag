# Author: Elin
# Date: 2024-09-06 09:07:57
# Last Modified by:   Elin
# Last Modified time: 2024-09-06 09:07:57

from pydantic import (
    BaseModel,
    Field
)

class szMFT(BaseModel):
    """
    Class to represent a szMFT Engine.\n
    :params Name: Name of the szMFT Engine
    :type Name: str
    :params EngineID: Engine ID
    :type EngineID: str
    :params Flag1: Flags of the Engine
    :type Flag1: int
    :params Flag2: Flags of the Engine
    :type Flag2: int
    :params EngineFile: Engine file name
    :type EngineFile: str
    :params EngineFileVersion: Engine file version
    :type EngineFileVersion: str
    :params EngineType: Engine type
    :type EngineType: str
    """
    Name: str = Field(...)
    EngineID: str = Field(...)
    Flag1: int = Field(...)
    Flag2: int = Field(...)
    EngineFile: str = Field(...)
    EngineFileVersion: str = Field(...)
    EngineType: str = Field(...)