from pydxdiag.schema.device.SoundDevice import *
from typing import *
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime

def GetSoundDevices(
    dxXML:BeautifulSoup
) -> List[SoundDevice]:
    """
    Function to get the sound devices from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[SoundDevice]: The sound devices information
    :rtype List[SoundDevice]: List[SoundDevice]
    """
    SoundDevices:List[Tag] = dxXML.find("DxDiag").find("SoundDevices").find_all("SoundDevice")
    SoundDevicesList:List[SoundDevice] = []
    for device in SoundDevices:
        Description:str = device.find("Description").text
        HardwareID:str = device.find("HardwareID").text
        ManufacturerID:Optional[str] = None if device.find("ManufacturerID").text == "N/A" else device.find("Manufacturer").text
        ProductID:Optional[str] = None if device.find("ProductID").text == "N/A" else device.find("ProductID").text
        Type:Optional[str] = None if device.find("Type").text == "N/A" else device.find("Type").text
        DriverName:str = device.find("DriverName").text
        DriverVersion:str = device.find("DriverVersion").text
        DriverLanguage:str = device.find("DriverLanguage").text
        IsBetaDriver:bool = bool(int(device.find("DriverBeta").text))
        IsDebugDriver:bool = bool(int(device.find("DriverDebug").text))
        WHQLLogo:bool = True 
        if device.find("DriverWHQLLogo") == None:
            WHQLLogo = True
        elif device.find("DriverWHQLLogo").text == "No":
            WHQLLogo = False
        else:
            WHQLLogo = True
        DriverDate:datetime = datetime.strptime(device.find("DriverDate").text, "%Y/%m/%d %H:%M:%S")
        DriverSize:int = int(device.find("DriverSize").text)
        OtherFiles:Optional[Any] = device.find("OtherFiles").text
        DriverProvider:str = device.find("DriverProvider").text
        HwAccelLevel:str = device.find("HwAccelLevel").text
        DefaultSoundPlayback:bool = bool(int(device.find("DefaultSoundPlayback").text))
        DefaultVoicePlayback:bool = bool(int(device.find("DefaultVoicePlayback").text))
        VoiceManager:int = int(device.find("VoiceManager").text)
        EAX20Listner:bool = bool(int(device.find("EAX20Listener").text))
        EAX20Source:bool = bool(int(device.find("EAX20Source").text))
        I3DL2Listner:bool = bool(int(device.find("I3DL2Listener").text))
        I3DL2Souce:bool = bool(int(device.find("I3DL2Source").text))
        ZoomFX:bool = bool(int(device.find("ZoomFX").text))
        Flags:int = int(device.find("Flags").text)
        MinSecondarySampleRate:int = int(device.find("MinSecondarySampleRate").text)
        MaxSecondarySampleRate:int = int(device.find("MaxSecondarySampleRate").text)
        PrimaryBuffers:int = int(device.find("PrimaryBuffers").text)
        MaxHwMixingAllBuffers:int = int(device.find("MaxHwMixingAllBuffers").text)
        MaxHwMixingStaticBuffers:int = int(device.find("MaxHwMixingStaticBuffers").text)
        MaxHwMixingStreamingBuffers:int = int(device.find("MaxHwMixingStreamingBuffers").text)
        FreeHwMixingAllBuffers:int = int(device.find("FreeHwMixingAllBuffers").text)
        FreeHwMixingStaticBuffers:int = int(device.find("FreeHwMixingStaticBuffers").text)
        FreeHwMixingStreamingBuffers:int = int(device.find("FreeHwMixingStreamingBuffers").text)
        FreeHw3DAllBuffers:int = int(device.find("FreeHw3DAllBuffers").text)
        FreeHw3DStaticBuffers:int = int(device.find("FreeHw3DStaticBuffers").text)
        FreeHw3DStreamingBuffers:int = int(device.find("FreeHw3DStreamingBuffers").text)
        MaxHw3DAllBufffers:int = int(device.find("MaxHw3DAllBuffers").text)
        MaxHw3DStaticBuffers:int = int(device.find("MaxHw3DStaticBuffers").text)
        MaxHw3DStreamingBuffers:int = int(device.find("MaxHw3DStreamingBuffers").text)
        TotalHwMemBytes:int = int(device.find("TotalHwMemBytes").text)
        FreeHwMemBytes:int = int(device.find("FreeHwMemBytes").text)
        MaxContigFreeHwMemBytes:int = int(device.find("MaxContigFreeHwMemBytes").text)
        UnlockTransferRateHwBuffers:int = int(device.find("UnlockTransferRateHwBuffers").text)
        PlayCPUOverheadSwBuffers:int = int(device.find("PlayCPUOverheadSwBuffers").text)
        SoundDevicesList.append(
            SoundDevice(
                Description=Description,
                HardwareID=HardwareID,
                ManufacturerID=ManufacturerID,
                ProductID=ProductID,
                Type=Type,
                DriverName=DriverName,
                DriverVersion=DriverVersion,
                DriverLanguage=DriverLanguage,
                IsBetaDriver=IsBetaDriver,
                IsDebugDriver=IsDebugDriver,
                WHQLLogo=WHQLLogo,
                DriverDate=DriverDate,
                DriverSize=DriverSize,
                OtherFiles=OtherFiles,
                DriverProvider=DriverProvider,
                HwAccelLevel=HwAccelLevel,
                DefaultSoundPlayback=DefaultSoundPlayback,
                DefaultVoicePlayback=DefaultVoicePlayback,
                VoiceManager=VoiceManager,
                EAX20Listener=EAX20Listner,
                EAX20Source=EAX20Source,
                I3DL2Listener=I3DL2Listner,
                I3DL2Source=I3DL2Souce,
                ZoomFX=ZoomFX,
                Flags=Flags,
                MinSecondarySampleRate=MinSecondarySampleRate,
                MaxSecondarySampleRate=MaxSecondarySampleRate,
                PrimaryBuffers=PrimaryBuffers,
                MaxHwMixingBuffers=MaxHwMixingBufferInfo(
                    AllBuffers=MaxHwMixingAllBuffers,
                    StaticBuffers=MaxHwMixingStaticBuffers,
                    StreamingBuffers=MaxHwMixingStreamingBuffers
                ),
                MaxHw3DBuffers=MaxHw3DBufferInfo(
                    AllBuffers=MaxHw3DAllBufffers,
                    StaticBuffers=MaxHw3DStaticBuffers,
                    StreamingBuffers=MaxHw3DStreamingBuffers
                ),
                FreeHwMixingBuffers=FreeHwMixingBufferInfo(
                    AllBuffers=FreeHwMixingAllBuffers,
                    StaticBuffers=FreeHwMixingStaticBuffers,
                    StreamingBuffers=FreeHwMixingStreamingBuffers
                ),
                FreeHw3DBuffers=FreeHw3DBufferInfo(
                    AllBuffers=FreeHw3DAllBuffers,
                    StaticBuffers=FreeHw3DStaticBuffers,
                    StreamingBuffers=FreeHw3DStreamingBuffers
                ),
                TotalHwMemBytes=TotalHwMemBytes,
                FreeHwMemBytes=FreeHwMemBytes,
                MaxContigFreeHwMemBytes=MaxContigFreeHwMemBytes,
                UnlockTransferRateHwBuffers=UnlockTransferRateHwBuffers,
                PlayCPUOverheadSwBuffers=PlayCPUOverheadSwBuffers
            )
        )
    return SoundDevicesList