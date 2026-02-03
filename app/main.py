from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import db
import service

# Create database tables
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title="Vehiculo CRUD FastAPI")

# Dependency to get Service
def get_vehiculo_service(db: Session = Depends(db.get_db)):
    return service.VehiculoService(db)

@app.get("/api/vehiculos", response_model=List[schemas.Vehiculo])
def read_vehiculos(service: service.VehiculoService = Depends(get_vehiculo_service)):
    return service.get_all()

@app.post("/api/vehiculos", response_model=schemas.Vehiculo, status_code=status.HTTP_201_CREATED)
def create_vehiculo(vehiculo: schemas.VehiculoCreate, service: service.VehiculoService = Depends(get_vehiculo_service)):
    try:
        return service.create(vehiculo)
    except Exception as e:
        # Simplistic error handling for uniqueness constraints etc.
        raise HTTPException(status_code=403, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)