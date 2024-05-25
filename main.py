import pytz

from datetime import datetime
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

from models.male import Male
from models.female import Female
from models.person import Person

app = FastAPI()

@app.get("/")
async def root():
    """
    處理根路徑 ("/") 的 GET 請求

    Returns:
        dict: 包含歡迎訊息的 json
    """
    print("用戶 GET 訪問 /")
    return {"message": "Hello World"}

# 模擬數據
persons = [
    Female(id=1, name="Alice", gender="Female", created_at=1716534549),
    Male(id=2, name="Bob", gender="Male", created_at=1716534249),
    Male(id=3, name="Charlie", gender="Other", created_at=1716524510)
]

# 定義 GET 請求的裝飾器，用於路徑 "/persons"
@app.get("/persons", response_model=List[Person])
async def get_persons():
    """
    處理 "/persons" 路徑的 GET 請求

    Returns:
        List[Person]: 包含多個 Person 對象的 JSON 數組
    """
    print("用戶 GET 訪問 /persons")
    return persons

# 定義404錯誤
class ErrorResponse(BaseModel):
    detail: str

@app.get("/person", responses={404: {"model": ErrorResponse, "description": "Person not found"}})
async def get_person_habit(id: int = Query(..., description="The ID of the person to retrieve")):
    """
    處理 "/person" 路徑的 GET 請求

    Args:
        id (int): Person 的 ID

    Returns:
        str: 對應的 Person 對象的 habit 字串
    """
    print(f"用戶 GET 訪問 /person?id={id}")

    # 從 persons 列表中查找具有給定 ID 的 Person 物件
    for person in persons:
        if person.id == id:
            return person.do_habit()
    # 如果未找到，抛出 404 錯誤
    raise HTTPException(status_code=404, detail="Person not found")