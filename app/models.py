from db import Base
from sqlalchemy import Column, String, Integer, Float

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True) 
    placa = Column(String, unique=True, index=True)
    propietario = Column(String)
    marca = Column(String)
    fabricacion = Column(Integer)
    valor_comercial = Column(Float)
    impuesto = Column(Float)
    codigo_revision = Column(String)