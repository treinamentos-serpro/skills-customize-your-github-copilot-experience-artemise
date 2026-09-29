from fastapi import FastAPI

app = FastAPI(title="Simple API")

# Dados de exemplo em memória
items = [
    {"id": 1, "name": "Laptop", "price": 1500.00},
    {"id": 2, "name": "Mouse", "price": 45.50},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# TODO: add GET /items
# TODO: add GET /items/{item_id}
# TODO: add POST /items
# TODO: add PUT /items/{item_id}
