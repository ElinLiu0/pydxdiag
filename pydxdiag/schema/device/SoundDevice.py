from pydantic import (
    BaseModel,
    Field,
)
from typing import *
from datetime import datetime

class BufferStatics(BaseModel):
    """
    Buffer Static for All kinds.\n
    :params AllBuffers: All buffers.
    :type AllBuffers: int
    :params StaticBuffers: Static buffers.
    :type StaticBuffers: int
    :params StreamingBuffers: Streaming buffers.
    :type StreamingBuffers: int
    """
    AllBuffers: int = Field(
        ...,
        description="All buffers."
    )
    StaticBuffers: int = Field(
        ...,
        description="Static buffers."
    )
    StreamingBuffers: int = Field(
        ...,
        description="Streaming buffers."
    )

class MaxHwMixingBufferInfo(BufferStatics):
    """
    Class to represent the maximum hardware mixing buffer information.\n
    Inherits from `BufferStatics`.
    """
    pass

class MaxHw3DBufferInfo(BufferStatics):
    """
    Class to represent the maximum hardware 3D buffer information.\n
    Inherits from `BufferStatics`.
    """
    pass

class FreeHwMixingBufferInfo(BufferStatics):
    """
    Class to represent the free hardware mixing buffer information.\n
    Inherits from `BufferStatics`.
    """
    pass

class FreeHw3DBufferInfo(BufferStatics):
    """
    Class to represent the free hardware 3D buffer information.\n
    Inherits from `BufferStatics`.
    """
    pass


