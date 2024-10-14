from pydantic import BaseModel
class szEnableHardwareMFT(BaseModel):
    """
    Class to represent HardwareMFTs compatibility on device.\n
    :params EnableEncoders: Enable Encoders
    :type EnableEncoders: bool
    :params EnableDecoders: Enable Decoders
    :type EnableDecoders: bool
    """
    EnableEncoders: bool
    EnableDecoders: bool