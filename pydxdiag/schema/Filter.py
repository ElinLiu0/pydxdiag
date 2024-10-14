from pydantic import (
    BaseModel,
    Field,
)
from typing import Optional

class Filter(BaseModel):
    """
    Class to represent a filter for DirectShow section of dxdiag output.\n
    :params Name: Name of the filter
    :type Name: str
    :params FilterCategory: Filter category
    :type FilterCategory: str
    :params Merit: Merit value of the filter
    :type Merit: int
    :params Inputs: Filter inputs
    :type Inputs: int
    :params Outputs: Filter outputs
    :type Outputs: int
    :params File: File name of the filter   
    :type File: str
    :params FileVersion: File version of the filter
    :type FileVersion: str
    """
    Name: str = Field(...)
    FilterCategory: str = Field(...)
    Merit: int = Field(...)
    Inputs: int = Field(...)
    Outputs: int = Field(...)
    File: str = Field(...)
    FileVersion: str = Field(...)

class PreferredDShowFilters(BaseModel):
    """
    A class to store the preferred direct show filters\n
    :params MediaSubType: The media subtype of the filter
    :type MediaSubType: Optional[str]
    :params Name: The name of the filter
    :type Name: Optional[str]
    :params CLSIDType: The CLSID type of the filter
    :type CLSIDType: Optional[str]
    """
    MediaSubType:Optional[str] = Field(
        None,
        title="Media Sub Type",
        description="The media subtype of the filter"
    )
    Name:Optional[str] = Field(
        None,
        title="Name",
        description="The name of the filter"
    )
    CLSIDType:Optional[str] = Field(
        None,
        title="CLSID Type",
        description="The CLSID type of the filter"
    )
