from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def list_users():
    # placeholder - will fetch from DB later
    return [{"id": 1, "username": "kiran"}, {"id": 2, "username": "alice"}]
