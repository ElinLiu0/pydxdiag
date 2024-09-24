from pydxdiag.schema.Filter import Filter
from typing import *
from datetime import datetime
from bs4 import BeautifulSoup
from bs4.element import Tag

def GetPreferredDShowFilters(
    dxXML:BeautifulSoup,
) -> List[str]:
    """
    Function to get the preferred direct show filters from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[str]: The preferred direct show filters
    :rtype List[str]: List[str]
    """
    return [
        filterName.strip()
        for filterName in dxXML.find("DxDiag").find_all("DirectShow")[1].find("PreferredDShowFilters").text.split(",")
    ]

def GetFilters(
    dxXML:BeautifulSoup,
) -> List[Filter]:
    """
    Function to get the filters from the dxdiag xml.\n
    :param dxXML: The dxdiag xml
    :type dxXML: BeautifulSoup
    :return List[Filter]: The filters information
    :rtype List[Filter]: List[Filter]
    """
    FilterTags:List[Tag] = dxXML.find("DxDiag").find("DirectShow").find_all("Filter")
    Filters:List[Filter] = []
    for filtertag in FilterTags:
        Name:str = filtertag.find("Name").text
        FilterCategory:str = filtertag.find("FilterCategory").text
        Merit:int = int(filtertag.find("Merit").text)
        Inputs:int = int(filtertag.find("Inputs").text)
        Outputs:int = int(filtertag.find("Outputs").text)
        File:str = filtertag.find("File").text
        FileVersion:str = filtertag.find("FileVersion").text
        Filters.append(
            Filter(
                Name=Name,
                FilterCategory=FilterCategory,
                Merit=Merit,
                Inputs=Inputs,
                Outputs=Outputs,
                File=File,
                FileVersion=FileVersion
            )
        )
    return Filters
