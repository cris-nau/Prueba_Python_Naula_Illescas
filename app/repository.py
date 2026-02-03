from sqlalchemy.orm import Session
import models

class VehiculoRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        # Selecciona todos los registros de la tabla Vehiculo
        return self.db.query(models.Vehiculo).all()

    def save(self, vehiculo: models.Vehiculo):
        # Guarda o actualiza un vehiculo en la base de datos
        self.db.add(vehiculo)
        self.db.commit()
        self.db.refresh(vehiculo)
        return vehiculo

