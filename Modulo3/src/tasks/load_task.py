import asyncio
import sqlite3
from prefect import task
from sqlalchemy import (create_engine, Column, Integer,
                        String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

# La clase representa la tabla en la bbdd
class Oferta(Base):
   # Aqui ponemos como queremos que se llame la tabla
   __tablename__ = "Ofertas"

   # Y aqui configuramos los campos
   id = Column(Integer, primary_key=True)
   puesto = Column(String)
   ubicacion = Column(String)
   url = Column(String)
   fecha = Column(Date)


@task(name="CARGANDO LA DATA EN LA BBDD")
async def load_task(ofertas):
   engine = create_engine("sqlite:///ofertas.db", echo=True)
   Base.metadata.create_all(bind=engine)
   Session = sessionmaker(bind=engine)
   session = Session()

   try:
      for oferta in ofertas:
         nueva_oferta = Oferta(
            puesto=oferta["peusto"],
            ubicacion=oferta["ubicacion"],
            url=oferta["url"],
            fecha=datetime.strptime(oferta["fecha"], "%Y-%m-%d").date()
         )
         session.add(nueva_oferta)

      session.commit()
      session.close()
   
   except Exception as e:
      print(f"Error bbdd: {e}")