from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok", "app": "fastapi-simple"}


@router.get("/greet")
def greet(name: str = "world"):
    return {"message": f"Hello, {name}!"}
