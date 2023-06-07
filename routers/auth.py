from fastapi import APIRouter

router = APIRouter()


@router.get("/api/auth")
async def get_user():
    return {"user": "authenticated"}
