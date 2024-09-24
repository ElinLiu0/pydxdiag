from pydxdiag.schema.LogicalDisk import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag


def GetLogicalDisks(
    dxXML:BeautifulSoup
) -> List[LogicalDisk]:
    """
    Function to get the logical disks from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[LogicalDisk]: The logical disks information
    :rtype List[LogicalDisk]: List[LogicalDisk]
    """
    LogicalDisks:List[Tag] = dxXML.find("DxDiag").find("LogicalDisks").find_all("LogicalDisk")
    LogicalDisksList:List[LogicalDisk] = []
    for disk in LogicalDisks:
        DriveLetter:str = disk.find("DriveLetter").text
        FreeSpace:int = int(disk.find("FreeSpace").text)
        MaxSpace:int = int(disk.find("MaxSpace").text)
        FileSystem:str = disk.find("FileSystem").text
        Model:str = disk.find("Model").text
        PNPDeviceID:str = disk.find("PNPDeviceID").text
        HardDriveIndex:int = int(disk.find("HardDriveIndex").text)
        LogicalDisksList.append(
            LogicalDisk(
                DriveLetter=DriveLetter,
                FreeSpace=FreeSpace,
                MaxSpace=MaxSpace,
                FileSystem=FileSystem,
                Model=Model,
                PNPDeviceID=PNPDeviceID,
                HardDriveIndex=HardDriveIndex
            )
        )
    return LogicalDisksList