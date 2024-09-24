from pydantic import (
    BaseModel,
    Field
)
from typing import *


class MachineInformation(BaseModel):
    """
    A class for storing the basic information of the device.\n
    :params MachineName: The name of the machine
    :types MachineName: str
    :params MachineId: The ID of the machine
    :types MachineId: str
    """
    MachineName:str = Field(
        ...,
        title="Machine Name",
        description="The name of the machine"
    )
    MachineId:str = Field(
        ...,
        title="Machine ID",
        description="The ID of the machine"
    )

class OSInformation(BaseModel):
    """
    A class for storing the OS information of the device.\n
    :params Name: The name of the OS
    :types Name: str
    :params Version: The version of the OS
    :types Version: int
    :params Bit: The bit of the OS
    :types Bit: int
    :params BuildId: The build ID of the OS
    :types BuildId: int
    :params ReleaseId: The release ID of the OS
    :types ReleaseId: str
    :params Language: The language of the OS
    :types Language: str
    """
    Name:str = Field(
        ...,
        title="OS Name",
        description="The name of the OS"
    )
    # Examples: 10,11,7,8
    Version:int = Field(
        ...,
        title="OS Version",
        description="The version of the OS"
    )
    Bit:int = Field(
        ...,
        title="OS Bit",
        description="The bit of the OS"
    )
    BuildId:int = Field(
        ...,
        title="OS Build ID",
        description="The build ID of the OS"
    )
    ReleaseId:str = Field(
        ...,
        title="OS Release ID",
        description="The release ID of the OS"
    )
    Language:str = Field(
        ...,
        title="OS Language",
        description="The language of the OS"
    )

class SystemModelInformation(BaseModel):
    """
    A class storage for the system model information\n
    whether if your machine is an OEM model or not.\n
    :params SystemManufacturer: The manufacturer of the system
    :types SystemManufacturer: str
    :params SystemModel: The model of the system
    :types SystemModel: str
    """
    SystemManufacturer:str = Field(
        ...,
        title="System Manufacturer",
        description="The manufacturer name of the system"
    )
    SystemModel:str = Field(
        ...,
        title="System Model",
        description="The model name of the system"
    )

class FirmwareInformation(BaseModel):
    """
    A class for storaging the firmware information\n
    :params FirmwareType: The type of the firmware
    :types FirmwareType: str
    :params BIOSVersion: The BIOS version
    :types BIOSVersion: str
    """
    FirmwareType:str = Field(
        ...,
        title="Firmware Type",
        description="The type of the firmware"
    )
    BIOSVersion:str = Field(
        ...,
        title="BIOS Version",
        description="The BIOS version"
    )

class CPUInformation(BaseModel):
    """
    A class for storing the CPU information from device.\n
    :params Gen: The generation of the CPU
    :types Gen: Optional[int]
    :params BaseClock: The base clock frequency of the current CPU
    :types BaseClock: float
    :params Threads: The number of threads of the current CPU
    :types Threads: int
    :params Brand: The brand of the CPU
    :types Brand: str
    :params Name: The name of the CPU
    :types Name: str
    """
    # FIXME: Although Windows on ARM is now available.
    # But we still need to consider the x86 architecture.
    # Probably would add capability with Qualcomm Snapdragon if i truly have one. 
    # RIP :(
    Gen:Optional[int] = Field(
        ...,
        title="CPU Generation",
        description="The generation of the CPU"
    )
    BaseClock:float = Field(
        ...,
        title="Base Clock",
        description="The base clock frquency of the current CPU"
    )
    # FIXME: Since after 12th generation, Intel has changed the architecture of the CPU.
    # With P and E core inside one CPU.So it's hard to predict how much P cores and E cores
    # Inside a Intel CPU after 12th generation.
    # So i decide record threads only here.
    # RIP :(
    Threads:int = Field(
        ...,
        title="Threads",
        description="The number of threads of the current CPU"
    )
    Brand:str = Field(
        ...,
        title="CPU Brand",
        description="The brand of the CPU"
    )
    Name:str = Field(
        ...,
        title="CPU Name",
        description="The name of the CPU"
    )

