from fastapi import FastAPI
from routes import login, prompt, history

app = FastAPI(title="FastAPI Backend Practical Test")

app.include_router(login.router)
app.include_router(prompt.router)
app.include_router(history.router)
@app.get("/")
def root():
    return {"message": "FastAPI Backend Test is running."}



from fastapi.openapi.models import APIKey, APIKeyIn, SecuritySchemeType
from fastapi.security import APIKeyHeader
from fastapi.openapi.utils import get_openapi
from fastapi import Security

# Keep this import if you're using get_current_user from auth
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

# Add this function in your FastAPI app file
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Backend Practical Test",
        version="0.1.0",
        description="Backend app with login, prompt submission, and history",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return openapi_schema

app.openapi = custom_openapi
