from pydantic import BaseModel, Field
from typing import Optional


class GeneralDXDebugLevelInformation(BaseModel):
    """
    A class for storing the general debug information of the DirectX Component\n
    :params Current: The current debug level of the DirectX Component.
    :types Current: int
    :params Max: The maximum debug level of the DirectX Component.
    :types Max: int
    :params Runtime: The runtime for the DirectX Component.
    :types Runtime: Optional[str]
    """
    Current:int = Field(
        ...,
        title="Current Debug Level",
        description="The current debug level of the DirectX Component"
    )
    Max:int = Field(
        ...,
        title="Maximum Debug Level",
        description="The maximum debug level of the DirectX Component"
    )
    Runtime:Optional[str] = Field(
        None,
        title="Runtime",
        description="The runtime for the DirectX Component"
    )

class D3DDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the D3D\n
    :params Current: The current debug level of the D3D
    :types Current: int
    :params Max: The maximum debug level of the D3D
    :types Max: int
    :params Runtime: The runtime for the D3D
    :types Runtime: Optional[str]
    """

class DirectDrawDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the DirectDraw\n
    :params Current: The current debug level of the DirectDraw
    :types Current: int
    :params Max: The maximum debug level of the DirectDraw
    :types Max: int
    :params Runtime: The runtime for the DirectDraw
    :types Runtime: Optional[str]
    """

class DirectInputDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the DirectInput\n
    :params Current: The current debug level of the DirectInput
    :types Current: int
    :params Max: The maximum debug level of the DirectInput
    :types Max: int
    :params Runtime: The runtime for the DirectInput
    :types Runtime: Optional[str]
    """

class DirectMusicDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the DirectMusic\n
    :params Current: The current debug level of the DirectMusic
    :types Current: int
    :params Max: The maximum debug level of the DirectMusic
    :types Max: int
    :params Runtime: The runtime for the DirectMusic
    :types Runtime: Optional[str]
    """

class DirectPlayDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the DirectPlay\n
    :params Current: The current debug level of the DirectPlay
    :types Current: int
    :params Max: The maximum debug level of the DirectPlay
    :types Max: int
    :params Runtime: The runtime for the DirectPlay
    :types Runtime: Optional[str]
    """

class DirectSoundDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the DirectSound\n
    :params Current: The current debug level of the DirectSound
    :types Current: int
    :params Max: The maximum debug level of the DirectSound
    :types Max: int
    :params Runtime: The runtime for the DirectSound
    :types Runtime: Optional[str]
    """

class DirectShowDebugInformation(GeneralDXDebugLevelInformation):
    """
    Debug information of the DirectShow\n
    :params Current: The current debug level of the DirectShow
    :types Current: int
    :params Max: The maximum debug level of the DirectShow
    :types Max: int
    :params Runtime: The runtime for the DirectShow
    :types Runtime: Optional[str]
    """
    
class DirectXDebugLevels:
    """
    Debug levels of the DirectX\n
    :params D3DDebugInformation: The debug information of the D3D
    :types D3DDebugInformation: D3DDebugInformation
    :params DirectDrawDebugInformation: The debug information of the DirectDraw
    :types DirectDrawDebugInformation: DirectDrawDebugInformation
    :params DirectInputDebugInformation: The debug information of the DirectInput
    :types DirectInputDebugInformation: DirectInputDebugInformation
    :params DirectMusicDebugInformation: The debug information of the DirectMusic
    :types DirectMusicDebugInformation: DirectMusicDebugInformation
    :params DirectPlayDebugInformation: The debug information of the DirectPlay
    :types DirectPlayDebugInformation: DirectPlayDebugInformation
    :params DirectSoundDebugInformation: The debug information of the DirectSound
    :types DirectSoundDebugInformation: DirectSoundDebugInformation
    :params DirectShowDebugInformation: The debug information of the DirectShow
    :types DirectShowDebugInformation: DirectShowDebugInformation
    """
    D3DDebugInformation:D3DDebugInformation
    DirectDrawDebugInformation:DirectDrawDebugInformation
    DirectInputDebugInformation:DirectInputDebugInformation
    DirectMusicDebugInformation:DirectMusicDebugInformation
    DirectPlayDebugInformation:DirectPlayDebugInformation
    DirectSoundDebugInformation:DirectSoundDebugInformation
    DirectShowDebugInformation:DirectShowDebugInformation