from pydxdiag.schema.sz.szBytesStreamHandler import *
from typing import *
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetBytesStreamHandlers(
    dxXML:BeautifulSoup,
) -> List[szBytesStreamHandler]:
    """
    Function to get the bytes stream handler from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return BytesStreamHandlers: The bytes stream handler
    :rtype BytesStreamHandlers: List[szBytesStreamHandler]
    """
    tag:str = dxXML.find("DxDiag").find("MediaFoundation").find("szByteStreamHandlers").text
    BytesStreamHandlers:List[szBytesStreamHandler] = []
    for i in tag.split("\n"):
        line:str = i.strip()
        if line == "":
            continue
        BytesStreamHandlers.append(
            szBytesStreamHandler(
                Name = line.split(",")[2].strip(),
                SupportedFormat = line.split(",")[0].strip(),
                HandlerID = line.split(",")[1].strip().replace("{","").replace("}",""),
                IsPreferred = True if line.split(",")[-1].strip() == "Preferred" else False
            )
        )
    return BytesStreamHandlers