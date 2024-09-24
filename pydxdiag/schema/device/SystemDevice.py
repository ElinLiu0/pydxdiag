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


class SystemDevice(BaseModel):
    """
    Class to describe basic information for a system device.\n
    :params Name: The name of the device.
    :type Name: str
    :params DeviceKey: The device key.
    :type DeviceKey: str
    :params Drivers: The drivers of the device.
    :type Drivers: List[Driver]
    """
    Name: str = Field(..., title="Name", description="The name of the device.")
    DeviceKey: str = Field(..., title="DeviceKey", description="The device key.")
    Drivers: List[Driver] = Field(..., title="Drivers", description="The drivers of the device.")