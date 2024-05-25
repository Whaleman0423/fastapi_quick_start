# 實作 Flask API 基礎入門

## 使用流程
### 0. 設置 .env
.env
```
# fastapi 預設端口
PORT=8000
```

### 1. 啟動並進入容器
```
docker compose up -d
docker exec -it my-fastapi-app sh
```

### 2. 啟動 FastAPI
```
# 啟動容器
fastapi dev main.py
# 或
uvicorn main:app --host 0.0.0.0 --reload
# 更換端口 5000
uvicorn main:app --host 0.0.0.0 --port 5000

# 生產環境執行
uvicorn main:app --host 0.0.0.0
```

### 3. 至 http://127.0.0.1/8000
1. Swagger UI: http://127.0.0.1:8000/docs  
Swagger UI 讓你透過一個友善的使用者介面來瀏覽API 的所有端點，並進行互動式測試。

2. ReDoc: http://127.0.0.1:8000/redoc  
ReDoc 介面更注重文件的可讀性和佈局，適合用於產生最終的API 文件，但沒有Swagger UI 那樣的互動功能。

### 4. 訪問 API
1. GET, "/"
2. GET, "/persons"
3. POST, "/person", body raw json
```
{
    "id": 0,
    "name": "Jack",
    "gender": "Female"
}
```
4. GET, "/person?id=1"