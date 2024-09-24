from pydxdiag.schema.device.SystemDevice import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetSystemDevices(
    dxXML:BeautifulSoup
) -> List[SystemDevice]:
    """
    Function to get the system devices from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[SystemDevice]: The system devices information
    :rtype List[SystemDevice]: List[SystemDevice]
    """
    SystemDevices:List[Tag] = dxXML.find("DxDiag").find("SystemDevices").find_all("SystemDevice")
    SystemDevicesList:List[SystemDevice] = []
    for device in SystemDevices:
        Name:str = device.find("Name").text
        DeviceKey:str = device.find("DeviceKey").text
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
        SystemDevicesList.append(
            SystemDevice(
                Name=Name,
                DeviceKey=DeviceKey,
                Drivers=Drivers
            )
        )
    return SystemDevicesList