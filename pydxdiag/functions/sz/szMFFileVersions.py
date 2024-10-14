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
    MFFileVersionsTags:List[str] = dxXML.find("DxDiag").find("MediaFoundation").find("szMFFileVersions").text.split("\n")
    MFFileVersionsStrings:List[szMFFileVersion] = []
    for MFFileVersion in MFFileVersionsTags:
        if MFFileVersion == "":
            continue
        Name, Version = [Info.strip() for Info in MFFileVersion.split(", ")]
        MFFileVersionsStrings.append(
            szMFFileVersion(
                Name=Name,
                Version=Version
            )
        )

    return MFFileVersionsStrings