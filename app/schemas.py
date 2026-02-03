from pydantic import BaseModel
from typing import Optional

class VehiculoBase(BaseModel):
    placa: str
    propietario: str
    marca: str
    fabricacion: int  
    valor_comercial: float = 0.025
    impuesto: float
    codigo_revision: str
    

class VehiculoCreate(VehiculoBase):
    pass  # <--- Ahora tiene sangría

class Vehiculo(VehiculoBase):
    # Esto es necesario para que Pydantic pueda leer modelos de SQLAlchemy
    class Config:
        from_attributes = True