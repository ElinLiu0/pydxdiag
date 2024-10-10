from pydxdiag.schema.SystemInformation import *
from pydxdiag.schema.DxDiagNotes import *
from bs4 import BeautifulSoup
from bs4.element import Tag
from pydxdiag.schema.DirectXDebugLevels import *


def GetMachineInformation(
    dxXML:BeautifulSoup
) -> MachineInformation:
    """
    Function to get the machine information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return MachineInformation: The machine information
    :rtype MachineInformation: MachineInformation
    """
    MachineName:str = dxXML.find("DxDiag").find("SystemInformation").find("MachineName").text
    MachineId:str = dxXML.find("DxDiag").find("SystemInformation").find("MachineId").text
    return MachineInformation(
        MachineName=MachineName,
        MachineId=MachineId
    )

def GetOSInformation(
        dxXML:BeautifulSoup
) -> OSInformation:
    """
    Function to get the OS information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return OSInformation: The OS information
    :rtype OSInformation: OSInformation
    """
    OSInfo:str = dxXML.find("DxDiag").find("OperatingSystem").text
    Version:int = int(OSInfo.split(" ")[1])
    Bit:int = int(OSInfo.split(" ")[3].replace("-bit",""))
    BuildId:int = int(OSInfo.split(" ")[6].replace("(","").replace(")",""))
    ReleaseId:str = OSInfo.split(" ")[-1].replace("(","").replace(")","")
    Language:str = dxXML.find("DxDiag").find("Language").text
    return OSInformation(
        Name=OSInfo,
        Version=Version,
        Bit=Bit,
        BuildId=BuildId,
        ReleaseId=ReleaseId,
        Language=Language
    )

def GetDxDiagNotes(
    dxXML:BeautifulSoup
) -> List[GeneralDXDiagNotes]:
    """
    Function to get the dxdiag notes from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[GeneralDXDiagNotes]: The dxdiag notes
    :rtype List[GeneralDXDiagNotes]: List[GeneralDXDiagNotes]
    """
    # Get Dxdiag notes
    Notes:List[BeautifulSoup] = dxXML.find("DxDiag").find("DxDiagNotes").find_all()
    # Retriving sub elements
    NotesList:List[GeneralDXDiagNotes] = []
    for note in Notes:
        # Get sub element name name
        NoteType:str = note.name
        if NoteType == "DisplayTab":
            NotesList.append(DisplayTabNotes(
                Notes=note.text
            ))
        elif NoteType == "SoundTab":
            NotesList.append(SoundTabNotes(
                Notes=note.text
            ))
        elif NoteType == "InputTab":
            NotesList.append(InputTabNotes(
                Notes=note.text
            ))
    return NotesList

def GetDirectXDebugLevels(
    dxXML:BeautifulSoup
) -> DirectXDebugLevels:
    """
    Function to get the DirectX debug levels from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return DirectXDebugLevels: The DirectX debug levels
    :rtype DirectXDebugLevels: DirectXDebugLevels
    """
    Levels:DirectXDebugLevels = DirectXDebugLevels()
    # Find all sub elements under DirectXDebugLevels
    DebugLevelElements:List[Tag] = dxXML.find("DxDiag").find("DirectXDebugLevels").find_all()
    for element in DebugLevelElements:
        if element.name == "Direct3D":
            Levels.D3DDebugInformation = D3DDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
        elif element.name == "DirectDraw":
            Levels.DirectDrawDebugInformation = DirectDrawDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
        elif element.name == "DirectInput":
            Levels.DirectInputDebugInformation = DirectInputDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
        elif element.name == "DirectMusic":
            Levels.DMDebugInformation = DirectMusicDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
        elif element.name == "DirectPlay":
            Levels.DirectPlayDebugInformation = DirectPlayDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
        elif element.name == "DirectSound":  
            Levels.DirectSoundDebugInformation = DirectSoundDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
        elif element.name == "DirectShow":
            Levels.DirectShowDebugInformation = DirectShowDebugInformation(
                Current = element.find("Current").text,
                Max = element.find("Max").text,
                Runtime = None if element.find("Runtime").text == "n/a" else element.find("Runtime").text
            )
    return Levels

def GetSystemModelInformation(
    dxXML:BeautifulSoup
) -> SystemModelInformation:
    """
    Function to get the system model information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return SystemModelInformation: The system model information
    :rtype SystemModelInformation: SystemModelInformation
    """
    Manufacturer:str = dxXML.find("DxDiag").find("SystemInformation").find("SystemManufacturer").text
    Model:str = dxXML.find("DxDiag").find("SystemInformation").find("SystemModel").text
    return SystemModelInformation(
        SystemManufacturer=Manufacturer,
        SystemModel=Model
    )

def GetFirmwareInformation(
    dxXML:BeautifulSoup
) -> FirmwareInformation:
    """
    Function to get the firmware information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return FirmwareInformation: The firmware information
    :rtype FirmwareInformation: FirmwareInformation
    """
    BIOSVersion:str = dxXML.find("DxDiag").find("SystemInformation").find("BIOS").text
    FirmwareType:str = dxXML.find("DxDiag").find("SystemInformation").find("FirmwareType").text
    return FirmwareInformation(
        FirmwareType=FirmwareType,
        BIOSVersion=BIOSVersion
    )

