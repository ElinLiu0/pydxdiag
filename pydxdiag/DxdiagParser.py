from bs4 import BeautifulSoup
from typing import *
from pathlib import Path
import subprocess
from pydantic import BaseModel, Field

import pydxdiag.schema.DirectXDebugLevels
import pydxdiag.schema.DxDiagNotes
import pydxdiag.schema.EnvPowerInformation
import pydxdiag.schema.Filter
import pydxdiag.schema.LogicalDisk
import pydxdiag.schema.SystemInformation
import pydxdiag.schema.WER
import pydxdiag.schema.device
import pydxdiag.schema.device.DirectInputDevice
import pydxdiag.schema.device.DisplayDevice
import pydxdiag.schema.device.InputRelatedDevice
import pydxdiag.schema.device.SoundCaptureDevice
import pydxdiag.schema.device.SoundDevice
import pydxdiag.schema.device.SystemDevice
import pydxdiag.schema.device.VideoCaptureDevice
import pydxdiag.schema.sz
import pydxdiag.schema.sz.szBytesStreamHandler
import pydxdiag.schema.sz.szEnableHarewareMFT
import pydxdiag.schema.sz.szMFFileVersion
import pydxdiag.schema.sz.szMFT
import pydxdiag.schema.sz.szPreferredMFT
import pydxdiag.schema.sz.szSchemeHandlers

# sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

import pydxdiag.functions.device.DirectInputDevice as DirectInputDevice
import pydxdiag.functions.device.DisplayDevice as DisplayDevice
import pydxdiag.functions.device.InputRelatedDevice as InputRelatedDevice
import pydxdiag.functions.device.SoundCaptureDevice as SoundCaptureDevice
import pydxdiag.functions.device.SoundDevice as SoundDevice
import pydxdiag.functions.device.SystemDevice as SystemDevice
import pydxdiag.functions.device.VideoCaptureDevice as VideoCaptureDevice
import pydxdiag.functions.sz.szByteStreamHandler as szByteStreamHandler
import pydxdiag.functions.sz.szEnabledHardwareMFT as szEnabledHardwareMFT
import pydxdiag.functions.sz.szMFFileVersions as szMFFileVersions
import pydxdiag.functions.sz.szMFTs as szMFTs
import pydxdiag.functions.sz.szPreferredMFT as szPreferredMFT
import pydxdiag.functions.sz.szSchemeHandlers as szSchemeHandlers
import pydxdiag.functions.EnvPowerInformation as EnvPowerInformation
import pydxdiag.functions.Filter as Filter
import pydxdiag.functions.LogicalDisk as LogicalDisk
import pydxdiag.functions.SystemInformation as SystemInformation
import pydxdiag.functions.WER as WERFuncs
import json

