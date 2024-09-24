from pydantic import (
    BaseModel,
    Field,
)
from typing import *
from datetime import datetime

class Driver(BaseModel):
    """
    Class to desribe basic information for a input related device driver.\n
    :params Name: The name of the driver.
    :type Name: str
    :params InstallationPath: The installation path of the driver.
    :type InstallationPath: str
    :params Version: The version of the driver.
    :type Version: str
    :params Language: The language of the driver.
    :type Language: str
    :params IsBetaDriver: Whether the driver is a beta driver or not.
    :type IsBetaDriver: bool
    :params IsDebugDriver: Whether the driver is a debug driver or not.
    :type IsDebugDriver: bool
    :params Date: The date of the driver.
    :type Date: Optional[datetime]
    :params Size: The size of the driver.
    :type Size: int
    """
    Name: str = Field(..., title="Name", description="The name of the driver.")
    InstallationPath: str = Field(..., title="InstallationPath", description="The installation path of the driver.")
    Version: str = Field(..., title="Version", description="The version of the driver.")
    Language: str = Field(..., title="Language", description="The language of the driver.")
    IsBetaDriver: bool = Field(..., title="IsBetaDriver", description="Whether the driver is a beta driver or not.")
    IsDebugDriver: bool = Field(..., title="IsDebugDriver", description="Whether the driver is a debug driver or not.")
    Date: Optional[datetime] = Field(None, title="Date", description="The date of the driver.")
    Size: int = Field(..., title="Size", description="The size of the driver.")


class InputRelatedDevice(BaseModel):
    """
    Class representing an input related device.\n
    :params Description: The description of the device.
    :type Description: str
    :params VendorID: The vendor ID of the device.
    :type VendorID: int
    :params ProductID: The product ID of the device.
    :type ProductID: int
    :params Location: The location of the device.
    :type Location: str
    :params MatchingDeviceID: The matching device ID.
    :type MatchingDeviceID: str
    :params UpperFilters: The upper filters.
    :type UpperFilters: Optional[Any] 
    :params LowerFilters: The lower filters.
    :type LowerFilters: Optional[Any] 
    :params Service: The service.
    :type Service: str
    :params OEMData: The OEM data.
    :type OEMData: Optional[str]
    :params Flags1: The flags1.
    :type Flags1: Optional[int]
    :params Flags2: The flags2.
    :type Flags2: Optional[int]
    :params Drivers: The drivers.
    :type Drivers: List[Driver]
    :params Type: The type of the device.
    :type Type: str
    """
    Description: str = Field(..., title="Description", description="The description of the device.")
    VendorID: int = Field(..., title="VendorID", description="The vendor ID of the device.")
    ProductID: int = Field(..., title="ProductID", description="The product ID of the device.")
    Location: str = Field(..., title="Location", description="The location of the device.")
    MatchingDeviceID: str = Field(..., title="MatchingDeviceID", description="The matching device ID.")
    UpperFilters: Optional[Any] = Field(..., title="UpperFilters", description="The upper filters.")
    LowerFilters: Optional[Any] = Field(..., title="LowerFilters", description="The lower filters.")
    Service: str = Field(..., title="Service", description="The service.")
    OEMData: Optional[str] = Field(..., title="OEMData", description="The OEM data.")
    # TODO: Maybe int for flags?
    Flags1: Optional[int] = Field(..., title="Flags1", description="The flags1.")
    Flags2: Optional[int] = Field(..., title="Flags2", description="The flags2.")
    Drivers: List[Driver] = Field(..., title="Drivers", description="The drivers.")
    Type: str = Field(..., title="Type", description="The type of the device.")

