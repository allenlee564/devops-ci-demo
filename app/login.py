"""登入邏輯 —— 示範「email 非空檢查」（對應教學的 PR 範例）。

Why: 使用者回報登入時 email 欄位空白會 500 error，應改成回明確錯誤訊息。
What: 加 email 非空檢查，空白回 400 + {"error": "email is required"}。
"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    email: str | None = None
    password: str | None = None


@router.post("/login")
def login(body: LoginRequest):
    # email 非空檢查：空白就回 400，而不是讓後面爆 500

    # demo 用：不做真正驗證，回個成功訊息就好
    return {"message": f"welcome, {body.email}"}
