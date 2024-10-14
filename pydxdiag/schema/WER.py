from pydantic import (
    BaseModel,
    Field,
)
from typing import *

class ProblemSignature:
    """
    Basic class to describe a problem signature entry.\n
    :params P1: 
    :type P1: Optional[str]
    :params P2:
    :type P2: Optional[str]
    :params P3:
    :type P3: Optional[str]
    :params P4:
    :type P4: Optional[str]
    :params P5:
    :type P5: Optional[str]
    :params P6:
    :type P6: Optional[str]
    :params P7:
    :type P7: Optional[str]
    :params P8:
    :type P8: Optional[str]
    :params P9:
    :type P9: Optional[str]
    :params P10:
    :type P10: Optional[str]
    """
    P1: Optional[str] = Field(None, title="P1")
    P2: Optional[str] = Field(None, title="P2")
    P3: Optional[str] = Field(None, title="P3")
    P4: Optional[str] = Field(None, title="P4")
    P5: Optional[str] = Field(None, title="P5")
    P6: Optional[str] = Field(None, title="P6")
    P7: Optional[str] = Field(None, title="P7")
    P8: Optional[str] = Field(None, title="P8")
    P9: Optional[str] = Field(None, title="P9")
    P10: Optional[str] = Field(None, title="P10")
    
    def model_dump(self) -> Dict[str, str]:
        """
        Function to dump the model into a dictionary.\n
        :returns: A dictionary containing the model
        :rtype: Dict[str, str]
        """
        return {
            "P1": self.P1,
            "P2": self.P2,
            "P3": self.P3,
            "P4": self.P4,
            "P5": self.P5,
            "P6": self.P6,
            "P7": self.P7,
            "P8": self.P8,
            "P9": self.P9,
            "P10": self.P10
        }
    
    def __repr__(self):
        return f"ProblemSignature(P1={self.P1}, P2={self.P2}, P3={self.P3}, P4={self.P4}, P5={self.P5}, P6={self.P6}, P7={self.P7}, P8={self.P8}, P9={self.P9}, P10={self.P10})"

class WERInformation:
    """
    Basic class to describe a Windows Error Reporting (WER) entry.\n
    :params FaultBucket: The bucket ID for the error
    :type FaultBucket: str
    :params EventName: The name of the event
    :type EventName: str
    :params Response: The response of the event
    :type Response: str
    :params CabId: The CAB ID for the event
    :type CabId: int
    :params ProblemSignatures: The problem signature for the event
    :type ProblemSignatures: ProblemSignature
    """
    def __init__(
        self,
        FaultBucket: str,
        EventName: str,
        Response: str,
        CabId: int,
        ProblemSignatures: ProblemSignature
    ) -> None:
        self.FaultBucket = FaultBucket
        self.EventName = EventName
        self.Response = Response
        self.CabId = CabId
        self.ProblemSignatures = ProblemSignatures

    def model_dump(self) -> Dict[str, Any]:
        """
        Function to dump the model into a dictionary.\n
        :returns: A dictionary containing the model
        :rtype: Dict[str, Any]
        """
        return {
            "FaultBucket": self.FaultBucket,
            "EventName": self.EventName,
            "Response": self.Response,
            "CabId": self.CabId,
            "ProblemSignatures": self.ProblemSignatures.model_dump()
        }

    def __repr__(self):
        return f"WERInformation(FaultBucket={self.FaultBucket}, EventName={self.EventName}, Response={self.Response}, CabId={self.CabId}, ProblemSignatures={self.ProblemSignatures})"