from pydxdiag.schema.sz.szMFT import *
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetMFTs(
    dxXML: BeautifulSoup
) -> List[szMFT]:
    """
    Function to get the media foundation transforms from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[MFT]: The media foundation transforms information
    :rtype List[MFT]: List[MFT]
    """
    mftstext:List[str] = dxXML.find("szMFTs").text.split("\n")
    mfts:List[szMFT] = []

    EngineType:str = ""
    Name:str = ""
    EngineId:str = ""
    Flags:int = 0
    EngineFile:str = ""
    EngineFileVersion:str = ""

    for line in mftstext:
        if ":" in line:
            EngineType = line.split(":")[0].strip()

        elif "," in line:
            Name:str = line.split(",")[0].strip()
            EngineId:str = line.split(",")[1].strip().replace("{","").replace("}","")
            Flag1:int = int(line.split(",")[2].strip(),16)
            Flag2:int = int(line.split(",")[3].strip(),16) if len(line.split(",")) == 6 else 0
            EngineFile:str = line.split(",")[3].strip() if len(line.split(",")) == 5 else line.split(",")[4].strip()
            EngineFileVersion:str = line.split(",")[4].strip() if len(line.split(",")) == 5 else line.split(",")[5].strip()

            mfts.append(
                szMFT(
                    Name=Name,
                    EngineID=EngineId,
                    Flag1=Flag1,
                    Flag2=Flag2,
                    EngineFile=EngineFile,
                    EngineFileVersion=EngineFileVersion,
                    EngineType=EngineType
                )
            )

            # Clear the variables
            Name:str = ""
            EngineId:str = ""
            Flags:int = 0
            EngineFile:str = ""
            EngineFileVersion:str = ""
            
        else:
            EngineType:str = ""

    return mfts