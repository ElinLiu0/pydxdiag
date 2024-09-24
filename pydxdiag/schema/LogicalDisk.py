

from pydantic import (
    BaseModel,
    Field,
)
from typing import *
from datetime import datetime


class LogicalDisk(BaseModel):
    """
    Class to describe basic information for a logical disk.\n
    :params DriveLetter: The drive letter of the logical disk.
    :type DriveLetter: str
    :params FreeSpace: The free space of the logical disk in bytes.
    :type FreeSpace: int
    :params MaxSpace: The max space of the logical disk in bytes.
    :type MaxSpace: int
    :params FileSystem: The file system of the logical disk.
    :type FileSystem: str
    :params Model: The model of the logical disk.
    :type Model: str
    :params PNPDeviceID: The PNP device ID of the logical disk.
    :type PNPDeviceID: str
    :params HardDriveIndex: The driver index of the logical disk.
    :type HardDriveIndex: int
    """
    DriveLetter: str = Field(..., title="DriveLetter", description="The drive letter of the logical disk.")
    FreeSpace: int = Field(..., title="FreeSpace", description="The free space of the logical disk in bytes.")
    MaxSpace: int = Field(..., title="MaxSpace", description="The max space of the logical disk in bytes.")
    FileSystem: str = Field(..., title="FileSystem", description="The file system of the logical disk.")
    Model: str = Field(..., title="Model", description="The model of the logical disk.")
    PNPDeviceID: str = Field(..., title="PNPDeviceID", description="The PNP device ID of the logical disk.")
    HardDriveIndex: int = Field(..., title="HardDriveIndex", description="The driver index of the logical disk.")