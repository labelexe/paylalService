import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import users, payment_methods
from app.database import engine, Base

app = FastAPI(debug=True, title="PaylalService")

# Load env
load_dotenv()


@app.on_event("startup")
async def startup():
    try:
        # DB Connect
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print("Panic startup, err:", e)


@app.middleware("http")
async def recover_from_error(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        error_message = {"detail": "An error occurred"}
        return JSONResponse(status_code=500, content=error_message)


# Routes
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(payment_methods.router, prefix="/payment_methods", tags=["payment_methods"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8053)
