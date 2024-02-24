from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import db_connection
import os

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    last: str

@router.post("/item/")
async def post_item(item: Item):
    db = await db_connection() 
    if db is None:  
        raise HTTPException(status_code=500, detail="Failed to connect to database")
    try:
        result = db.test.insert_one(item.dict())  
        inserted_id = result.inserted_id
        return {"inserted_id": str(inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to add")
    finally:
        if db is not None:  
            db.client.close()  

@router.delete("/item/{item_id}")
async def delete_item(item_id: int):
    db = await db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Failed to connect to database")
    try:
        result = db.test.delete_one({"id": item_id})  
        if result.deleted_count == 1:
            return {"message": "Item deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete")
    finally:
        if db is not None:
            db.client.close()
