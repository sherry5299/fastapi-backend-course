from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional  # 引入 Optional

# 如果您要使用資料庫，請確保正確引入資料庫部分
from .database import Base, engine
from .routers import router

app = FastAPI()

# Initialize Database's Table
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(router=router, prefix="/api", tags=["todos"])

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None  # 使用 Optional，表示 description 可以為 None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: Item):
    print(f"Received item: {item}")
    return {"message": "Item received", "item": item}
