from pydantic import (
    BaseModel,
    Field,
)

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