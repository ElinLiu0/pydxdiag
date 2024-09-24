from pydxdiag.schema.SystemInformation import *
from pydxdiag.schema.DxDiagNotes import *
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import *
from pydxdiag.schema.device.DisplayDevice import (
    DisplayDevice,
    ColorPrimaries,
    Luminance,
    HardwareSchedulingAttributes,
    DXVADeinterplaceCap,
    MPO
)
from datetime import datetime

def GetDisplayDevices(
    dxXML: BeautifulSoup
) -> List[DisplayDevice]:
    """
    Function to get the display devices from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: ElementTree
    :return List[DisplayDevice]: The display devices information
    :rtype List[DisplayDevice]: List[DisplayDevice]
    """
    DisplayDevices:List[Tag] = dxXML.find("DxDiag").find("DisplayDevices").find_all("DisplayDevice")
    DisplayDevicesList:List[DisplayDevice] = []
    for device in DisplayDevices:
        CardName:str = device.find("CardName").text
        Manufacturer:str = device.find("Manufacturer").text
        ChipType:str = device.find("ChipType").text
        DACType:str = device.find("DACType").text
        DeviceType:str = device.find("DeviceType").text
        DeviceKey:str = device.find("DeviceKey").text
        DeviceStatus:str = device.find("DeviceStatus").text
        DeviceProblemCode:Optional[str] = None if device.find("DeviceProblemCode").text == "No Problem" else device.find("DeviceProblemCode").text
        DriverProblemCode:Optional[str] = None if device.find("DriverProblemCode").text == "Unknown" else device.find("DriverProblemCode").text
        # dxdiag reports memory in MB, converting to bytes
        DisplayMemory:str = int(device.find("DisplayMemory").text.split(" ")[0]) * 1024 * 1024
        DedicatedMemory:int = int(device.find("DedicatedMemory").text.split(" ")[0]) * 1024 * 1024
        SharedMemory:int = int(device.find("SharedMemory").text.split(" ")[0]) * 1024 * 1024
        ResolutionWidth:int = int(device.find("CurrentMode").text.split("x")[0]) if "x" in device.find("CurrentMode").text else 0
        ResolutionHeight:int = int(device.find("CurrentMode").text.split("x")[1].split(" ")[1]) if "x" in device.find("CurrentMode").text else 0
        ColorBits:int = int(device.find("CurrentMode").text.split(" ")[3].replace("(","").replace(")",""))  if "x" in device.find("CurrentMode").text else 0
        RefreshRate:int = int(device.find("CurrentMode").text.split(" ")[5].replace("Hz","").replace("(","").replace(")","")) if "x" in device.find("CurrentMode").text else 0
        HDRSupported:bool = True if device.find("HDRSupport").text == "Supported" else False
        Topology:str = device.find("Topology").text
        ColorSpace:str = device.find("ColorSpace").text
        ColorPrimariesInfo:ColorPrimaries = ColorPrimaries()
        Colors:List[str] = device.find("ColorPrimaries").text.replace("Red","").replace("White Point","").replace("Green","").replace("Blue","")
        Colors:List[Tuple[float,float]] = [eval(color) for color in Colors.split(", ") if color != "Unknown"]
        ColorPrimariesInfo.Red = Colors[0] if len(Colors) > 0 else (0.0,0.0)
        ColorPrimariesInfo.Green = Colors[1] if len(Colors) > 1 else (0.0,0.0)
        ColorPrimariesInfo.Blue = Colors[2] if len(Colors) > 2 else (0.0,0.0)
        ColorPrimariesInfo.WhitePoint = Colors[3] if len(Colors) > 3 else (0.0,0.0)
        LuminanceInfo:Luminance = Luminance()
        Luminances:List[str] = device.find("Luminance").text.split(", ")
        for LuminanceSlice in Luminances:
            LuminanceValue:float = round(
                float(LuminanceSlice.split("=")[-1]),
                ndigits = 2
            ) if LuminanceSlice != "Unknown" else 0.0
            setattr(
                LuminanceInfo,
                LuminanceSlice.split("=")[0].strip().split(" ")[0],
                LuminanceValue
            ) if LuminanceSlice != "Unknown" else None
        MonitorName:Optional[str] = device.find("MonitorName").text if device.find("MonitorName") != None else None
        MonitorModel:Optional[str] = None
        if device.find("MonitorModel") == None:
            MonitorModel = None
        elif device.find("MonitorModel").text == "Unknown":
            MonitorModel = None
        else:
            device.find("MonitorModel").text
        MonitorId:str = device.find("MonitorId").text if device.find("MonitorId") != None else None
        # NativeWidth:int = int(device.find("NativeMode").text.split("x")[0]) if "x" in device.find("NativeMode").text else 0
        NativeWidth:int = 0
        if device.find("NativeMode") != None:
            if "x" in device.find("NativeMode").text:
                NativeWidth = int(device.find("NativeMode").text.split("x")[0])
            else:
                NativeWidth = 0
        # NativeHeight:int = int(device.find("NativeMode").text.split("x")[1].split(" ")[1].replace("(p)","")) if "x" in device.find("NativeMode").text else 0
        NativeHeight:int = 0
        if device.find("NativeMode") != None:
            if "x" in device.find("NativeMode").text:
                NativeHeight = int(device.find("NativeMode").text.split("x")[1].split(" ")[1].replace("(p)",""))
            else:
                NativeHeight = 0
        # NativeRefreshRate:int = int(float(device.find("NativeMode").text.split(" ")[3].replace("Hz","").replace("(","").replace(")",""))) if "x" in device.find("NativeMode").text else 0
        NativeRefreshRate:int = 0
        if device.find("NativeMode") != None:
            if "x" in device.find("NativeMode").text:
                NativeRefreshRate = int(float(device.find("NativeMode").text.split(" ")[3].replace("Hz","").replace("(","").replace(")","")))
            else:
                NativeRefreshRate = 0
        OutputType:Optional[str] = device.find("OutputType").text if device.find("OutputType") != None else None
        Eotf2084Supported:bool = bool(int(device.find("Eotf2084Supported").text) if device.find("Eotf2084Supported") != None else 0)
        BT2020YCCSupported:bool = bool(int(device.find("BT2020YCC").text) if device.find("BT2020YCC") != None else 0)
        BT2020RGBSupported:bool = bool(int(device.find("BT2020RGB").text) if device.find("BT2020RGB") != None else 0)
        AdavancedColorEnabled:bool = bool(int(device.find("AdvancedColorEnabled").text) if device.find("AdvancedColorEnabled") != None else 0)
        AdavancedColorSupported:bool = bool(int(device.find("AdvancedColorSupported").text) if device.find("AdvancedColorSupported") != None else 0)
        bCheckedMonitorCapabilities:bool = bool(int(device.find("bCheckedMonitorCapabilities").text) if device.find("bCheckedMonitorCapabilities") != None else 0)
        PixelFormat:Optional[str] = device.find("PixelFormat").text if device.find("PixelFormat") != None else None
        # MonitorMaxRes:Optional[str] = None if device.find("MonitorMaxRes").text == "Unknown" else device.find("MonitorMaxRes").text
        MonitorMaxRes:Optional[str] = None
        if device.find("MonitorMaxRes") != None:
            if device.find("MonitorMaxRes").text == "Unknown":
                MonitorMaxRes = None
            else:
                MonitorMaxRes = device.find("MonitorMaxRes").text
        DriverName:str = device.find("DriverName").text
        DriverFileVersion:str = device.find("DriverFileVersion").text
        DriverVersion:str = device.find("DriverVersion").text
        DriverLanguage:str = device.find("DriverLanguage").text
        DDIVersion:int = int(device.find("DDIVersion").text)
        FeatureLevels:List[str] = device.find("FeatureLevels").text.split(",")
        DriverModel:str = device.find("DriverModel").text.split(" ")[0]
        WDDMVersion:Optional[str] = device.find("DriverModel").text.split(" ")[1]
        IsBetaDriver:bool = bool(int( device.find("DriverBeta").text))
        ISDebugDriver:bool = bool(int( device.find("DriverDebug").text))
        DriverDate:datetime = datetime.strptime(device.find("DriverDate").text,"%Y/%m/%d %H:%M:%S")
        DriverSize:int = int(device.find("DriverSize").text)
        WHQLLogo:bool = True if device.find("DriverWHQLLogo").text == "Yes" else False
        WHQLDateStamp:Optional[datetime] = None if device.find("WHQLDateStamp").text == "Unknown" else datetime.strptime(device.find("WHQLDateStamp").text,"%Y/%m/%d %H:%M:%S")
        VDD:Optional[Any] = None if device.find("VDD").text == "Unknown" or device.find("VDD").text == "未知" else device.find("VDD").text
        MiniVDD:Optional[Any] = None if device.find("MiniVDD").text == "Unknown" or device.find("MiniVDD").text == "未知" else device.find("MiniVDD").text
        MiniVDDSize:int = int(device.find("MiniVDDSize").text)
        DeviceIdentifier:str = device.find("DeviceIdentifier").text.replace("{","").replace("}","")
        VendorID:str = device.find("VendorID").text
        DeviceID:str = device.find("DeviceID").text
        SubSysID:str = device.find("SubSysID").text
        DriverNodeStrongName:str = device.find("DriverNodeStrongName").text
        RankOfInstalledDriver:str = str(device.find("RankOfInstalledDriver").text)
        DXVAModes:Optional[Any] = None if device.find("DXVAModes").text == None else device.find("DXVAModes").text
        DXVA2Modes:List[str] = [
            # * I'm not sure this filter is correct or not
            # * Because other data seems like UUID or something
            Mode for Mode in device.find("DXVA2Modes").text.split(" ") if "DXVA2" in Mode
        ]
        GraphicsPreemption:str = device.find("GraphicsPreemption").text
        ComputePreemption:str = device.find("ComputePreemption").text
        Miracast:Optional[str] = None if "Not Supported" in device.find("Miracast").text else device.find("Miracast").text
        DetachableGPU:bool = True if device.find("DetachableGPU").text == "Yes" else False
        HybridGraphicsGPUType:Optional[str] = None if "Not Supported" in device.find("HybridGraphicsGPUType").text else device.find("HybridGraphicsGPUType").text
        PowerManagementPStates:Optional[str] = None if "Not Supported" in device.find("PowerManagementPStates").text else device.find("PowerManagementPSState").text
        VirtualGPUSupport:bool = False if "Not Supported" in device.find("VirtualGPUSupport").text else True
        BlockList:str = device.find("BlockList").text
        DriverCatalogAttributes:Dict[str,bool] = {}
        CatalogAttributesReadFromDX:str = device.find("DriverCatalogAttributes").text
        for attribute in CatalogAttributesReadFromDX.split(" ")[:-1]:
            attribute:List[str] = attribute.split(":")
            DriverCatalogAttributes[attribute[0]] = eval(attribute[1])
        MPOMaxPlanes:int = int(device.find("MPOMaxPlanes").text)
        MPOCaps:List[str] = device.find("MPOCaps").text.split(",")
        MPOStrechString:str = device.find("MPOStretch").text
        if MPOStrechString == "Not Supported":
            MPOStretch:Optional[Tuple[float,float]] = None
        else:
            StrechString:List[str] = [s.strip() for s in MPOStrechString.split("-")]
            StrechFloat:List[float] = []
            for i in range(len(StrechString)):
                StrechFloat.append(
                    float(StrechString[i].replace("X",""))
                )
            MPOStretch:Optional[Tuple[float,float]] = tuple(StrechFloat)
        MPOMediaHints:str = device.find("MPOMediaHints").text
        MPOFormats:List[str] = device.find("MPOFormats").text.split(",")
        PanelFitterCaps:Optional[Any] = device.find("PanelFitterCaps").text
        HardwareSchedulingAttributesInfo:HardwareSchedulingAttributes = HardwareSchedulingAttributes()
        HardwareSchedulingAttributesString:str = device.find("HardwareSchedulingAttributes").text
        Attributes:List[str] = HardwareSchedulingAttributesString.split(" ")
        for attribute in Attributes:
            attribute:List[str] = attribute.split(":")
            if attribute == [""]:
                continue
            setattr(
                HardwareSchedulingAttributesInfo,
                attribute[0],
                eval(attribute[1]) if attribute[1] == "True" or attribute[1] == "False" else attribute[1]
            )
        DisplayableSupport:bool = True if device.find("DisplayableSupport").text == "Supported" else False
        DXVADeinterlaceCaps:List[DXVADeinterplaceCap] = []
        DXVADeinterlaceCapTags:List[Tag] = device.find("DXVADeinterlaceCaps").find_all("DXVADeinterlaceCap")
        for Cap in DXVADeinterlaceCapTags:
            DXVADeinterlaceCaps.append(
                DXVADeinterplaceCap(
                    GUID=Cap.find("GUID").text,
                    D3DInputFormat=Cap.find("D3DInputFormat").text,
                    D3DOutputFormat=Cap.find("D3DOutputFormat").text,
                    Caps = Cap.find("Caps").text.split(" "),
                    NumPreviousOutputFrames = int(Cap.find("NumPreviousOutputFrames").text),
                    NumBackwardRefSamples = int(Cap.find("NumBackwardRefSamples").text),
                    NumForwardRefSamples = int(Cap.find("NumForwardRefSamples").text)
                )
            )
        D3D9Overlay:bool = True if device.find("D3D9Overlay").text == "Supported" else False
        DXVAHD:bool = True if device.find("DXVAHD").text == "Enabled" else False
        DDrawStatus:bool = True if device.find("DDrawStatus").text == "Enabled" else False
        D3DStatus:bool = True if device.find("D3DStatus").text == "Enabled" else False
        AGPStatus:bool = True if device.find("AGPStatus").text == "Enabled" else False
        DisplayDevicesList.append(
            DisplayDevice(
                CardName=CardName,
                Manufacturer=Manufacturer,
                ChipType=ChipType,
                DACType=DACType,
                DeviceType=DeviceType,
                DeviceKey=DeviceKey,
                DeviceStatus=DeviceStatus,
                DeviceProblemCode=DeviceProblemCode,
                DriverProblemCode=DriverProblemCode,
                DisplayMemory=DisplayMemory,
                DedicatedMemory=DedicatedMemory,
                SharedMemory=SharedMemory,
                ResolutionWidth=ResolutionWidth,
                ResolutionHeight=ResolutionHeight,
                ColorBits=ColorBits,
                RefreshRate=RefreshRate,
                HDRSupported=HDRSupported,
                Topology=Topology,
                ColorSpace=ColorSpace,
                ColorPrimaries=ColorPrimariesInfo,
                Luminance=LuminanceInfo,
                MonitorName=MonitorName,
                MonitorModel=MonitorModel,
                MonitorId=MonitorId,
                NativeWidth=NativeWidth,
                NativeHeight=NativeHeight,
                NativeRefreshRate=NativeRefreshRate,
                OutputType=OutputType,
                Eotf2084Supported=Eotf2084Supported,
                BT20YCC=BT2020YCCSupported,
                BT2020RGB=BT2020RGBSupported,
                AdavancedColorEnabled=AdavancedColorEnabled,
                AdavancedColorSupported=AdavancedColorSupported,
                bCheckedMonitorCapabilities=bCheckedMonitorCapabilities,
                PixelFormat=PixelFormat,
                MonitorMaxRes=MonitorMaxRes,
                DriverName=DriverName,
                DriverFileVersion=DriverFileVersion,
                DriverVersion=DriverVersion,
                DriverLanguage=DriverLanguage,
                DDIVersion=DDIVersion,
                FeatureLevels=FeatureLevels,
                DriverModel=DriverModel,
                WDDMVersion=WDDMVersion,
                IsBetaDriver=IsBetaDriver,
                IsDebugDriver=ISDebugDriver,
                DriverDate=DriverDate,
                DriverSize=DriverSize,
                WHQLLogo=WHQLLogo,
                WHQLDate=WHQLDateStamp,
                VDD=VDD,
                MiniVDD=MiniVDD,
                MiniVDDSize=MiniVDDSize,
                DeviceIdentifier=DeviceIdentifier,
                VendorID=VendorID,
                DeviceID=DeviceID,
                SubSysID=SubSysID,
                DriverNodeStrongName=DriverNodeStrongName,
                RankOfInstalledDriver=RankOfInstalledDriver,
                DXVAModes=DXVAModes,
                DXVA2Modes=DXVA2Modes,
                GraphicsPreemption=GraphicsPreemption,
                ComputePreemption=ComputePreemption,
                Miracast=Miracast,
                DetachableGPU=DetachableGPU,
                HybridGraphics=HybridGraphicsGPUType,
                PowerManagementPStates=PowerManagementPStates,
                VirtualGPUSupport=VirtualGPUSupport,
                BlockList=BlockList,
                DriverCatalogAttributes=DriverCatalogAttributes,
                MPOInfo = MPO(
                    MaxPlanes=MPOMaxPlanes,
                    Caps=MPOCaps,
                    Stretch=MPOStretch,
                    Hints=MPOMediaHints,
                    Formats=MPOFormats
                ),
                PanelFilterCaps = PanelFitterCaps,
                HardwareSchedulingAttributesInfo=HardwareSchedulingAttributesInfo,
                DisplayableSupport=DisplayableSupport,
                DXVADeinterlaceCaps=DXVADeinterlaceCaps,
                D3D9Overlay=D3D9Overlay,
                DXVAHD=DXVAHD,
                DDrawStatus=DDrawStatus,
                D3DStatus=D3DStatus,
                AGPStatus=AGPStatus,
            )
        )
    return DisplayDevicesList