from fastapi import Request, HTTPException
from .handler_types import RequestModel, ResponseModel

async def handle(request: Request, req: RequestModel) -> ResponseModel:
    """handle a request to the function
    Args:
        req (dict): request body
    """
    try:
        res: ResponseModel = ResponseModel(data=req.data)
    except Exception:
        raise HTTPException(status_code=500, detail=f'An API Error occurred')
    return res
