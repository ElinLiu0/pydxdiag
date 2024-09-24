import sys
import os

sys.path.append("..")

from pydxdiag.DxdiagParser import DxdiagParser
from loguru import logger
from pathlib import Path
from inspect import getmembers, isfunction,ismethod
import os

os.environ["TEST_FLAG"] = "False"

try:
    logger.debug("Try initalizing dxdiagparser")
    parser = DxdiagParser()
    # Get all of attributes of the parser object
    attributes = getmembers(parser)
    # Retriving all attributes
    for name,attr in attributes:
        if name == "LoadDXDiag":
            break
        if isfunction(attr) == True or ismethod(attr) == True:
            logger.debug(f"Testing function {name}")
            returns = attr()
            assert returns != None
    logger.success("All functions are working")
except Exception as e:
    logger.error(f"Testing corrupted because : {str(e)},full stack trace below:\n")
    raise e