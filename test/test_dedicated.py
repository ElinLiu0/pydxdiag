import bs4
from bs4.element import Tag
from typing import List

with open("../out.xml", "r",encoding="utf-8") as f:
    dxXML = bs4.BeautifulSoup(f.read(), "xml")
    VideoCaptureDevices:List[Tag] = dxXML.find("DxDiag").find("VideoCaptureDevices").find_all("VideoCaptureDevice")
    for device in VideoCaptureDevices:
        print(
            device.find("Manufacturer")
        )