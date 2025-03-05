from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="SEO Keyword Finder API")

# Include API routes
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to the SEO Keyword Finder API"}