class DxdiagDataTotal:
    """
    A class for storing the total dxdiag data\n
    :params DirectInputDevices: The DirectInput devices
    :types DirectInputDevices: List[DirectInputDevice.DirectInputDevice]
    :params DisplayDevices: The Display devices
    :types DisplayDevices: List[DisplayDevice.DisplayDevice]
    :params InputRelatedDevicesViaUSBRoot: The Input Related devices via USB Root
    :types InputRelatedDevicesViaUSBRoot: List[InputRelatedDevice.InputRelatedDevice]
    :params InputRelatedDeviceViaPS2: The Input Related devices via PS2
    :types InputRelatedDeviceViaPS2: List[InputRelatedDevice.InputRelatedDevice]
    :params StatusForPollWithInterput: The status for Poll with Interrupt
    :types StatusForPollWithInterput: bool
    :params SoundCaptureDevices: The Sound Capture devices
    :types SoundCaptureDevices: List[SoundCaptureDevice.SoundCaptureDevice]
    :params SoundDevices: The Sound devices
    :types SoundDevices: List[SoundDevice.SoundDevice]
    :params SystemDevices: The System devices
    :types SystemDevices: List[SystemDevice.SystemDevice]
    :params VideoCaptureDevices: The Video Capture devices
    :types VideoCaptureDevices: List[VideoCaptureDevice.VideoCaptureDevice]
    :params BytesStreamHandlers: The Byte Stream Handlers
    :types BytesStreamHandlers: List[szBytesStreamHandler.szBytesStreamHandler.szBytesStreamHandler]
    :params StatufForEnableHardwareMFT: The status for Enable Hardware MFT
    :types StatufForEnableHardwareMFT: bool
    :params MFFileVersions: The MF File Versions
    :types MFFileVersions: List[szMFFileVersion.szMFFileVersion.szMFFileVersion]
    :params MFTs: The MFTs
    :types MFTs: List[szMFT.szMFT.szMFT]
    :params szPreferedMFTs: The Preferred MFTs
    :types szPreferedMFTs: List[szPreferredMFT.szPreferredMFT.szPreferredMFT]
    :params SchemeHandlers: The Scheme Handlers
    :types SchemeHandlers: List[szSchemeHandlers.szSchemeHandlers.szSchemeHandlers]
    :params EnvPowerInformation: The Environment Power Information
    :types EnvPowerInformation: EvrPowerInformation
    :params Filters: The Filters
    :types Filters: List[Filter.Filter]
    :params PreferredDShowFilters: The Preferred DShow Filters
    :types PreferredDShowFilters: List[str]
    :params LogicalDisks: The Logical Disks
    :types LogicalDisks: List[LogicalDisk.LogicalDisk]
    :params OSInformation: The OS Information
    :types OSInformation: OSInformation
    :params DirectXDebugLevels: The DirectX Debug Levels
    :types DirectXDebugLevels: DirectXDebugLevels
    :params DxDiagNotes: The DxDiag Notes
    :types DxDiagNotes: List[GeneralDXDiagNotes]
    :params MachineInformation: The Machine Information
    :types MachineInformation: MachineInformation
    :params SystemModelInformation: The System Model Information
    :types SystemModelInformation: SystemModelInformation
    :params FirmwareInformation: The Firmware Information
    :types FirmwareInformation: FirmwareInformation
    :params CPUInformation: The CPU Information
    :types CPUInformation: CPUInformation
    :params MemoryInformation: The Memory Information
    :types MemoryInformation: MemoryInformation
    :params GraphicsInfromation: The Graphics Information
    :types GraphicsInfromation: GraphicsInformation
    :params DXDiagInformation: The DXDiag Information
    :types DXDiagInformation: DXDiagInformation
    :params WERInfo: The WER Information
    :types WERInfo: List[WERInformation]
    """
    def __init__(
        self,
        DirectInputDevices: List[DirectInputDevice.DirectInputDevice],
        DisplayDevices: List[DisplayDevice.DisplayDevice],
        InputRelatedDevicesViaUSBRoot: List[InputRelatedDevice.InputRelatedDevice],
        InputRelatedDeviceViaPS2: List[InputRelatedDevice.InputRelatedDevice],
        StatusForPollWithInterput: bool,
        SoundCaptureDevices: List[SoundCaptureDevice.SoundCaptureDevice],
        SoundDevices: List[SoundDevice.SoundDevice],
        SystemDevices: List[SystemDevice.SystemDevice],
        VideoCaptureDevices: List[VideoCaptureDevice.VideoCaptureDevice],
        BytesStreamHandlers: List[pydxdiag.schema.sz.szBytesStreamHandler.szBytesStreamHandler],
        StatufForEnableHardwareMFT: bool,
        MFFileVersions: List[pydxdiag.schema.sz.szMFFileVersion.szMFFileVersion],
        MFTs: List[pydxdiag.schema.sz.szMFT.szMFT],
        szPreferedMFTs: List[szPreferredMFT.szPreferredMFT],
        SchemeHandlers: List[szSchemeHandlers.szSchemeHandlers],
        EnvPowerInformation: EnvPowerInformation.EvrPowerInformation,
        Filters: List[Filter.Filter],
        PreferredDShowFilters: List[str],
        LogicalDisks: List[LogicalDisk.LogicalDisk],
        OSInformation: SystemInformation.OSInformation,
        DirectXDebugLevels: pydxdiag.schema.DirectXDebugLevels.DirectXDebugLevels,
        DxDiagNotes: List[pydxdiag.schema.DxDiagNotes.GeneralDXDiagNotes],
        MachineInformation: SystemInformation.MachineInformation,
        SystemModelInformation: SystemInformation.SystemModelInformation,
        FirmwareInformation: SystemInformation.FirmwareInformation,
        CPUInformation: SystemInformation.CPUInformation,
        MemoryInformation: SystemInformation.MemoryInformation,
        GraphicsInfromation: SystemInformation.GraphicsInformation,
        DXDiagInformation: SystemInformation.DXDiagInformation,
        WERInfo: List[pydxdiag.schema.WER.WERInformation]
    ) -> None:
        self.DirectInputDevices = DirectInputDevices
        self.DisplayDevices = DisplayDevices
        self.InputRelatedDevicesViaUSBRoot = InputRelatedDevicesViaUSBRoot
        self.InputRelatedDeviceViaPS2 = InputRelatedDeviceViaPS2
        self.StatusForPollWithInterput = StatusForPollWithInterput
        self.SoundCaptureDevices = SoundCaptureDevices
        self.SoundDevices = SoundDevices
        self.SystemDevices = SystemDevices
        self.VideoCaptureDevices = VideoCaptureDevices
        self.BytesStreamHandlers = BytesStreamHandlers
        self.StatufForEnableHardwareMFT = StatufForEnableHardwareMFT
        self.MFFileVersions = MFFileVersions
        self.MFTs = MFTs
        self.szPreferedMFTs = szPreferedMFTs
        self.SchemeHandlers = SchemeHandlers
        self.EnvPowerInformation = EnvPowerInformation
        self.Filters = Filters
        self.PreferredDShowFilters = PreferredDShowFilters
        self.LogicalDisks = LogicalDisks
        self.OSInformation = OSInformation
        self.DirectXDebugLevels = DirectXDebugLevels
        self.DxDiagNotes = DxDiagNotes
        self.MachineInformation = MachineInformation
        self.SystemModelInformation = SystemModelInformation
        self.FirmwareInformation = FirmwareInformation
        self.CPUInformation = CPUInformation
        self.MemoryInformation = MemoryInformation
        self.GraphicsInfromation = GraphicsInfromation
        self.DXDiagInformation = DXDiagInformation
        self.WERInfo = WERInfo
    def model_dump(self) -> Dict[str, Any]:
        """
        Convert all the data into a dictionary\n
        :return: The data as a dictionary
        :rtype: Dict[str, Any]
        """
        return {
            "DirectInputDevices": [x.model_dump() for x in self.DirectInputDevices],
            "DisplayDevices": [x.model_dump() for x in self.DisplayDevices],
            "InputRelatedDevicesViaUSBRoot": [x.model_dump() for x in self.InputRelatedDevicesViaUSBRoot],
            "InputRelatedDeviceViaPS2": [x.model_dump() for x in self.InputRelatedDeviceViaPS2],
            "StatusForPollWithInterput": self.StatusForPollWithInterput,
            "SoundCaptureDevices": [x.model_dump() for x in self.SoundCaptureDevices],
            "SoundDevices": [x.model_dump() for x in self.SoundDevices],
            "SystemDevices": [x.model_dump() for x in self.SystemDevices],
            "VideoCaptureDevices": [x.model_dump() for x in self.VideoCaptureDevices],
            "BytesStreamHandlers": [x.model_dump() for x in self.BytesStreamHandlers],
            "StatufForEnableHardwareMFT": self.StatufForEnableHardwareMFT,
            "MFFileVersions": [x.model_dump() for x in self.MFFileVersions],
            "MFTs": [x.model_dump() for x in self.MFTs],
            "szPreferedMFTs": [x.model_dump() for x in self.szPreferedMFTs],
            "SchemeHandlers": [x.model_dump() for x in self.SchemeHandlers],
            "EnvPowerInformation": self.EnvPowerInformation.model_dump(),
            "Filters": [x.model_dump() for x in self.Filters],
            "PreferredDShowFilters": self.PreferredDShowFilters,
            "LogicalDisks": [x.model_dump() for x in self.LogicalDisks],
            "OSInformation": self.OSInformation.model_dump(),
            "DirectXDebugLevels": self.DirectXDebugLevels.model_dump(),
            "DxDiagNotes": [x.model_dump() for x in self.DxDiagNotes],
            "MachineInformation": self.MachineInformation.model_dump(),
            "SystemModelInformation": self.SystemModelInformation.model_dump(),
            "FirmwareInformation": self.FirmwareInformation.model_dump(),
            "CPUInformation": self.CPUInformation.model_dump(),
            "MemoryInformation": self.MemoryInformation.model_dump(),
            "GraphicsInfromation": self.GraphicsInfromation.model_dump(),
            "DXDiagInformation": self.DXDiagInformation.model_dump(),
            "WERInfo": [x.model_dump() for x in self.WERInfo]
        }
    def model_dump_json(self,save_path:str = None) -> Optional[str]:
        """
        Convert all the data into a JSON string\n
        :param save_path: The path to save the JSON file
        :type save_path: str
        :return: The data as a JSON string
        :rtype: Optional[str]
        """
        data:Dict[str,Any] = self.model_dump()
        # Retriving all data and convert datetime object to string
        data = json.dumps(data,default=str,indent=4,ensure_ascii=False)
        if save_path:
            with open(save_path,"w",encoding="utf-8") as f:
                f.write(data)
            f.close()
        else:
            return data


