from fastapi import FastAPI

# 1. Define an API object
app = FastAPI()


# 3. Map HTTP method and path to python function
@app.get("/")
async def root():
    return {"Todo RESTful API"}

