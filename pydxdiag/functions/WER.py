# Author: Elin
# Date: 2024-09-23 09:06:28
# Last Modified by:   Elin
# Last Modified time: 2024-09-23 09:06:28

from pydxdiag.schema.WER import *
from bs4 import BeautifulSoup
from bs4.element import Tag
import re
from typing import *

def GetWERInfo(
    dxXML: BeautifulSoup,
) -> List[WERInformation]:
    """
    Functions to get information about Windows Error Reporting from the dxdiag XML output.\n
    :param dxXML: dxdiag XML output
    :type dxXML: BeautifulSoup
    :return WERInfoList: Windows Error Reporting information
    :rtype: List[WER]
    """
    WERTags:Tag = dxXML.find("WindowsErrorReporting")
    WERInfoList:List[WERInformation] = []
    Meet:Set[str] = set()
    # Retrieving all children tags under WindowsErrorReporting
    for tag in WERTags.children:
        WERChildText:List[str] = tag.text.split("\n")
        FaultBucketId:str = ""
        if "," in WERChildText[0]:
            FaultBucketId:str = WERChildText[0].split(",")[0].split(" ")[-1].strip()
        elif "，" in WERChildText[0]:
            FaultBucketId:str = WERChildText[0].split("，")[0].split(" ")[-1].strip()
        Type:int = 0
        if "," in WERChildText[0]:
            Type:int = int(WERChildText[0].split(",")[1].split(" ")[-1].strip())
        elif "，" in WERChildText[0]:
            Type:int = int(WERChildText[0].split("，")[1].split(" ")[-1].strip())
        EventName:str = WERChildText[1].split(":")[1].strip()
        Response:str = WERChildText[2].split(":")[1].strip()
        CabId:int = int(WERChildText[3].split(":")[1].strip())

        ProblemSignatures:ProblemSignature = ProblemSignature()
        # Use Regular Expression to get from P1 to P10
        P1toP10:List[str] = re.findall(r"P\d: (.*)", tag.text)
        for i in range(10):
            if i < len(P1toP10):
                setattr(ProblemSignatures, f"P{i+1}", P1toP10[i].split(" ")[-1].strip())
            else:
                setattr(ProblemSignatures, f"P{i+1}", None)
        WERObject:WERInformation = WERInformation(
            FaultBucket=FaultBucketId,
            EventName=EventName,
            Response=Response,
            CabId=CabId,
            ProblemSignatures=ProblemSignatures
        )
        if WERObject.FaultBucket not in Meet:
            WERInfoList.append(WERObject)
            Meet.add(WERObject.FaultBucket)
    return WERInfoList