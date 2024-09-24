from pydxdiag.schema.device.VideoCaptureDevice import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag
import re

def GetVideoCaptureDevices(
    dxXML:BeautifulSoup
) -> List[VideoCaptureDevice]:
    """
    Function to get the video capture devices from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[VideoCaptureDevice]: The video capture devices information
    :rtype List[VideoCaptureDevice]: List[VideoCaptureDevice]
    """
    VideoCaptureDevices:List[Tag] = dxXML.find("DxDiag").find("VideoCaptureDevices").find_all("VideoCaptureDevice")
    VideoCaptureDevicesList:List[VideoCaptureDevice] = []
    for device in VideoCaptureDevices:
        FriendlyName:str = device.find("FriendlyName").text
        Category:str = device.find("Category").text
        SysmbolicLink:str = device.find("SymbolicLink").text
        Location:str = device.find("Location").text
        Rotation:int = int(device.find("Rotation").text)
        SensorOrientation:int = int(device.find("SensorOrientation").text)
        Manufacturer:str = device.find("Manufacturer").text
        HardwareID:str = device.find("HardwareID").text
        DriverDesc:str = device.find("DriverDesc").text
        DriverVersion:str = device.find("DriverVersion").text
        Driverte:datetime = datetime.strptime(device.find("DriverDateLocalized").text, "%Y/%m/%d %H:%M:%S")
        Service:str = device.find("Service").text
        Class:str = device.find("Class").text
        DevNodeStatus:str = device.find("DevNodeStatus").text
        ContainerID:str = device.find("ContainerID").text
        ProblemCode:str = device.find("ProblemCode").text
        BusReportedDeviceDesc:str = device.find("BusReportedDeviceDesc").text
        UpperFilters:Optional[str] = None if device.find("UpperFilters").text == "n/a" else device.find("UpperFilters").text
        LowerFilters:Optional[str] = None if device.find("LowerFilters").text == "n/a" else device.find("LowerFilters").text
        StackString:str = device.find("Stack").text
        Stack:List[str] = []
        for stack in StackString.split(","):
            Stack.append(
                re.split(r"\\", stack)[-1]
            )
        ContainerCategory:Optional[str] = None if device.find("ContainerCategory").text == "n/a" else device.find("ContainerCategory").text
        SensorGroupID:str = device.find("SensorGroupID").text.replace("{", "").replace("}", "")
        MFT0:Optional[str] = None if device.find("MFT0").text == "n/a" else device.find("MFT0").text
        DMFT:Optional[str] = None if device.find("DMFT").text == "n/a" else device.find("DMFT").text
        CustomCaptureSource:Optional[str] = None if device.find("CustomCaptureSource").text == "n/a" else device.find("CustomCaptureSource").text
        DependentStillCapture:Optional[str] = None if device.find("DependentStillCapture").text == "n/a" else device.find("DependentStillCapture").text
        EnablePlatformDMFT:bool = bool(device.find("EnablePlatformDMFT").text)
        DMFTChain:Optional[str] = None if device.find("DMFTChain").text == "n/a" else device.find("DMFTChain").text
        EnableDshowRedirection:bool = bool(device.find("EnableDshowRedirection").text)
        FrameServerEnabled:Optional[str] = None if device.find("FrameServerEnabled").text == "n/a" else device.find("FrameServerEnabled").text
        AnalogProviders:Optional[str] = None if device.find("AnalogProviders").text == "n/a" else device.find("AnalogProviders").text
        MSXUCapability:Optional[str] = None if device.find("MSXUCapability").text == "n/a" else device.find("MSXUCapability").text
        ProfileIDs:Optional[str] = None if device.find("ProfileIDs").text == "n/a" else device.find("ProfileIDs").text
        DriverProvider:Optional[str] = None if device.find("DriverProvider").text == "n/a" else device.find("DriverProvider").text
        VideoCaptureDevicesList.append(
            VideoCaptureDevice(
                FriendlyName = FriendlyName,
                Category = Category,
                SymbolicLink = SysmbolicLink,
                Location = Location,
                Rotation = Rotation,
                SensorOrientation = SensorOrientation,
                Manufacturer = Manufacturer,
                HardwareID = HardwareID,
                DriverDesc = DriverDesc,
                DriverVersion = DriverVersion,
                DriverDate = Driverte,
                DriverProvider = DriverProvider,
                Service = Service,
                Class = Class,
                DevNodeStatus = DevNodeStatus,
                ContainerID = ContainerID,
                ProblemCode = ProblemCode,
                BusReportedDeviceDesc = BusReportedDeviceDesc,
                UpperFilters = UpperFilters,
                LowerFilters = LowerFilters,
                Stack = Stack,
                ContainerCategory = ContainerCategory,
                SensorGroupID = SensorGroupID,
                MFT0 = MFT0,
                DMFT = DMFT,
                CustomCaptureSource = CustomCaptureSource,
                DependentStillCapture = DependentStillCapture,
                EnablePlatformDMFT = EnablePlatformDMFT,
                DMFTChain = DMFTChain,
                EnableDshowRedirection = EnableDshowRedirection,
                FrameServerEnabled = FrameServerEnabled,
                AnalogProviders = AnalogProviders,
                MSXUCapability = MSXUCapability,
                ProfileIDs = ProfileIDs
            )
        )
    return VideoCaptureDevicesList