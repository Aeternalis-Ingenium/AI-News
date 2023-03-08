from fastapi import status
from fastapi.exceptions import HTTPException

from src.utility.messages.exceptions.http.exc_details import http_401_unauthorized_details


async def http_exc_401_unauthorized_request() -> Exception:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=http_401_unauthorized_details(),
    )
