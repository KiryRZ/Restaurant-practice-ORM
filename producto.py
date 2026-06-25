from sqlalchemy import Column, String, Integer, Float, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

Base = declarative_base()
load_dotenv()


class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=True)

    def __repr__(self):
        print(
            f"Producto: id={self.id}, nombre={self.nombre}, tipo={self.tipo}, precio = {self.precio}, disponibilidad{self.disponible}"
        )


# Configuracion inicial de la base de datos
DATABASE_HOST = os.getenv("DB_HOST")
DATABASE_USER = os.getenv("DB_USER")
DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
