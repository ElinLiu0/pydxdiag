from pydxdiag.schema.sz.szEnableHarewareMFT import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetStatufForEnableHardwareMFT(
    dxXML:BeautifulSoup
) -> szEnableHardwareMFT:
    """
    Function to get the status for enabling hardware MFT from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return EnableHardwareMFT: The status for enabling hardware MFT
    :rtype EnableHardwareMFT: szEnableHarewareMFT
    """
    tag:str = dxXML.find("DxDiag").find("MediaFoundation").find("szEnabledHardwareMFTs").text
    tag:str = tag.split("\n")
    HardMFTStatus:szEnableHardwareMFT = szEnableHardwareMFT(
        EnableEncoders = False,
        EnableDecoders = False
    )
    for i in tag:
        if i.startswith("EnableEncoders"):
            HardMFTStatus.EnableEncoders = bool(int(i.split("=")[1].strip()))
        if i.startswith("EnableDecoders"):
            HardMFTStatus.EnableDecoders = bool(int(i.split("=")[1].strip()))

    return HardMFTStatus