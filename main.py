import pytz

from datetime import datetime
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

# 創建一個 FastAPI 應用實例, 提供了許多功能的 Class
app = FastAPI()

# 最基本的 API
# 定義一個 GET 請求的裝飾器，用於根路徑 "/"
@app.get("/")
async def root(): # 也可以是同步 def root, 不加 async
    """
    處理根路徑 ("/") 的 GET 請求

    Returns:
        dict: 包含歡迎訊息的 json
    """
    print("用戶 GET 訪問 /")
    return {"message": "Hello World"}

# 搭配 pydantic
# 定義 Pydantic 模型
class Person(BaseModel):
    id: int
    name: str
    gender: str
    created_at: int

# 用戶要提交的資料
class PersonCreate(BaseModel):
    id: int
    name: str
    gender: str

# 模擬數據
persons = [
    Person(id=1, name="Alice", gender="Female", created_at=1716534549),
    Person(id=2, name="Bob", gender="Male", created_at=1716534249),
    Person(id=3, name="Charlie", gender="Other", created_at=1716524510)
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

# 定義 POST 請求的裝飾器，用於路徑 "/person"
@app.post("/person", response_model=Person)
async def create_person(person: PersonCreate):
    """
    處理 "/person" 路徑的 POST 請求

    Args:
        person (PersonCreate): 包含 Person 信息的 JSON 數據

    Returns:
        Person: 包含新創建的 Person 信息的 JSON
    """
    print("用戶 POST 訪問 /person")

    # 檢查請求體是否包含內容
    if not person:
        raise HTTPException(status_code=400, detail="Invalid input, no data provided")

    # 生成 created_at 時間戳
    taiwan_tz = pytz.timezone('Asia/Taipei')
    created_at = int(datetime.now(taiwan_tz).timestamp())

    # 創建新的 Person 對象
    new_person = Person(id=person.id, name=person.name, gender=person.gender, created_at=created_at)

    # 模擬將新 Person 對象添加到數據庫
    persons.append(new_person)

    return new_person

# 定義404錯誤
class ErrorResponse(BaseModel):
    detail: str

# 定義 GET 請求的裝飾器，用於路徑 "/person"
@app.get("/person", response_model=Person, responses={404: {"model": ErrorResponse, "description": "Person not found"}})
async def get_person(id: int = Query(..., description="The ID of the person to retrieve")):
    """
    處理 "/person" 路徑的 GET 請求

    Args:
        id (int): Person 的 ID

    Returns:
        Person: 對應的 Person 對象的 JSON 數據
    """
    print(f"用戶 GET 訪問 /person?id={id}")

    # 從 persons 列表中查找具有給定 ID 的 Person 物件
    for person in persons:
        if person.id == id:
            return person
    
    # 如果未找到，抛出 404 錯誤
    raise HTTPException(status_code=404, detail="Person not found")