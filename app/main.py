from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import dicom

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DICOM Metadata API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(dicom.router, tags=["DICOM"])
