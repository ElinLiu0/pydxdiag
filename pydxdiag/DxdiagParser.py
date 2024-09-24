from bs4 import BeautifulSoup
from typing import *
from pathlib import Path
import subprocess

import sys
import os

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


class DxdiagParser:
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
        