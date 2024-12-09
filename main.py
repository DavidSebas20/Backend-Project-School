from fastapi import FastAPI
from database import engine, Base
from routers import events, locations, contacts
from fastapi.middleware.cors import CORSMiddleware

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Permite solicitudes desde cualquier origen (reemplaza con el dominio de tu frontend en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a URLs específicas como ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todas las cabeceras
)

# Incluir routers
app.include_router(events.router, prefix="/api", tags=["events"])
app.include_router(locations.router, prefix="/api", tags=["locations"])
app.include_router(contacts.router, prefix="/api", tags=["contacts"])
