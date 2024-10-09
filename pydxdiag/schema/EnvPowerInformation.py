from pydantic import (
    BaseModel,
    Field,
)
from typing import List

class GeneralEnvPowerFlags(BaseModel):
    """
    Abstract class to represent general environment power flags.\n
    :params Flags: Flags of the general environment power flags
    :type Flags: int
    :params EnabledOptions: Enabled options of the general environment power flags
    :type EnabledOptions: List[str]
    :params DecodePowerUsage: Decode power usage of the general environment power flags
    :type DecodePowerUsage: int
    """
    Flags: int = Field(...)
    EnabledOptions: List[str] = Field(...)
    DecodePowerUsage: int = Field(...)

class QualityFlags(GeneralEnvPowerFlags):
    """
    Class to represent quality flags of the general environment power flags.\n
    Inherits from `GeneralEnvPowerFlags`.
    """
    pass

class BalanceFlags(GeneralEnvPowerFlags):
    """
    Class to represent balance flags of the general environment power flags.\n
    Inherits from `GeneralEnvPowerFlags`.
    """
    pass

class PowerFlags(GeneralEnvPowerFlags):
    """
    Class to represent power flags of the general environment power flags.\n
    Inherits from `GeneralEnvPowerFlags`.
    """
    pass

class EnvPowerInformation(BaseModel):
    """
    Class to describe environment power information.\n
    :params GUID: GUID of the environment power information
    :type GUID: str
    :params Mode: Mode of the environment power information
    :type Mode: str
    :params QualityFlagsInfo: Quality flags information of the environment power information
    :type QualityFlagsInfo: QualityFlags
    :params BalanceFlagsInfo: Balance flags information of the environment power information
    :type BalanceFlagsInfo: BalanceFlags
    :params PowerFlagsInfo: Power flags information of the environment power information
    :type PowerFlagsInfo: PowerFlags
    """
    GUID: str = Field(...)
    Mode: str = Field(...)
    QualityFlagsInfo: QualityFlags = Field(...)
    BalanceFlagsInfo: BalanceFlags = Field(...)
    PowerFlagsInfo: PowerFlags = Field(...)

