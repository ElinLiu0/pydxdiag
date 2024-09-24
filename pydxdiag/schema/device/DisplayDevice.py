from datetime import datetime
from pydantic import BaseModel, Field
from typing import *


class MPO(BaseModel):
    """
    MPO Information of the Monitor\n
    :params MaxPlanes: Maximum Planes
    :type MaxPlanes: int
    :params Caps: Caps Supported by MPO
    :type Caps: List[str]
    :params Stretch: Stretch Supported by MPO
    :type Stretch: Optional[tuple[float, float]]
    :params Hints: Hints of MPO
    :type Hints: str
    :params Formats: Formats Supported by MPO
    :type Formats: List[str]
    """
    MaxPlanes: int = Field(..., description="Maximum Planes")
    Caps: List[str] = Field(..., description="Caps Supported by MPO")
    Stretch: Optional[tuple[float, float]] = Field(..., description="Stretch Supported by MPO")
    Hints: str = Field(..., description="Hints of MPO")
    Formats: List[str] = Field(..., description="Formats Supported by MPO")

class DXVADeinterplaceCap(BaseModel):
    """
    DXVA Deinterplace Capabilities of the Monitor\n
    :params GUID: GUID of the DXVA Deinterplace Cap
    :type GUID: str
    :params D3DInputFormat: D3D Input Format of the DXVA Deinterplace Cap
    :type D3DInputFormat: str
    :params D3DOutputFormat: D3D Output Format of the DXVA Deinterplace Cap
    :type D3DOutputFormat: str
    :params Caps: Caps of the DXVA Deinterplace Cap
    :type Caps: List[str]
    :params NumPreviousOutputFrames: Number of Previous Output Frames of the DXVA Deinterplace Cap
    :type NumPreviousOutputFrames: int
    :params NumForwardRefSamples: Number of Forward Reference Samples of the DXVA Deinterplace Cap
    :type NumForwardRefSamples: int
    :params NumBackwardRefSamples: Number of Backward Reference Samples of the DXVA Deinterplace Cap
    :type NumBackwardRefSamples: int
    """
    GUID: str = Field(..., description="GUID of the DXVA Deinterplace Cap")
    D3DInputFormat: str = Field(..., description="D3D Input Format of the DXVA Deinterplace Cap")
    D3DOutputFormat: str = Field(..., description="D3D Output Format of the DXVA Deinterplace Cap")
    Caps: List[str] = Field(..., description="Caps of the DXVA Deinterplace Cap")
    NumPreviousOutputFrames: int = Field(..., description="Number of Previous Output Frames of the DXVA Deinterplace Cap")
    NumForwardRefSamples: int = Field(..., description="Number of Forward Reference Samples of the DXVA Deinterplace Cap")
    NumBackwardRefSamples: int = Field(..., description="Number of Backward Reference Samples of the DXVA Deinterplace Cap")


class ColorPrimaries:
    """
    Color Primaries of the GPU\n
    :params Red: Red Color Primary
    :type Red: tuple(float, float)
    :params Green: Green Color Primary
    :type Green: tuple(float, float)
    :params Blue: Blue Color Primary
    :type Blue: tuple(float, float)
    :params WhitePoint: Point Color Primary
    :type WhitePoint: tuple(float, float)
    """
    Red: tuple[float, float] = Field(..., description="Red Color Primary")
    Green: tuple[float, float] = Field(..., description="Green Color Primary")
    Blue: tuple[float, float] = Field(..., description="Blue Color Primary")
    WhitePoint: tuple[float, float] = Field(..., description="WhitePoint Color Primary")

class Luminance:
    """
    Luminance of the GPU\n
    :params Min: Minimum Luminance
    :type Min: float
    :params Max: Maximum Luminance
    :type Max: float
    :params MaxFullFrame: Maximum Full Frame Luminance
    :type MaxFullFrame: float
    """
    Min: float = Field(..., description="Minimum Luminance")
    Max: float = Field(..., description="Maximum Luminance")
    MaxFullFrame: float = Field(..., description="Maximum Full Frame Luminance")

class HardwareSchedulingAttributes:
    """
    Class to describe the Hardware Scheduling Attributes\n
    :params DriverSupportState: Driver Support State
    :type DriverSupportState: str
    :params Enabled: HardwareSchedulingAttributes Enabled
    :type Enabled: Union[bool, str]
    """
    DriverSupportState: str
    Enabled: Union[bool, str]


