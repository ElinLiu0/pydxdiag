# Author: Elin
# Date: 2024-09-10 09:10:12
# Last Modified by:   Elin
# Last Modified time: 2024-09-10 09:10:12

from pydxdiag.schema.device.InputRelatedDevice import *
from typing import *
from datetime import datetime
from bs4.element import Tag
from bs4 import BeautifulSoup

def GetInputRelatedDevicesViaUSBRoot(
    dxXML: BeautifulSoup
) -> List[InputRelatedDevice]:
    """
    Function to get the input related devices via use root from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[InputRelatedDevice]: The input related devices information
    :rtype List[InputRelatedDevice]: List[InputRelatedDevice]
    """
    InputRelatedDevices:List[Tag] = dxXML.find("DxDiag").find_all("DirectInput")[1].find("USBRoot").find_all("InputRelatedDevice")
    InputRelatedDevicesList:List[InputRelatedDevice] = []
    for device in InputRelatedDevices:
        Description:str = device.find("Description").text
        VendorID:int = int(device.find("VendorID").text)
        ProductID:int = int(device.find("ProductID").text)
        Location:Optional[str] = device.find("Location").text   
        MatchingDeviceID:str = device.find("MatchingDeviceID").text
        UpperFilters:Optional[Any] = device.find("UpperFilters").text
        LowerFilters:Optional[Any] = device.find("LowerFilters").text
        Service:str = device.find("Service").text
        OEMData:Optional[str] = device.find("OEMData").text
        Flags1:Optional[int] = None if device.find("Flags1").text == '' else int(device.find("Flags1").text)
        Flags2:Optional[int] = None if device.find("Flags2").text == '' else int(device.find("Flags2").text)
        Drivers:List[Driver] = []
        for driver in device.find_all("Driver"):
            Name:str = driver.find("Name").text
            InstallationPath:str = driver.find("Path").text
            Version:str = driver.find("Version").text
            IsBetaDriver:bool = bool(int(driver.find("Beta").text))
            IsDebugDriver:bool = bool(int(driver.find("Debug").text))
            Date:datetime = datetime.strptime(driver.find("Date").text, "%m/%d/%Y %H:%M:%S")
            Size:int = int(driver.find("Size").text)
            Drivers.append(
                Driver(
                    Name=Name,
                    InstallationPath=InstallationPath,
                    Version=Version,
                    Language="",
                    IsBetaDriver=IsBetaDriver,
                    IsDebugDriver=IsDebugDriver,
                    Date=Date,
                    Size=Size
                )
            )
        InputRelatedDevicesList.append(
            InputRelatedDevice(
                Description=Description,
                VendorID=VendorID,
                ProductID=ProductID,
                Location=Location,
                MatchingDeviceID=MatchingDeviceID,
                UpperFilters=UpperFilters,
                LowerFilters=LowerFilters,
                Service=Service,
                OEMData=OEMData,
                Flags1=Flags1,
                Flags2=Flags2,
                Drivers=Drivers,
                Type="USBRoot"
            )
        )
    return InputRelatedDevicesList

def GetInputRelatedDeviceViaPS2(
    dxXML: BeautifulSoup
) -> List[InputRelatedDevice]:
    """
    Function to get the input related devices via PS2 device tree from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[InputRelatedDevice]: The input related devices information
    :rtype List[InputRelatedDevice]: List[InputRelatedDevice]
    """
    InputRelatedDevices:List[Tag] = dxXML.find("DxDiag").find_all("DirectInput")[1].find("PS2Devices").find_all("InputRelatedDevice")
    InputRelatedDevicesList:List[InputRelatedDevice] = []
    for device in InputRelatedDevices:
        Description:str = device.find("Description").text
        VendorID:int = int(device.find("VendorID").text)
        ProductID:int = int(device.find("ProductID").text)
        Location:Optional[str] = device.find("Location").text   
        MatchingDeviceID:str = device.find("MatchingDeviceID").text
        UpperFilters:Optional[Any] = device.find("UpperFilters").text
        LowerFilters:Optional[Any] = device.find("LowerFilters").text
        Service:str = device.find("Service").text
        OEMData:Optional[str] = device.find("OEMData").text
        Flags1:Optional[int] = None if device.find("Flags1").text == '' else int(device.find("Flags1").text)
        Flags2:Optional[int] = None if device.find("Flags2").text == '' else int(device.find("Flags2").text)
        Drivers:List[Driver] = []
        for driver in device.find_all("Driver"):
            Name:str = driver.find("Name").text
            InstallationPath:str = driver.find("Path").text
            Version:str = driver.find("Version").text
            IsBetaDriver:bool = bool(int(driver.find("Beta").text))
            IsDebugDriver:bool = bool(int(driver.find("Debug").text))
            Date:datetime = datetime.strptime(driver.find("Date").text, "%m/%d/%Y %H:%M:%S")
            Size:int = int(driver.find("Size").text)
            Drivers.append(
                Driver(
                    Name=Name,
                    InstallationPath=InstallationPath,
                    Version=Version,
                    Language="",
                    IsBetaDriver=IsBetaDriver,
                    IsDebugDriver=IsDebugDriver,
                    Date=Date,
                    Size=Size
                )
            )
        InputRelatedDevicesList.append(
            InputRelatedDevice(
                Description=Description,
                VendorID=VendorID,
                ProductID=ProductID,
                Location=Location,
                MatchingDeviceID=MatchingDeviceID,
                UpperFilters=UpperFilters,
                LowerFilters=LowerFilters,
                Service=Service,
                OEMData=OEMData,
                Flags1=Flags1,
                Flags2=Flags2,
                Drivers=Drivers,
                Type="PS2"
            )
        )
    return InputRelatedDevicesList

def GetStatusForPollWithInterput(
    dxXML: BeautifulSoup
) -> bool:
    """
    Function to get the status for poll with interrupt from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return bool: The status for poll with interrupt
    :rtype bool: bool
    """
    Status:bool = True if dxXML.find("DxDiag").find_all("DirectInput")[1].find("PollWithInterrupt").text == "Yes" else False
    return Status