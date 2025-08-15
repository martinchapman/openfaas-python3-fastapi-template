from pydantic import BaseModel
from typing import Dict

class RequestModel(BaseModel):
    data: Dict


class ResponseModel(BaseModel):
    data: Dict