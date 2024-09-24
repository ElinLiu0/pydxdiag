from pydxdiag.schema.device.DirectInputDevice import *
from typing import *
from datetime import datetime
from bs4.element import Tag
from bs4 import BeautifulSoup

def GetDirectInputDevices(
    dxXML:BeautifulSoup,
) -> List[DirectInputDevice]:
    """
    Function to get the direct input devices from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[DirectInputDevice]: The direct input devices information
    :rtype List[DirectInputDevice]: List[DirectInputDevice]
    """
    DirectInputDevices:List[Tag] = dxXML.find("DxDiag").find_all("DirectInput")[1].find("DirectInputDevices").find_all("DirectInputDevice")
    DirectInputDevicesList:List[DirectInputDevice] = []
    for device in DirectInputDevices:
        DeviceName:str = device.find("DeviceName").text
        Attached:bool = bool(int(device.find("Attached").text))
        JoyStickID:int = int(device.find("JoyStickID").text) if device.find("JoyStickID") != None else None
        VendorID:int = int(device.find("VendorID").text)
        ProductID:int = int(device.find("ProductID").text)
        FFDriverName:Optional[str] = device.find("FFDriverName").text
        FFDriverDate:Optional[datetime] = None 
        if device.find("FFDriverDateEnglish").text == None:
            FFDriverDate = None
        elif device.find("FFDriverDateEnglish").text == '':
            FFDriverDate = None
        else:   
            datetime.strptime(device.find("FFDriverDateEnglish").text, "%m/%d/%Y %H:%M:%S")
        FFDriverVersion:Optional[str] = device.find("FFDriverVersion").text
        FFDriverSize:int = int(device.find("FFDriverSize").text)
        DirectInputDevicesList.append(
            DirectInputDevice(
                DeviceName=DeviceName,
                Attached=Attached,
                JoyStickID=JoyStickID,
                VendorID=VendorID,
                ProductID=ProductID,
                FFDriverName=FFDriverName,
                FFDriverDate=FFDriverDate,
                FFDriverVersion=FFDriverVersion,
                FFDriverSize=FFDriverSize
            )
        )
    return DirectInputDevicesList