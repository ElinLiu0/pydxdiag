from pydxdiag.schema.device.SoundCaptureDevice import *
from datetime import datetime
from typing import List
from bs4.element import Tag
from bs4 import BeautifulSoup

def GetSoundCaptureDevices(
    dxXML:BeautifulSoup
) -> List[SoundCaptureDevice]:
    """
    Function to get the sound capture devices from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[SoundCaptureDevice]: The sound capture devices information
    :rtype List[SoundCaptureDevice]: List[SoundCaptureDevice]
    """
    SoundCaptureDevices:List[Tag] = dxXML.find("DxDiag").find("SoundCaptureDevices").find_all("SoundCaptureDevice")
    SoundCaptureDevicesList:List[SoundCaptureDevice] = []
    for device in SoundCaptureDevices:
        Description:str = device.find("Description").text
        DriverName:str = device.find("DriverName").text
        DriverVersion:str = device.find("DriverVersion").text
        DriverLanguage:str = device.find("DriverLanguage").text
        IsBetaDriver:bool = bool(int(device.find("DriverBeta").text))
        IsDebugDriver:bool = bool(int(device.find("DriverDebug").text))
        DriverDate:datetime = datetime.strptime(device.find("DriverDate").text, "%Y/%m/%d %H:%M:%S")
        DriverSize:int = int(device.find("DriverSize").text)
        DefaultSoundRecording:bool = bool(int(device.find("DefaultSoundRecording").text))
        DefaultVoiceRecording:bool = bool(int(device.find("DefaultVoiceRecording").text))
        Flags:int = int(device.find("Flags").text)
        Foramts:int = int(device.find("Formats").text)
        SoundCaptureDevicesList.append(
            SoundCaptureDevice(
                Description = Description,
                DriverName = DriverName,
                DriverVersion = DriverVersion,
                DriverLanguage = DriverLanguage,
                IsBetaDriver = IsBetaDriver,
                IsDebugDriver = IsDebugDriver,
                DriverDate = DriverDate,
                DriverSize = DriverSize,
                DefaultSoundRecording = DefaultSoundRecording,
                DefaultVoiceRecording = DefaultVoiceRecording,
                Flags = Flags,
                Formats = Foramts
            )
        )
    return SoundCaptureDevicesList