class DisplayDevice(BaseModel):
    """
    Display Device Information for GPU Devices\n
    :params CardName: Name of the GPU
    :type CardName: str
    :params Manufacturer: Manufacturer of the GPU
    :type Manufacturer: str
    :params ChipType: Chip Type of the GPU
    :type ChipType: str
    :params DACType: DAC Type of the GPU
    :type DACType: str
    :params DeviceType: Device Type of the GPU
    :type DeviceType: str
    :params DeviceKey: Device Key of the GPU
    :type DeviceKey: str
    :params DisplayMemory: Display Memory of the GPU in bytes
    :type DisplayMemory: int
    :params DedicatedMemory: Dedicated Memory of the GPU in bytes
    :type DedicatedMemory: int
    :params SharedMemory: Shared Memory of the GPU in bytes
    :type SharedMemory: int
    :params ResoultionWidth: Resolution Width of the GPU
    :type ResolutionWidth: int
    :params ResolutionHeight: Resolution Height of the GPU
    :type ResolutionHeight: int
    :params ColorBits: Color Bits of the GPU
    :type ColorBits: int
    :params RefreshRate: Refresh Rate of the GPU
    :type RefreshRate: int
    :params HDRSupported: HDR Supported by the GPU
    :type HDRSupported: bool
    :params Topology: Topology of the GPU
    :type Topology: str
    :params ColorSpace: Color Space of the GPU
    :type ColorSpace: str
    :params ColorPrimaries: Color Primaries of the GPU
    :type ColorPrimaries: ColorPrimaries
    :params Luminance: Luminance of the GPU
    :type Luminance: Luminance
    :params MonitorName: Name of the Monitor
    :type MonitorName: Optional[str]
    :params MonitorId: ID of the Monitor
    :type MonitorId: Optional[str]
    :params NativeWidth: Native Width of the Monitor
    :type NativeWidth: int
    :params NativeHeight: Native Height of the Monitor
    :type NativeHeight: int
    :params NativeRefreshRate: Native Refresh Rate of the Monitor
    :type NativeRefreshRate: int
    :params OutputType: Output Type of the Monitor
    :type OutputType: Optional[str]
    :params Eotf2084Supported: EOTF 2084 Supported by the Monitor
    :type Eotf2084Supported: bool
    :params BT20YCC: BT20YCC Supported by the Monitor
    :type BT20YCC: bool
    :params BT2020RGB: BT2020RGB Supported by the Monitor
    :type BT2020RGB: bool
    :params AdavancedColorEnabled: Advanced Color Enabled by the Monitor
    :type AdavancedColorEnabled: bool
    :params AdavancedColorSupported: Advanced Color Supported by the Monitor
    :type AdavancedColorSupported: bool
    :params bCheckedMonitorCapabilities: Checked Monitor Capabilities
    :type bCheckedMonitorCapabilities: bool
    :params PixelFormat: Pixel Format of the Monitor
    :type PixelFormat: Optional[str]s
    :params MonitorMaxRes: Maximum Resolution of the Monitor
    :type MonitorMaxRes: Optional[str]
    :params DriverName: Driver Name of the Monitor
    :type DriverName: str
    :params DriverVersion: Driver Version of the Monitor
    :type DriverVersion: str
    :params DriverFileVersion: Driver File Version of the Monitor
    :type DriverFileVersion: str
    :params DriverLanguage: Driver Language of the Monitor
    :type DriverLanguage: str
    :params DDIVersion: DDI Version of the Monitor
    :type DDIVersion: int
    :params FeatureLevels: Feature Levels of the Monitor
    :type FeatureLevels: List[str]
    :params DriverModel: Driver Model of the Monitor
    :type DriverModel: str
    :params WDDM Version: WDDM Version of the Monitor
    :type WDDM Version: str
    :params IsBetaDriver: Is that Driver for Monitor is beta or not
    :type IsBetaDriver: bool
    :params IsDebugDriver: Is that Driver for Monitor published as a debug version or not
    :type IsDebugDriver: bool
    :params DriverDate: Driver Date of the Monitor
    :type DriverDate: datetime
    :params DriverSize: Driver Binary Size in bytes(I guess?)
    :type DriverSize: int
    :params WHQLLogo: Is that Driver for Monitor has WHQL Logo or not
    :type WHQLLogo: bool
    :params WHQLDate: WHQL Date of the Monitor
    :type WHQLDate: Optional[datetime]
    :params VDD: VDD of the Monitor
    :type VDD: Optional[Any]
    :params MiniVDD: Mini VDD of the Monitor
    :type MiniVDD: Optional[Any]
    :params MiniVDDDate: Mini VDD Date of the Monitor
    :type MiniVDDDate: Optional[datetime]
    :params MiniVDDSize: Mini VDD Size of the Monitor
    :type MiniVDDSize: int
    :params DeviceIdentifier: Device Identifier of the Monitor
    :type DeviceIdentifier: str
    :params VendorID: Vendor ID of the Monitor
    :type VendorID: str
    :params DeviceID: Device ID of the Monitor
    :type DeviceID: str
    :params SubSysID: Sub System ID of the Monitor
    :type SubSysID: str
    :params DriverNodeStrongName: Driver Node Strong Name of the Monitor
    :type DriverNodeStrongName: str
    :params RankOfInstalledDriver: Rank of Installed Driver of the Monitor
    :type RankOfInstalledDriver: str
    :params DXVAModes: DXVA Modes of the Monitor
    :type DXVAModes: Union[List[str],str]   
    :params DXVA2Modes: DXVA2 Modes of the Monitor
    :type DXVA2Modes: List[str]
    :params GraphicsPreemption: Graphics Preemption of the Monitor
    :type GraphicsPreemption: str
    :params ComputePreemption: Compute Preemption of the Monitor
    :type ComputePreemption: str
    :params Miracast: Miracast of the Monitor
    :type Miracast: Optional[str]
    :params DetachableGPU: Is that GPU is detachable or not
    :type DetachableGPU: bool
    :params HybridGraphics: Hybrid Graphics of the Monitor
    :type HybridGraphics: Optional[str]
    :params PowerManagementPStates: Power Management P States of the Monitor
    :type PowerManagementPStates: Optional[str]
    :params VirtualGPUSupport: Virtualization of the Monitor
    :type VirtualGPUSupport: bool
    :params BlockList: Block List of the Monitor
    :type BlockList: str
    :params DriverCatalogAttributes: Driver Catalog Attributes of the Monitor
    :type DriverCatalogAttributes: Dict[str,bool]
    :params MPO: MPO Information of the Monitor
    :type MPO: MPO
    :params PanelFilterCaps: Panel Filter Caps of the Monitor
    :type PanelFilterCaps: Optinal[Any]
    :params HardwareSchedulingAttributesInfo: Hardware Scheduling Attributes of the Monitor
    :type HardwareSchedulingAttributesInfo: HardwareSchedulingAttributes
    :params DisplayableSupport: Displayable Support of the Monitor
    :type DisplayableSupport: bool
    :params DXVADeinterlaceCaps: DXVA Deinterplace Caps of the Monitor
    :type DXVADeinterlaceCaps: List[DXVADeinterplaceCap]
    :params D3D9Overlay: D3D9 Overlay of the Monitor Supported or not
    :type D3D9Overlay: bool
    :params DXVAHD: DXVA HD of the Monitor Supported or not
    :type DXVAHD: bool
    :params DDrawStatus: DDraw Status of the Monitor
    :type DDrawStatus: bool
    :params D3DStatus: D3D Status of the Monitor
    :type D3DStatus: bool
    :params AGPStatus: AGP Status of the Monitor
    :type AGPStatus: bool
    """
    CardName: str = Field(..., description="Name of the GPU")
    Manufacturer: str = Field(..., description="Manufacturer of the GPU")
    ChipType: str = Field(..., description="Chip Type of the GPU")
    DACType: str = Field(..., description="DAC Type of the GPU")
    DeviceType: str = Field(..., description="Device Type of the GPU")
    DeviceKey: str = Field(..., description="Device Key of the GPU")
    DisplayMemory: int = Field(..., description="Display Memory of the GPU in bytes")
    DedicatedMemory: int = Field(..., description="Dedicated Memory of the GPU in bytes")
    SharedMemory: int = Field(..., description="Shared Memory of the GPU in bytes")
    ResolutionWidth: int = Field(..., description="Resolution Width of the GPU")
    ResolutionHeight: int = Field(..., description="Resolution Height of the GPU")
    ColorBits: int = Field(..., description="Color Bits of the GPU")
    RefreshRate: int = Field(..., description="Refresh Rate of the GPU")
    HDRSupported: bool = Field(..., description="HDR Supported by the GPU")
    Topology: str = Field(..., description="Topology of the GPU")
    ColorSpace: str = Field(..., description="Color Space of the GPU")
    ColorPrimaries: object = Field(..., description="Color Primaries of the GPU")
    Luminance: object = Field(..., description="Luminance of the GPU")
    MonitorName: Optional[str] = Field(..., description="Name of the Monitor")
    MonitorId: Optional[str] = Field(..., description="ID of the Monitor")
    NativeWidth: int = Field(..., description="Native Width of the Monitor")
    NativeHeight: int = Field(..., description="Native Height of the Monitor")
    NativeRefreshRate: int = Field(..., description="Native Refresh Rate of the Monitor")
    OutputType: Optional[str] = Field(..., description="Output Type of the Monitor")
    Eotf2084Supported: bool = Field(..., description="EOTF 2084 Supported by the Monitor")
    BT20YCC: bool = Field(..., description="BT20YCC Supported by the Monitor")
    BT2020RGB: bool = Field(..., description="BT2020RGB Supported by the Monitor")
    AdavancedColorEnabled: bool = Field(..., description="Advanced Color Enabled by the Monitor")
    AdavancedColorSupported: bool = Field(..., description="Advanced Color Supported by the Monitor")
    bCheckedMonitorCapabilities: bool = Field(..., description="Checked Monitor Capabilities")
    PixelFormat: Optional[str] = Field(..., description="Pixel Format of the Monitor")
    MonitorMaxRes: Optional[str] = Field(None, description="Maximum Resolution of the Monitor")
    DriverName: str = Field(..., description="Driver Name of the Monitor")
    DriverVersion: str = Field(..., description="Driver Version of the Monitor")
    DriverFileVersion: str = Field(..., description="Driver File Version of the Monitor")
    DriverLanguage: str = Field(..., description="Driver Language of the Monitor")
    DDIVersion: int = Field(..., description="DDI Version of the Monitor")
    FeatureLevels: List[str] = Field(..., description="Feature Levels of the Monitor")
    DriverModel: str = Field(..., description="Driver Model of the Monitor")
    WDDMVersion: str = Field(..., description="WDDM Version of the Monitor")
    IsBetaDriver: bool = Field(..., description="Is that Driver for Monitor is beta or not")
    IsDebugDriver: bool = Field(..., description="Is that Driver for Monitor published as a debug version or not")
    DriverDate: datetime = Field(..., description="Driver Date of the Monitor")
    DriverSize: int = Field(..., description="Driver Binary Size in bytes(I guess?)")
    WHQLLogo: bool = Field(..., description="Is that Driver for Monitor has WHQL Logo or not")
    WHQLDate: Optional[datetime] = Field(..., description="WHQL Date of the Monitor")
    VDD: Optional[Any] = Field(None, description="VDD of the Monitor")
    MiniVDD: Optional[Any] = Field(None, description="Mini VDD of the Monitor")
    MiniVDDDate: Optional[datetime] = Field(None, description="Mini VDD Date of the Monitor")
    MiniVDDSize: int = Field(..., description="Mini VDD Size of the Monitor")
    DeviceIdentifier: str = Field(..., description="Device Identifier of the Monitor")
    VendorID: str = Field(..., description="Vendor ID of the Monitor")
    DeviceID: str = Field(..., description="Device ID of the Monitor")
    SubSysID: str = Field(..., description="Sub System ID of the Monitor")
    DriverNodeStrongName: str = Field(..., description="Driver Node Strong Name of the Monitor")
    RankOfInstalledDriver: str = Field(..., description="Rank of Installed Driver of the Monitor")
    DXVAModes: Union[List[str],str] = Field(..., description="DXVA Modes of the Monitor")
    DXVA2Modes: List[str] = Field(..., description="DXVA2 Modes of the Monitor")
    GraphicsPreemption: str = Field(..., description="Graphics Preemption of the Monitor")
    ComputePreemption: str = Field(..., description="Compute Preemption of the Monitor")
    Miracast: Optional[str] = Field(..., description="Miracast of the Monitor")
    DetachableGPU: bool = Field(..., description="Is that GPU is detachable or not")
    HybridGraphics: Optional[str] = Field(..., description="Hybrid Graphics of the Monitor")
    PowerManagementPStates: Optional[str] = Field(..., description="Power Management P States of the Monitor")
    VirtualGPUSupport: bool = Field(..., description="Virtualization capability of the GPU")
    BlockList: str = Field(..., description="Block List of the Monitor")
    DriverCatalogAttributes: Dict[str,bool] = Field(..., description="Driver Catalog Attributes of the Monitor")
    MPOInfo: MPO = Field(..., description="MPO Information of the Monitor")
    PanelFilterCaps: Optional[Any] = Field(None, description="Panel Filter Caps of the Monitor")
    HardwareSchedulingAttributesInfo: object = Field(..., description="Hardware Scheduling Attributes of the Monitor")
    DisplayableSupport: bool = Field(..., description="Displayable Support of the Monitor")
    DXVADeinterlaceCaps: List[object] = Field(..., description="DXVA Deinterplace Caps of the Monitor")
    D3D9Overlay: bool = Field(..., description="D3D9 Overlay of the Monitor Supported or not")
    DXVAHD: bool = Field(..., description="DXVA HD of the Monitor Supported or not")
    DDrawStatus: bool = Field(..., description="DDraw Status of the Monitor")
    D3DStatus: bool = Field(..., description="D3D Status of the Monitor")
    AGPStatus: bool = Field(..., description="AGP Status of the Monitor")
    

