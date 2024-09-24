from pydxdiag.schema.sz.szPreferredMFT import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetszPreferedMFTs(
    dxXML:BeautifulSoup
) -> List[szPreferredMFT]:
    """
    Function to get all preferred MFTs from a dxdiag XML file.\n
    :param dxXML: The root of the dxdiag XML tree
    :type dxXML: BeautifulSoup\n
    :return: A list of all preferred MFTs in the dxdiag XML file
    :rtype: List[szPreferredMFT]
    """
    szPreferedMFTs:List[szPreferredMFT] = []
    szPreferedMFTsString:List[str] = dxXML.find("DxDiag").find("MediaFoundation").find("szPreferredMFTs").text.split("\n")
    for mft in szPreferedMFTsString:
        if mft == "":
            continue
        szPreferedMFTs.append(
            szPreferredMFT(
                EngineID = mft.split(",")[0].replace("{", "").replace("}", "").strip(),
                Name = mft.split(",")[1].strip(),
                EngineType = mft.split(",")[2].strip()
            )
        )
    return szPreferedMFTs

def GetszDiasbledMFTs(
    dxXML:BeautifulSoup
) -> Optional[str]:
    """
    Function to get all disabled MFTs from a dxdiag XML file.\n
    :param dxXML: The root of the dxdiag XML tree
    :type dxXML: BeautifulSoup\n
    :return: result in string format
    :rtype: Optional[str]
    """
    return dxXML.find("DxDiag").find("MediaFoundation").find("szDisabledMFTs").text

def GetszDisabledMediaSources(
    dxXML:BeautifulSoup
) -> Optional[str]:
    """
    Function to get all disabled media sources from a dxdiag XML file.\n
    :param dxXML: The root of the dxdiag XML tree
    :type dxXML: BeautifulSoup\n
    :return: result in string format
    :rtype: Optional[str]
    """
    return dxXML.find("DxDiag").find("MediaFoundation").find("szDisabledMediaSources").text