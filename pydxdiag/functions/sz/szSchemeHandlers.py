from pydxdiag.schema.sz.szSchemeHandlers import *
from typing import *
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetSchemeHandlers(
    dxXML:BeautifulSoup
) -> List[szSchemeHandlers]:
    """
    Function to get the scheme handlers from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return SchemeHandlers: The scheme handlers
    :rtype SchemeHandlers: List[szSchemeHandlers]
    """
    tag:str = dxXML.find("DxDiag").find("MediaFoundation").find("szSchemeHandlers").text
    SchemeHandlers:List[szSchemeHandlers] = []
    for i in tag.split("\n"):
        line:str = i.strip()
        if line == "":
            continue
        SchemeHandlers.append(
            szSchemeHandlers(
                Name = line.split(",")[2].strip(),
                SupportedFormat = line.split(",")[0].strip(),
                HandlerID = line.split(",")[1].strip().replace("{","").replace("}",""),
                IsPreferred = True if len(line.split(",")) > 3 and line.split(",")[3].strip() == "Preferred" else False,
            )
        )
    return SchemeHandlers