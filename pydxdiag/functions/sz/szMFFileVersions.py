from pydxdiag.schema.sz.szMFFileVersion import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetMFFileVersions(
    dxXML:BeautifulSoup,
) -> List[szMFFileVersion]:
    """
    Function to get the media foundation file versions from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[MFFileVersion]: The media foundation file versions information
    :rtype List[MFFileVersion]: List[MFFileVersion]
    """
    MFFileVersions:str = dxXML.find("DxDiag").find("MediaFoundation").find("szMFFileVersions").text.split("\n")
    MFFileVersions:List[szMFFileVersion] = []
    for MFFileVersion in MFFileVersions:
        Name, Version = MFFileVersion.split(", ")
        MFFileVersions.append(
            szMFFileVersion(
                Name=Name,
                Version=Version
            )
        )

    return MFFileVersions