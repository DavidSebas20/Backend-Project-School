from fastapi import FastAPI
from database import engine, Base
from routers import events, locations, contacts

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir routers
app.include_router(events.router, prefix="/api", tags=["events"])
app.include_router(locations.router, prefix="/api", tags=["locations"])
app.include_router(contacts.router, prefix="/api", tags=["contacts"])
