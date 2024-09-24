from pydantic import (
    BaseModel,
    Field,
)

class GeneralDXDiagNotes(BaseModel):
    """
    Class to represent general dxdiag notes.\n
    :params Notes: Notes
    :type Notes: str
    :params Type: Type of the notes
    :type Type: str
    """
    Notes: str = Field(...)
    Type: str = Field(...)

class DisplayTabNotes(GeneralDXDiagNotes):
    """
    Class to represent display tab notes.\n
    Inherits from `GeneralDXDiagNotes`.\n
    """
    Type: str = "DisplayTab"

class SoundTabNotes(GeneralDXDiagNotes):
    """
    Class to represent sound tab notes.\n
    Inherits from `GeneralDXDiagNotes`.\n
    """
    Type: str = "SoundTab"

class InputTabNotes(GeneralDXDiagNotes):
    """
    Class to represent input tab notes.\n
    Inherits from `GeneralDXDiagNotes`.\n
    """
    Type: str = "InputTab"