class MemoryInformation(BaseModel):
    """
    A class for storing the memory information from device.\n
    :params MemorySize: The size of the memory in bytes
    :types MemorySize: int
    :params AvailableMemory: The available memory in bytes
    :types AvailableMemory: int
    :params InusedPageFile: The inused page file in bytes
    :types InusedPageFile: int
    :params AvailablePageFile: The available page file in bytes
    """
    MemorySize:int = Field(
        ...,
        title="Memory Size in bytes",
        description="The size of the memory in bytes"
    )
    AvailableMemory:int = Field(
        ...,
        title="Available Memory in bytes",
        description="The available memory in bytes"
    )
    InusedPageFile:int = Field(
        ...,
        title="Inused Page File in bytes",
        description="The inused page file in bytes"
    )
    AvailablePageFile:int = Field(
        ...,
        title="Available Page File in bytes",
        description="The available page file in bytes"
    )

class GraphicsInformation(BaseModel):
    """
    A class for storing the DirectX graphics information from device.\n
    :parmas Version: The version of the DirectX
    :types Version: int
    :params SetupParamaters: The setup parameters of the DirectX
    :types SetupParamaters: Optional[str]
    :params UserDPI: The DPI of the user
    :types UserDPI: int
    :params UserDPIScale: The DPI scale of the user
    :types UserDPIScale: int
    :params SystemDPI: The DPI of the system
    :types SystemDPI: int
    :params DWMDPIScaling: The DPI scaling of the DWM
    :types DWMDPIScaling: Any
    """
    Version:int = Field(
        ...,
        title="DirectX Version",
        description="The version of the DirectX"
    )
    SetupParamaters:Optional[str] = Field(
        None,
        title="Setup Parameters",
        description="The setup parameters of the DirectX"
    )
    UserDPI:int = Field(
        ...,
        title="User DPI",
        description="The DPI of the user"
    )
    UserDPIScale:int = Field(
        ...,
        title="User DPI Scale",
        description="The DPI scale of the user"
    )
    SystemDPI:int = Field(
        ...,
        title="System DPI",
        description="The DPI of the system"
    )
    DWMDPIScaling:Any = Field(
        ...,
        title="DWM DPI Scaling",
        description="The DPI scaling of the DWM"
    )

class DXDiagInformation(BaseModel):
    """
    A class for storing Dxdiag information from device\n
    :params Version: The version of the Dxdiag.exe
    :types Version: str
    :params UnicodeEnabled: Whether if the Unicode is enabled on dxdiag
    :types UnicodeEnabled: bool
    :params Is64Bit: Whether if the dxdiag is 64 bit
    :types Is64Bit: bool
    :params MiracastAvailable: Whether if the Miracast is available
    :types MiracastAvailable: bool
    :params MSHybrid: Whether if the MS Hybrid is available
    :types MSHybrid: bool
    :params DatabaseVersion: The version of the database
    :types DatabaseVersion: str
    """
    Version:str = Field(
        ...,
        title="Dxdiag Version",
        description="The version of the Dxdiag.exe"
    )
    UnicodeEnabled:bool = Field(
        ...,
        title="Unicode Enabled",
        description="Whether if the Unicode is enabled on dxdiag"
    )
    Is64Bit:bool = Field(
        ...,
        title="64 Bit",
        description="Whether if the dxdiag is 64 bit"
    )
    MiracastAvailable:bool = Field(
        ...,
        title="Miracast Available",
        description="Whether if the Miracast is available"
    )
    MSHybrid:bool = Field(
        ...,
        title="MS Hybrid",
        description="Whether if the MS Hybrid is available"
    )
    DatabaseVersion:str = Field(
        ...,
        title="Database Version",
        description="The version of the database"
    )