class SoundDevice(BaseModel):
    """
    A class to represent the sound device of a computer.\n
    :params Description: The description of the sound device.
    :type Description: str
    :params HardwareID: The hardware ID of the sound device.
    :type HardwareID: str
    :params ManufacturerID: The manufacturer ID of the sound device.
    :type ManufacturerID: Optional[str]
    :params ProductID: The product ID of the sound device.
    :type ProductID: Optional[str]
    :params Type: The type of the sound device.
    :type Type: Optional[str]
    :params DriverName: The name of the driver of the sound device.
    :type DriverName: str
    :params DriverVersion: The version of the driver of the sound device.
    :type DriverVersion: str
    :params DriverLanguage: The language of the driver of the sound device.
    :type DriverLanguage: str
    :parms IsBetaDriver: Whether the driver of the sound device is a beta driver.
    :type IsBetaDriver: bool
    :params IsDebugDriver: Whether the driver of the sound device is a debug driver.
    :type IsDebugDriver: bool
    :params WHQLLogo: Whether the driver of the sound device is WHQL logo.
    :type WHQLLogo: bool
    :params DriverDate: The date of the driver of the sound device.
    :type DriverDate: datetime
    :params DriverSize: The size of the driver binaries
    :type DriverSize: int
    :params OtherFiles: Other files associated with the sound device.
    :type OtherFiles: Optional[Any]
    :params DriverProvider: The provider of the driver of the sound device.
    :type DriverProvider: str
    :params HwAccelLevel: The hardware acceleration level of the sound device.
    :type HwAccelLevel: str
    :params DefaultSoundPlayback: The default sound playback device.
    :type DefaultSoundPlayback: bool
    :params DefaultVoicePlayback: The default voice playback device.
    :type DefaultVoicePlayback: bool
    :params VoiceManager: The voice manager of the sound device.
    :type VoiceManager: int
    :params EAX20Listener: Is this Device EAX 2.0 Listener Supported
    :type EAX20Listener: bool
    :params EAX20Source: Is this Device an EAX 2.0 Source 
    :type EAX20Source: bool
    :params I3DL2Listener: Is this Device an I3DL2 Listener
    :type I3DL2Listener: bool
    :params I3DL2Source: Is this Device an I3DL2 Source
    :type I3DL2Source: bool
    :params ZoomFX: Is this Device ZoomFX Supported
    :type ZoomFX: bool
    :params Flags: Flags for the sound device.
    :type Flags: int
    :params MinSecondarySampleRate: Minimum secondary sample rate
    :type MinSecondarySampleRate: int
    :params MaxSecondarySampleRate: Maximum secondary sample rate
    :type MaxSecondarySampleRate: int
    :params PrimaryBuffers: Primary buffers
    :type PrimaryBuffers: int
    :params MaxHwMixingBuffers: Maximum hardware mixing buffers
    :type MaxHwMixingBuffers: MaxHwMixingAllBufferInfo
    :params FreeHwMixingBuffers: Free hardware mixing buffers
    :type FreeHwMixingBuffers: FreeHwMixingBufferInfo
    :params FreeHw3DAllBuffers: Free hardware 3D buffers
    :type FreeHw3DAllBuffers: FreeHw3DAllBufferInfo
    :params TotalHwMemBytes: Total hardware memory in bytes
    :type TotalHwMemBytes: int
    :params FreeHwMemBytes: Free hardware memory in bytes
    :type FreeHwMemBytes: int
    :params MaxContigFreeHwMemBytes: Maximum contiguous memory in bytes
    :type MaxContigFreeHwMemBytes: int
    :params UnlockTransferRateHwBuffers: Unlock transfer rate hardware buffers
    :type UnlockTransferRateHwBuffers: int
    :params PlayCPUOverheadSwBuffers: Play CPU overhead software buffers
    :type PlayCPUOverheadSwBuffers: int
    """
    Description: str = Field(..., description="The description of the sound device.")
    HardwareID: str = Field(..., description="The hardware ID of the sound device.")
    ManufacturerID: Optional[str] = Field(None, description="The manufacturer ID of the sound device.")
    ProductID: Optional[str] = Field(None, description="The product ID of the sound device.")
    Type: Optional[str] = Field(..., description="The type of the sound device.")
    DriverName: str = Field(..., description="The name of the driver of the sound device.")
    DriverVersion: str = Field(..., description="The version of the driver of the sound device.")
    DriverLanguage: str = Field(..., description="The language of the driver of the sound device.")
    IsBetaDriver: bool = Field(..., description="Whether the driver of the sound device is a beta driver.")
    IsDebugDriver: bool = Field(..., description="Whether the driver of the sound device is a debug driver.")
    WHQLLogo: bool = Field(..., description="Whether the driver of the sound device is WHQL logo.")
    DriverDate: datetime = Field(..., description="The date of the driver of the sound device.")
    DriverSize: int = Field(..., description="The size of the driver binaries")
    OtherFiles: Optional[Any] = Field(None, description="Other files associated with the sound device.")
    DriverProvider: str = Field(..., description="The provider of the driver of the sound device.")
    HwAccelLevel: str = Field(..., description="The hardware acceleration level of the sound device.")
    DefaultSoundPlayback: bool = Field(..., description="The default sound playback device.")
    DefaultVoicePlayback: bool = Field(..., description="The default voice playback device.")
    VoiceManager: int = Field(..., description="The voice manager of the sound device.")
    EAX20Listener: bool = Field(..., description="Is this Device EAX 2.0 Listener Supported")
    EAX20Source: bool = Field(..., description="Is this Device an EAX 2.0 Source")
    I3DL2Listener: bool = Field(..., description="Is this Device an I3DL2 Listener")
    I3DL2Source: bool = Field(..., description="Is this Device an I3DL2 Source")
    ZoomFX: bool = Field(..., description="Is this Device ZoomFX Supported")
    Flags: int = Field(..., description="Flags for the sound device.")
    MinSecondarySampleRate: int = Field(..., description="Minimum secondary sample rate")
    MaxSecondarySampleRate: int = Field(..., description="Maximum secondary sample rate")
    PrimaryBuffers: int = Field(..., description="Primary buffers")
    MaxHwMixingBuffers: MaxHwMixingBufferInfo = Field(..., description="Maximum hardware mixing buffers")
    MaxHw3DBuffers: MaxHw3DBufferInfo = Field(..., description="Maximum hardware 3D buffers")
    FreeHwMixingBuffers: FreeHwMixingBufferInfo = Field(..., description="Free hardware mixing buffers")
    FreeHw3DBuffers: FreeHw3DBufferInfo = Field(..., description="Free hardware 3D buffers")
    TotalHwMemBytes: int = Field(..., description="Total hardware memory in bytes")
    FreeHwMemBytes: int = Field(..., description="Free hardware memory in bytes")
    MaxContigFreeHwMemBytes: int = Field(..., description="Maximum contiguous memory in bytes")
    UnlockTransferRateHwBuffers: int = Field(..., description="Unlock transfer rate hardware buffers")
    PlayCPUOverheadSwBuffers: int = Field(..., description="Play CPU overhead software buffers")
    

