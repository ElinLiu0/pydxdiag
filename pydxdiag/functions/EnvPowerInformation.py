from pydxdiag.schema.EnvPowerInformation import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetEnvPowerInformation(
    dxXML:BeautifulSoup,   
) -> EnvPowerInformation:
    """
    Function to get the power information from a dxdiag XML file.\n
    :param dxXML: The root of the dxdiag XML tree
    :type dxXML: BeautifulSoup
    :return: The power information in the dxdiag XML file
    :rtype: EnvPowerInformation
    """
    EvrPowerInformationElement:Tag = dxXML.find("DxDiag").find("EvrPowerInformation")
    GUID:str = EvrPowerInformationElement.find("GUID").text.split(" ")[0].replace("{", "").replace("}", "").strip()
    Mode:str = EvrPowerInformationElement.find("GUID").text.split(" ")[1].replace("(", "").replace(")", "").strip()
    QualityFlagsElement:BeautifulSoup = EvrPowerInformationElement.find("QualityFlags")
    QualityFlagsInfo:QualityFlags = QualityFlags(
        Flags = int(QualityFlagsElement.find("Flags").text),
        EnabledOptions = [Option.strip() for Option in QualityFlagsElement.find("Enabled").text.split("\n")],
        DecodePowerUsage = int(QualityFlagsElement.find("DecodePowerUsage").text)
    )
    BalancedFlagsElement:Tag = EvrPowerInformationElement.find("BalancedFlags")
    BalancedFlagsInfo:BalanceFlags = BalanceFlags(
        Flags = int(BalancedFlagsElement.find("Flags").text),
        EnabledOptions = [Option.strip() for Option in BalancedFlagsElement.find("Enabled").text.split("\n")],
        DecodePowerUsage = int(BalancedFlagsElement.find("DecodePowerUsage").text)
    )
    PowerFlagsElement:Tag = EvrPowerInformationElement.find("PowerFlags")
    PowerFlagsInfo:PowerFlags = PowerFlags(
        Flags = int(PowerFlagsElement.find("Flags").text),
        EnabledOptions = [Option.strip() for Option in PowerFlagsElement.find("Enabled").text.split("\n")],
        DecodePowerUsage = int(PowerFlagsElement.find("DecodePowerUsage").text)
    )
    EvrPower:EnvPowerInformation = EnvPowerInformation(
        GUID = GUID,
        Mode = Mode,
        QualityFlagsInfo = QualityFlagsInfo,
        BalanceFlagsInfo = BalancedFlagsInfo,
        PowerFlagsInfo = PowerFlagsInfo
    )
    return EvrPower