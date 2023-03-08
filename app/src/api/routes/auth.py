from fastapi import APIRouter, status

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post(
    path="/signup",
    name="auth:account-registration",
    status_code=status.HTTP_201_CREATED,
)
async def account_registration_endpoint():
    return {"endpoint": "OK"}


@router.post(
    path="/signin",
    name="auth:account-login",
    status_code=status.HTTP_202_ACCEPTED,
)
async def account_login_endpoint():
    return {"endpoint": "OK"}


@router.post(
    path="/signout",
    name="auth:account-logout",
    status_code=status.HTTP_200_OK,
)
async def account_logout_endpoint():
    return {"endpoint": "OK"}
