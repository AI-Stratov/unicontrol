from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import src.routers as routers
from src.database import Database

app = FastAPI()


db = Database()
db.connect()


@app.on_event("startup")
def startup_event():
    db.execute_script("src/sql_scripts/create_tables.sql")
    if not db.check_data_exists("faculty", "id", 1):
        db.execute_script("src/sql_scripts/insert_data.sql")


@app.on_event("shutdown")
def shutdown_event():
    db.disconnect()


@app.get("/", include_in_schema=False)
def root():
    """Redirects to the docs page."""
    return RedirectResponse(url="/docs")


app.include_router(routers.router)
