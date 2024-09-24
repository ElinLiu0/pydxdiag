from pydantic import (
    BaseModel,
    Field,
)
from typing import *
from datetime import datetime

class DirectInputDevice(BaseModel):
    """
    Class representing a DirectInput device.\n
    :params DeviceName: The name of the device.
    :type DeviceName: str
    :params Attached: Whether the device is attached.
    :type Attached: bool
    :params JoyStickID: The ID of the joystick.
    :type JoyStickID: Optional[int]
    :params VendorID: The vendor ID of the device.
    :type VendorID: int
    :params ProductID: The product ID of the device.
    :type ProductID: int
    :params FFDriverName: The name of the force feedback driver.
    :type FFDriverName: Optional[str]
    :params FFDriverDate: The date of the force feedback driver.
    :type FFDriverDate: Optional[datetime]
    :params FFDriverVersion: The version of the force feedback driver.
    :type FFDriverVersion: Optional[str]
    :params FFDriverSize: The size of the force feedback driver.
    :type FFDriverSize: int
    """
    DeviceName: str = Field(..., title="DeviceName", description="The name of the device.")
    Attached: bool = Field(..., title="Attached", description="Whether the device is attached.")
    JoyStickID: Optional[int] = Field(..., title="JoyStickID", description="The ID of the joystick.")
    VendorID: int = Field(..., title="VendorID", description="The vendor ID of the device.")
    ProductID: int = Field(..., title="ProductID", description="The product ID of the device.")
    FFDriverName: Optional[str] = Field(..., title="FFDriverName", description="The name of the force feedback driver.")
    FFDriverDate: Optional[datetime] = Field(None, title="FFDriverDate", description="The date of the force feedback driver.")
    FFDriverVersion: Optional[str] = Field(..., title="FFDriverVersion", description="The version of the force feedback driver.")
    FFDriverSize: int = Field(..., title="FFDriverSize", description="The size of the force feedback driver.")
