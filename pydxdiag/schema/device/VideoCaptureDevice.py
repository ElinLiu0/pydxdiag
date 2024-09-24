from pydantic import (
    BaseModel,
    Field,
)
from typing import *
from datetime import datetime

class VideoCaptureDevice(BaseModel):
    """
    Class to represent the video capture device.\n
    :params FriendlyName: Friendly name displayed for users.
    :type FriendlyName: str
    :params Category: Category of the video capture device.
    :type Category: str
    :params SymbolicLink: Symbolic link of the video capture device.
    :type SymbolicLink: str
    :params Location: Location of the video capture device.
    :type Location: str
    :params Rotation: Rotation of the video capture device.
    :type Rotation: int
    :"params SensorOrientation: Sensor orientation of the video capture device.
    :type SensorOrientation: int
    :params Manufacturer: Manufacturer of the video capture device.
    :type Manufacturer: str
    :params HardwareID: Hardware ID of the video capture device.
    :type HardwareID: str
    :params DriverDesc: Driver description of the video capture device.
    :type DriverDesc: str
    :params DriverProvider: Driver provider of the video capture device.
    :type DriverProvider: str
    :parmas DriverVersion: Driver version of the video capture device.
    :type DriverVersion: str
    :params DriverDate: Date of the driver.
    :type DriverDate: datetime
    :params Service: Service type of the video capture device.
    :type Service: str
    :params Class: Class of the video capture device.
    :type Class: str
    :params DevNodeStatus: Device node status of the video capture device.
    :type DevNodeStatus: str
    :params ContainerID: Container ID of the video capture device.
    :type ContainerID: str
    :params ProblemCode: Problem code of the video capture device.
    :type ProblemCode: Optional[str]
    :params BusReportedDeviceDesc: Bus reported device description of the video capture device.
    :type BusReportedDeviceDesc: Optional[str]
    :params UpperFilters: Upper filters of the video capture device.
    :type UpperFilters: Optional[str]
    :params LowerFilters: Lower filters of the video capture device.
    :type LowerFilters: Optional[str]
    :params Stack: Stack of the video capture device.
    :type Stack: List[str]
    :params ContainerCategory: Container category of the video capture device.
    :type ContainerCategory: Optional[str]
    :params SensorGroupID: Sensor group ID of the video capture device.
    :type SensorGroupID: str
    :params MFT0: MFT0 of the video capture device.
    :type MFT0: Optional[str]
    :params DMFT: DMFT of the video capture device.
    :type DMFT: Optional[str]
    :params CustomCaptureSource: Custom capture source of the video capture device.
    :type CustomCaptureSource: Optional[str]    
    :params DependentStillCapture: Dependent still capture of the video capture device.
    :type DependentStillCapture: Optional[str]
    :params EnableDshowRedirection: Enable Dshow redirection of the video capture device.
    :type EnableDshowRedirection: bool
    :params DMFTChain: DMFT chain of the video capture device.
    :type DMFTChain: Optional[str]
    :params EnablePlatformDMFT: Enable platform DMFT of the video capture device.
    :type EnablePlatformDMFT: bool
    :params FrameServerEnabled: Frame server enabled of the video capture device.
    :type FrameServerEnabled: Optional[str]
    :params AnalogProviders: Analog providers of the video capture device.
    :type AnalogProviders: Optional[str]
    :params MSXUCapability: MSXU capability of the video capture device.
    :type MSXUCapability: Optional[str]
    :params ProfileIDs: Profile IDs of the video capture device.
    :type ProfileIDs: Optional[str]
    """
    FriendlyName: str = Field(..., description="Friendly Name")
    Category: str = Field(..., description="Category")
    SymbolicLink: str = Field(..., description="Symbolic Link")
    Location: str = Field(..., description="Location")
    Rotation: int = Field(..., description="Rotation")
    SensorOrientation: int = Field(..., description="Sensor Orientation")
    Manufacturer: str = Field(..., description="Manufacturer")
    HardwareID: str = Field(..., description="Hardware ID")
    DriverDesc: str = Field(..., description="Driver Desc")
    DriverProvider: str = Field(..., description="Driver Provider")
    DriverVersion: str = Field(..., description="Driver Version")
    DriverDate: datetime = Field(..., description="Driver Date")
    Service: str = Field(..., description="Service")
    Class: str = Field(..., description="Class")
    DevNodeStatus: str = Field(..., description="DevNode Status")
    ContainerID: str = Field(..., description="Cotainer ID")
    ProblemCode: Optional[str] = Field(None, description="Problem Code")
    BusReportedDeviceDesc: Optional[str] = Field(None, description="Bus Reported Device Desc")
    UpperFilters: Optional[str] = Field(None, description="Upper Filters")
    LowerFilters: Optional[str] = Field(None, description="Lower Filters")
    Stack: List[str] = Field(..., description="Stack")
    ContainerCategory: Optional[str] = Field(..., description="Container Category")
    SensorGroupID: str = Field(..., description="Sensor Group ID")
    MFT0: Optional[str] = Field(None, description="MFT0")
    DMFT: Optional[str] = Field(None, description="DMFT")
    CustomCaptureSource: Optional[str] = Field(None, description="Custom Capture Source")
    DependentStillCapture: Optional[str]
    EnableDshowRedirection: bool
    DMFTChain: Optional[str]
    EnablePlatformDMFT: bool
    FrameServerEnabled: Optional[str]
    AnalogProviders: Optional[str]
    MSXUCapability: Optional[str]
    ProfileIDs: Optional[str]