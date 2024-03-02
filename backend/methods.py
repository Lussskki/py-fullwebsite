from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import db_connection
import os

router = APIRouter()

class Item(BaseModel):
    name: str  
    last: str

# get method only for testing in postman, yet
@router.get("/")
async def get_item():
    try:
        db = await db_connection()
        if db is None:
            raise HTTPException(status_code=500, detail="Failed to connect to the database")
        data_list = list(db.test.find())
        for data in data_list:
            data['_id'] = str(data['_id'])
        return data_list
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve data") from e
    finally:
        if db is not None:
            db.client.close()

# working on put method
@router.put("/item/{item_id}")
async def put_item(item: Item):
    pass

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
async def delete_item(item_id: str):
    try:
        db = await db_connection()
        if db is None:
            raise HTTPException(status_code=500, detail="Failed to connect to database")
        item_id_obj = ObjectId(item_id)
        result = db.test.delete_one({"_id": item_id_obj})  
        if result.deleted_count == 1:
            return {"message": "Item deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete item")
    finally:
        if db is not None:
            db.client.close()