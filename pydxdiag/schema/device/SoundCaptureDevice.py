from pydantic import (
    BaseModel,
    Field,
)
from typing import *
from datetime import datetime

class SoundCaptureDevice(BaseModel):
    """
    Class to represent the sound capture device.\n
    :params Description: Description of the sound capture device.
    :type Description: str
    :params DriverName: Driver name of the sound capture device.
    :type DriverName: str
    :params DriverVersion: Driver version of the sound capture device.
    :type DriverVersion: str
    :params DriverLanguage: Driver language of the sound capture device.
    :type DriverLanguage: str
    :params IsBetaDriver: Whether the driver is a beta driver or not.
    :type IsBetaDriver: bool
    :params IsDebugDriver: Whether the driver is a debug driver or not.
    :type IsDebugDriver: bool
    :params DriverDate: Date of the driver.
    :type DriverDate: datetime
    :params DriverSize: Size of the driver binaries.
    :type DriverSize: int
    :params DefaultSoundRecording: Whether the sound capture device is the default sound recording device.
    :type DefaultSoundRecording: bool
    :params DefaultVoiceRecording: Whether the sound capture device is the default voice recording device.
    :type DefaultVoiceRecording: bool
    :params Flags: Flags of the sound capture device.
    :type Flags: int
    :params Formats: Formats of the sound capture device.
    :type Formats: int
    """
    Description: str = Field(..., title="Description", description="Description of the sound capture device.")
    DriverName: str = Field(..., title="DriverName", description="Driver name of the sound capture device.")
    DriverVersion: str = Field(..., title="DriverVersion", description="Driver version of the sound capture device.")
    DriverLanguage: str = Field(..., title="DriverLanguage", description="Driver language of the sound capture device.")
    IsBetaDriver: bool = Field(..., title="IsBetaDriver", description="Whether the driver is a beta driver or not.")
    IsDebugDriver: bool = Field(..., title="IsDebugDriver", description="Whether the driver is a debug driver or not.")
    DriverDate: datetime = Field(..., title="DriverDate", description="Date of the driver.")
    DriverSize: int = Field(..., title="DriverSize", description="Size of the driver binaries.")
    DefaultSoundRecording: bool = Field(..., title="DefaultSoundRecording", description="Whether the sound capture device is the default sound recording device.")
    DefaultVoiceRecording: bool = Field(..., title="DefaultVoiceRecording", description="Whether the sound capture device is the default voice recording device.")
    Flags: int = Field(..., title="Flags", description="Flags of the sound capture device.")
    Formats: int = Field(..., title="Formats", description="Formats of the sound capture device.")
