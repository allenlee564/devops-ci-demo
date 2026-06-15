"""單元測試 —— 用 FastAPI 的 TestClient，不用真的開 server。"""
from fastapi.testclient import TestClient
from app.main import app

# 建立 TestClient，它會在記憶體內直接模擬 API 請求，速度快且獨立
client = TestClient(app)

def test_login_empty_email():
    """測試案例 1：當 email 為空字串時，預期回傳 400 錯誤與對應的錯誤訊息"""
    r = client.post("/login", json={"email": "", "password": "x"})
    assert r.status_code == 400
    assert r.json() == {"error": "email is required"}

def test_login_ok():
    """測試案例 2：當輸入正常的 email 時，預期回傳 200 成功"""
    r = client.post("/login", json={"email": "a@b.com", "password": "x"})
    assert r.status_code == 200
    assert "welcome" in r.json()["message"]
