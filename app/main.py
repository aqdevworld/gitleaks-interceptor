import os
from fastapi import FastAPI

app = FastAPI(title="GitLeaks Interceptor Baseline")


@app.get("/")
def read_root():
    return {
        "status": "Online",
        "system": "Gitleaks Interceptor Pipeline",
        "gate-status": "Active"

    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}