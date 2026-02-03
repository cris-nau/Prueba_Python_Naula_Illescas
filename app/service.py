from sqlalchemy.orm import Session
from repository import VehiculoRepository
import schemas
import models  # <--- IMPORTANTE: Faltaba esta línea

class VehiculoService:
    def __init__(self, db: Session):
        self.repo = VehiculoRepository(db)

    def get_all(self):
        return self.repo.find_all()

    def create(self, vehiculo_data: schemas.VehiculoCreate):
        # Aquí usamos models.Vehiculo que ahora sí está importado
        vehiculo = models.Vehiculo(**vehiculo_data.model_dump())
        return self.repo.save(vehiculo)