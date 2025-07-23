from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

items = [] #to-do items

class Item(BaseModel):
    text : str = None
    is_done : bool = False
#PS C:\Users\USER\Desktop\fastapi> curl.exe --% -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d "{\"text\": \"papaya\", \"is_done\": false}"
#PS C:\Users\USER\Desktop\fastapi> curl.exe --% -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d "{\"text\": \"banana\"}"                
#>>[{"text":"papaya","is_done":false},{"text":"banana","is_done":false}]

@app.get("/") #defines a path for http get method
def root(): #root directory
    return {"message": "Hello, World!"}

#to post items : curl.exe -X POST "http://127.0.0.1:8000/items?item=papaya"  
@app.post("/items")
def create_item(item :Item):
    items.append(item)
    return items

#to get items : curl.exe -X GET "http://127.0.0.1:8000/items"
@app.get("/items")
def list_items(limit : int = 5):
    return items[0 :limit]  # Return the first 'limit' items)
 
@app.get("/items", response_model=list[Item])
def list_items(limit : int = 5):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:  
    if item_id < len(items):
        return items[item_id]
    else :
        raise HTTPException(status_code=404, detail=f" Item{item_id} not found")

    # If item_id is valid, return the item
    
