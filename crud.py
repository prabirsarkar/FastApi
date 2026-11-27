from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id":1,
        "title":"C Programming language"
    },
    {
        "id":2,
        "title":"Python"
    }
]

@app.get("/book")
def get_book();
    return books