class DxdiagParser(DxdiagDataTotal):
    """
    Basic parser class for DirectX Diagnostic Tool output
    """
    def __init__(self) -> None:
        self.dxXML:BeautifulSoup = None
        # Creating a BeautifulSoup object for the dxdiag output
        self.LoadDXDiag()
    def LoadDXDiag(self) -> None:
        """
        Function to load the dxdiag output into the BeautifulSoup object
        """
        # Running subprocess without shell execution
        subprocess.run(
            ["dxdiag", "-x","dxdiag.xml"],
            shell=False
        )
        # Reading output file then transfer into StringIO Object
        # FIXME: Since dxdiag.exe doesn't support stdout, we have to read the file
        # Probably there is some way that can capture the I/O Buffer while writing?
        with open("dxdiag.xml", "r",encoding="utf-8") as f:
            # Creating an ElementTree object from the StringIO object
              self.dxXML:BeautifulSoup = BeautifulSoup(f, features="xml")
        f.close()
        # Removing the output file
        Path("dxdiag.xml").unlink()
        super(DxdiagParser, self).__init__(
            DirectInputDevices=self.GetDirectInputDevices(),
            DisplayDevices=self.GetDisplayDevices(),
            InputRelatedDevicesViaUSBRoot=self.GetInputRelatedDevicesViaUSBRoot(),
            InputRelatedDeviceViaPS2=self.GetInputRelatedDeviceViaPS2(),
            StatusForPollWithInterput=self.GetStatusForPollWithInterput(),
            SoundCaptureDevices=self.GetSoundCaptureDevices(),
            SoundDevices=self.GetSoundDevices(),
            SystemDevices=self.GetSystemDevices(),
            VideoCaptureDevices=self.GetVideoCaptureDevices(),
            BytesStreamHandlers=self.GetBytesStreamHandlers(),
            StatufForEnableHardwareMFT=self.GetStatufForEnableHardwareMFT(),
            MFFileVersions=self.GetMFFileVersions(),
            MFTs=self.GetMFTs(),
            szPreferedMFTs=self.GetszPreferedMFTs(),
            SchemeHandlers=self.GetSchemeHandlers(),
            EnvPowerInformation=self.GetEnvPowerInformation(),
            Filters=self.GetFilters(),
            PreferredDShowFilters=self.GetPreferredDShowFilters(),
            LogicalDisks=self.GetLogicalDisks(),
            OSInformation=self.GetOSInformation(),
            DirectXDebugLevels=self.GetDirectXDebugLevels(),
            DxDiagNotes=self.GetDxDiagNotes(),
            MachineInformation=self.GetMachineInformation(),
            SystemModelInformation=self.GetSystemModelInformation(),
            FirmwareInformation=self.GetFirmwareInformation(),
            CPUInformation=self.GetCPUInformation(),
            MemoryInformation=self.GetMemoryInformation(),
            GraphicsInfromation=self.GetGraphicsInfromation(),
            DXDiagInformation=self.GetDXDiagInformation(),
            WERInfo=self.GetWERInfo()
        )
    
    def __call__(self) -> DxdiagDataTotal:
        return self._data

    def GetDirectInputDevices(self) -> List[DirectInputDevice.DirectInputDevice]:
        """
        Function to get the DirectInput devices from the dxdiag output\n
        :return: List of DirectInputDevice objects
        :rtype: List[DirectInputDevice.DirectInputDevice]
        """
        return DirectInputDevice.GetDirectInputDevices(self.dxXML)
    def GetDisplayDevices(self) -> List[DisplayDevice.DisplayDevice]:
        """
        Function to get the Display devices from the dxdiag output\n
        :return: List of DisplayDevice objects
        :rtype: List[DisplayDevice.DisplayDevice]
        """
        return DisplayDevice.GetDisplayDevices(self.dxXML)
    def GetInputRelatedDevicesViaUSBRoot(self) -> List[InputRelatedDevice.InputRelatedDevice]:
        """
        Function to get the Input Related devices via USB Root from the dxdiag output\n
        :return: List of InputRelatedDevice objects
        :rtype: List[InputRelatedDevice.InputRelatedDevice]
        """
        return InputRelatedDevice.GetInputRelatedDevicesViaUSBRoot(self.dxXML)
    def GetInputRelatedDeviceViaPS2(self) -> List[InputRelatedDevice.InputRelatedDevice]:
        """
        Function to get the Input Related devices via PS2 from the dxdiag output\n
        :return: List of InputRelatedDevice objects
        :rtype: List[InputRelatedDevice.InputRelatedDevice]
        """
        return InputRelatedDevice.GetInputRelatedDeviceViaPS2(self.dxXML)
    def GetStatusForPollWithInterput(self) -> bool:
        """
        Function to get the Status for Poll with Interrupt from the dxdiag output\n
        :return: The status for Poll with Interrupt
        :rtype: bool
        """
        return InputRelatedDevice.GetStatusForPollWithInterput(self.dxXML)
    def GetSoundCaptureDevices(self) -> List[SoundCaptureDevice.SoundCaptureDevice]:
        """
        Function to get the Sound Capture devices from the dxdiag output\n
        :return: List of SoundCaptureDevice objects
        :rtype: List[SoundCaptureDevice.SoundCaptureDevice]
        """
        return SoundCaptureDevice.GetSoundCaptureDevices(self.dxXML)
    def GetSoundDevices(self) -> List[SoundDevice.SoundDevice]:
        """
        Function to get the Sound devices from the dxdiag output\n
        :return: List of SoundDevice objects
        :rtype: List[SoundDevice.SoundDevice]
        """
        return SoundDevice.GetSoundDevices(self.dxXML)
    def GetSystemDevices(self) -> List[SystemDevice.SystemDevice]:
        """
        Function to get the System devices from the dxdiag output\n
        :return: List of SystemDevice objects
        :rtype: List[SystemDevice.SystemDevice]
        """
        return SystemDevice.GetSystemDevices(self.dxXML)
    def GetVideoCaptureDevices(self) -> List[VideoCaptureDevice.VideoCaptureDevice]:
        """
        Function to get the Video Capture devices from the dxdiag output\n
        :return: List of VideoCaptureDevice objects
        :rtype: List[VideoCaptureDevice.VideoCaptureDevice]
        """
        return VideoCaptureDevice.GetVideoCaptureDevices(self.dxXML)
    def GetBytesStreamHandlers(self) -> List[pydxdiag.schema.sz.szBytesStreamHandler.szBytesStreamHandler]:
        """
        Function to get the Byte Stream Handlers from the dxdiag output\n
        :return: List of szBytesStreamHandler objects
        :rtype: List[pydxdiag.schema.sz.szBytesStreamHandler.szBytesStreamHandler]
        """
        return szByteStreamHandler.GetBytesStreamHandlers(self.dxXML)
    def GetStatufForEnableHardwareMFT(self) -> pydxdiag.schema.sz.szEnableHarewareMFT.szEnableHardwareMFT:
        """
        Function to get the Status for Enable Hardware MFT from the dxdiag output\n
        :return: The status for Enable Hardware MFT
        :rtype: bool
        """
        return szEnabledHardwareMFT.GetStatufForEnableHardwareMFT(self.dxXML)
    def GetMFFileVersions(self) -> List[pydxdiag.schema.sz.szMFFileVersion.szMFFileVersion]:
        """
        Function to get the MF File Versions from the dxdiag output\n
        :return: List of szMFFileVersions objects
        :rtype: List[pydxdiag.schema.sz.szMFFileVersion.szMFFileVersion]
        """
        return szMFFileVersions.GetMFFileVersions(self.dxXML)
    def GetMFTs(self) -> List[pydxdiag.schema.sz.szMFT.szMFT]:
        """
        Function to get the MFTs from the dxdiag output\n
        :return: List of szMFTs objects
        :rtype: List[pydxdiag.schema.sz.szMFT.szMFT]
        """
        return szMFTs.GetMFTs(self.dxXML)
    def GetszPreferedMFTs(self) -> List[pydxdiag.schema.sz.szPreferredMFT.szPreferredMFT]:
        """
        Function to get the Preferred MFTs from the dxdiag output\n
        :return: List of szPreferredMFT objects
        :rtype: List[pydxdiag.schema.sz.szPreferredMFT.szPreferredMFT]
        """
        return szPreferredMFT.GetszPreferedMFTs(self.dxXML)
    def GetSchemeHandlers(self) -> List[pydxdiag.schema.sz.szSchemeHandlers.szSchemeHandlers]:
        """
        Function to get the Scheme Handlers from the dxdiag output\n
        :return: List of szSchemeHandler objects
        :rtype: List[pydxdiag.schema.sz.szSchemeHandler.szSchemeHandlers]
        """
        return szSchemeHandlers.GetSchemeHandlers(self.dxXML)
    def GetEnvPowerInformation(self) -> pydxdiag.schema.EnvPowerInformation.EvrPowerInformation:
        """
        Function to get the Environment Power Information from the dxdiag output\n
        :return: The Environment Power Information
        :rtype: pydxdiag.schema.EnvPowerInformation.EvrPowerInformation
        """
        return EnvPowerInformation.GetEnvPowerInformation(self.dxXML)
    def GetFilters(self) -> List[pydxdiag.schema.Filter.Filter]:
        """
        Function to get the Filters from the dxdiag output\n
        :return: List of Filter objects
        :rtype: List[pydxdiag.schema.Filter.Filter]
        """
        return Filter.GetFilters(self.dxXML)
    def GetPreferredDShowFilters(self) -> List[str]:
        """
        Function to get the Preferred DShow Filters from the dxdiag output\n
        :return: List of Filter objects
        :rtype: List[str]
        """
        return Filter.GetPreferredDShowFilters(self.dxXML)
    def GetLogicalDisks(self) -> List[pydxdiag.schema.LogicalDisk.LogicalDisk]:
        """
        Function to get the Logical Disks from the dxdiag output\n
        :return: List of Logical Disks
        :rtype: List[pydxdiag.schema.LogicalDisk.LogicalDisk]
        """
        return LogicalDisk.GetLogicalDisks(self.dxXML)
    def GetOSInformation(self) -> pydxdiag.schema.SystemInformation.OSInformation:
        """
        Function to get the OS Information from the dxdiag output\n
        :return: The OS Information
        :rtype: pydxdiag.schema.SystemInformation.OSInformation
        """
        return SystemInformation.GetOSInformation(self.dxXML)
    def GetDirectXDebugLevels(self) -> pydxdiag.schema.DirectXDebugLevels.DirectXDebugLevels:
        """
        Function to get the DirectX Debug Levels from the dxdiag output\n
        :return: List of DirectX Debug Levels
        :rtype: pydxdiag.schema.DirectXDebugLevels.DirectXDebugLevels
        """
        return SystemInformation.GetDirectXDebugLevels(self.dxXML)
    def GetDxDiagNotes(self) -> List[pydxdiag.schema.DxDiagNotes.GeneralDXDiagNotes]:
        """
        Function to get the DxDiag Notes from the dxdiag output\n
        :return: List of DxDiag Notes
        :rtype: List[pydxdiag.schema.DxDiagNotes.GeneralDXDiagNotes]
        """
        return SystemInformation.GetDxDiagNotes(self.dxXML)
    def GetMachineInformation(self) -> pydxdiag.schema.SystemInformation.MachineInformation:
        """
        Function to get the Machine Information from the dxdiag output\n
        :return: The Machine Information
        :rtype: pydxdiag.schema.SystemInformation.MachineInformation
        """
        return SystemInformation.GetMachineInformation(self.dxXML)
    def GetSystemModelInformation(self) -> pydxdiag.schema.SystemInformation.SystemModelInformation:
        """
        Function to get the System Model Information from the dxdiag output\n
        :return: The System Model Information
        :rtype: pydxdiag.schema.SystemInformation.SystemModelInformation
        """
        return SystemInformation.GetSystemModelInformation(self.dxXML)
    def GetFirmwareInformation(self) -> pydxdiag.schema.SystemInformation.FirmwareInformation:
        """
        Function to get the Firmware Information from the dxdiag output\n
        :return: The Firmware Information
        :rtype: pydxdiag.schema.SystemInformation.FirmwareInformation
        """
        return SystemInformation.GetFirmwareInformation(self.dxXML)
    def GetCPUInformation(self) -> pydxdiag.schema.SystemInformation.CPUInformation:
        """
        Function to get the CPU Information from the dxdiag output\n
        :return: The CPU Information
        :rtype: pydxdiag.schema.SystemInformation.CPUInformation
        """
        return SystemInformation.GetCPUInformation(self.dxXML)
    def GetMemoryInformation(self) -> pydxdiag.schema.SystemInformation.MemoryInformation:
        """
        Function to get the Memory Information from the dxdiag output\n
        :return: The Memory Information
        :rtype: pydxdiag.schema.SystemInformation.MemoryInformation
        """
        return SystemInformation.GetMemoryInformation(self.dxXML)
    def GetGraphicsInfromation(self) -> pydxdiag.schema.SystemInformation.GraphicsInformation:
        """
        Function to get the Graphics Information from the dxdiag output\n
        :return: The Graphics Information
        :rtype: pydxdiag.schema.SystemInformation.GraphicsInformation
        """
        return SystemInformation.GetGraphicsInfromation(self.dxXML)
    def GetDXDiagInformation(self) -> pydxdiag.schema.SystemInformation.DXDiagInformation:
        """
        Function to get the DXDiag Information from the dxdiag output\n
        :return: The DXDiag Information
        :rtype: pydxdiag.schema.SystemInformation.DXDiagInformation
        """
        return SystemInformation.GetDXDiagInformation(self.dxXML)
    def GetWERInfo(self) -> List[pydxdiag.schema.WER.WERInformation]:
        """
        Function to get the WER Information from the dxdiag output\n
        :return: List of WER Information
        :rtype: List[pydxdiag.schema.WER.WERInformation]
        """
        return WERFuncs.GetWERInfo(self.dxXML)
