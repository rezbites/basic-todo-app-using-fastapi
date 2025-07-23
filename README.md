# 📝 FastAPI To-Do App

This is a **basic FastAPI To-Do list project** built as part of my learning journey with the FastAPI web framework. The purpose of this project is **solely educational** — to understand how FastAPI works, how to build APIs with it, and to build a strong foundation for future backend projects.

## 🚀 Project Goals

- 🧠 **Learn** FastAPI — routing, request handling, Pydantic models, and more  
- 🏗️ **Build** a simple to-do app that stores in-memory task items  
- 🧪 Explore how to use tools like **curl**, **interactive docs**, and **HTTP methods**  

## 💡 What This Project Includes

- `POST /items`: Add new to-do items  
- `GET /items`: View a limited list of added items  
- `GET /items/{item_id}`: View a specific item by ID  
- Data is stored in a simple Python list (`items[]`)  
- FastAPI handles data validation using **Pydantic** models  

## 📦 Tech Stack Used

- 🐍 Python 3.11+  
- ⚡ [FastAPI](https://fastapi.tiangolo.com/)  
- 🧪 [curl](https://curl.se/) (for testing HTTP requests)  
- 🔍 Auto-generated API docs via Swagger (at `/docs`)

## 🛠️ How to Run

### 1. Install dependencies
pip install fastapi uvicorn

### 2. Run the server
uvicorn app:app --reload


> Replace `app` with your filename (without `.py`)

### 3. Test with curl (Windows PowerShell)
curl.exe --% -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d "{"text": "Task 1"}"


Or go to:
http://127.0.0.1:8000/docs


To test using the interactive Swagger UI.

## 🔍 Sample Request & Response

**POST /items**
{
"text": "Buy groceries",
"is_done": false
}
You get back an updated list of items like:
[
{
"text": "Buy groceries",
"is_done": false
}
]

## 📚 What I Learned

- How to define **routes** in FastAPI
- How to use **Pydantic models** for request validation
- How to send HTTP requests with `curl`
- Understanding **GET**, **POST**, and **path parameters**
- Creating simple APIs and interacting with them via Swagger UI or terminal

## 📌 Notes

- This project **does not use a database** — all items are stored in memory and will reset when the app restarts.
- This is not a full production-ready app; it’s made for learning purposes only.

## 🌱 Next Steps (Future Projects)

- Add file-based or database storage (e.g., SQLite)
- Add `PUT` and `DELETE` endpoints
- Add user authentication with JWT
- Connect to a frontend using React or HTMX

## ✅ Conclusion

This project helped me get hands-on experience with one of Python’s most powerful web frameworks — **FastAPI**. While minimal, it gave me the confidence to understand how APIs work and build better backend systems going forward.