def GetCPUInformation(
    dxXML:BeautifulSoup
) -> CPUInformation:
    """
    Function to get the CPU information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return CPUInformation: The CPU information
    :rtype CPUInformation: CPUInformation
    """
    CPUInfo:str = dxXML.find("DxDiag").find("SystemInformation").find("Processor").text
    Name:str = CPUInfo.split(",")[0]
    Gen:int = 0
    # * Since i got no Legacy CPU like AMD Athlon or Intel Pentium
    # * or HEDT CPU like Intel Xeon or AMD Threadripper
    # * So this function will only support AMD Ryzen and Intel Core Series Processors
    if "Intel" in Name:
        if "Ultra" in Name:
            Gen:int = int(Name.split(" ")[4][0]) * 100
        elif "Core" in Name:
            Gen:int = int(Name.split(" ")[0].replace("th",""))    
        else:
            Gen:Optional[int] = None
    elif "AMD" in Name:
        if "Ryzen" in Name:
            Gen:int = int(Name.split(" ")[3][0] * 1000)
        else:
            Gen:Optional[int] = None
    BaseClock:float = float(CPUInfo.split("~")[1].split("GHz")[0])
    Threads:int = int(CPUInfo.split("CPUs")[0].split("(")[-1])
    Brand:str = ""
    if "Intel" in Name:
        Brand = "Intel"
    elif "AMD" in Name:
        Brand = "AMD"
    else:
        Brand = "Unknown"
    return CPUInformation(
        Gen=Gen,
        BaseClock=BaseClock,
        Threads=Threads,
        Brand=Brand,
        Name=Name
    )

def GetMemoryInformation(
    dxXML:BeautifulSoup
) -> MemoryInformation:
    """
    Function to get the memory information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return MemoryInformation: The memory information
    :rtype MemoryInformation: MemoryInformation
    """
    MemoryInfo:str = dxXML.find("DxDiag").find("SystemInformation").find("Memory").text
    TotalMemory:int = int(MemoryInfo.split(" ")[0].replace("MB",""))
    AvailableMemory:str = dxXML.find("DxDiag").find("SystemInformation").find("AvaliableOSMem").text
    AvailableMemory:int = int(AvailableMemory.split(" ")[0].replace("MB",""))
    InusedPageFile:str = dxXML.find("DxDiag").find("SystemInformation").find("PageFile").text
    InusedPageFile:int = int(InusedPageFile.split(",")[0].split(" ")[0].replace("MB",""))
    AvailablePageFile:str = dxXML.find("DxDiag").find("SystemInformation").find("PageFile").text
    AvailablePageFile:int = int(AvailablePageFile.split(",")[1].strip().split(" ")[0].replace("MB",""))

    return MemoryInformation(
        MemorySize=TotalMemory,
        AvailableMemory=AvailableMemory,
        InusedPageFile=InusedPageFile,
        AvailablePageFile=AvailablePageFile
    )

def GetGraphicsInfromation(
    dxXML:BeautifulSoup
) -> List[GraphicsInformation]:
    """
    Function to get the graphics information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return GraphicsInformation: The graphics information
    :rtype GraphicsInformation: GraphicsInformation
    """
    DireectXVersion:int = int(dxXML.find("DxDiag").find("SystemInformation").find("DirectXVersion").text.split(" ")[1])
    SetupParamaters:str = dxXML.find("DxDiag").find("SystemInformation").find("DXSetupParameters").text
    UserDPI:int = int(dxXML.find("DxDiag").find("SystemInformation").find("UserDPISettings").text.split(" ")[0])
    UserDPIScale:int = int(dxXML.find("DxDiag").find("SystemInformation").find("UserDPISettings").text.split(" ")[2].replace("(",""))
    SystemDPI:int = int(dxXML.find("DxDiag").find("SystemInformation").find("SystemDPISettings").text.split(" ")[0])
    SystemDPIScale:int = int(dxXML.find("DxDiag").find("SystemInformation").find("SystemDPISettings").text.split(" ")[2].replace("(",""))
    DWMDPIScaling:Any = dxXML.find("DxDiag").find("SystemInformation").find("DWMDPIScaling").text
    return GraphicsInformation(
        Version=DireectXVersion,
        SetupParamaters=SetupParamaters,
        UserDPI=UserDPI,
        UserDPIScale=UserDPIScale,
        SystemDPI=SystemDPI,
        SystemDPIScale=SystemDPIScale,
        DWMDPIScaling=DWMDPIScaling
    )

def GetDXDiagInformation(
    dxXML:BeautifulSoup
) -> DXDiagInformation:
    """
    Function to get the dxdiag information from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return DXDiagInformation: The dxdiag information
    :rtype DXDiagInformation: DXDiagInformation
    """
    DxDiagVersion:str = dxXML.find("DxDiag").find("DxDiagVersion").text
    DxDiagUnicode:bool = bool(int(dxXML.find("DxDiag").find("DxDiagUnicode").text))
    DxDiag64Bit:bool = bool(int(dxXML.find("DxDiag").find("DxDiag64Bit").text))
    Miracast:bool = True if "Available" in dxXML.find("DxDiag").find("Miracast").text else False
    MSHybrid:bool = True if "Supported" in dxXML.find("DxDiag").find("MSHybrid").text else False
    DatabaseVersion:str = dxXML.find("DxDiag").find("DirectXDatabaseVersion").text
    return DXDiagInformation(
        Version=DxDiagVersion,
        UnicodeEnabled=DxDiagUnicode,
        Is64Bit=DxDiag64Bit,
        MiracastAvailable=Miracast,
        MSHybrid=MSHybrid,
        DatabaseVersion=DatabaseVersion
    )