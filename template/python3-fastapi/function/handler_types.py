from pydantic import BaseModel
from typing import Dict, Any

class RequestModel(BaseModel):
    data: Dict[Any, Any]


class ResponseModel(BaseModel):
    data: Dict[Any, Any]