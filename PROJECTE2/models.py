from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, Decimal, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

# Socios
class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)

# Hoteles
class Hotel(Base):
    __tablename__ = 'hoteles'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    ubicacion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)

    servicios = relationship("ServicioRestaurante", back_populates="restaurante")  # Nuevo
    reservas = relationship("ReservaHotel", back_populates="habitacion")
    
class Habitacion(Base):
    __tablename__ = 'habitaciones'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hoteles.id'))
    tipo = Column(String(50), nullable=True)
    disponibilidad = Column(Boolean, default=True)

    hotel = relationship("Hotel", back_populates="habitaciones")

Hotel.habitaciones = relationship("Habitacion", back_populates="hotel")


# Restaurantes
class Restaurante(Base):
    __tablename__ = 'restaurantes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    ubicacion = Column(Text, nullable=True)
    valoracion = Column(Decimal(3, 1), nullable=True)
    descripcion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)

    servicios = relationship("ServicioRestaurante", back_populates="restaurante")  # Nuevo
    reservas_restaurante = relationship("ReservaRestaurante", back_populates="restaurante")

# Pistas
class Pista(Base):
    __tablename__ = 'pistas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    tipo = Column(String(50), nullable=True)
    disponibilidad = Column(Boolean, default=True)

    reservas_pistas = relationship("ReservaPista", back_populates="pista")

# Spa
class Spa(Base):
    __tablename__ = 'spa'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=True)
    descripcion = Column(Text, nullable=True)
    disponibilidad = Column(Boolean, default=True)

    servicios = relationship("ServicioSpa", back_populates="spa")  # Nuevo
    reservas_spa = relationship("ReservaSpa", back_populates="spa")

class ServicioRestaurante(Base):
    __tablename__ = 'servicio_restaurante'

    id = Column(Integer, primary_key=True, index=True)
    restaurante_id = Column(Integer, ForeignKey('restaurantes.id'))
    tipo_menu = Column(String(50), nullable=True)
    tipo_cocina = Column(String(100), nullable=True)
    ambiente = Column(String(100), nullable=True)
    terraza = Column(Boolean, default=False)

    restaurante = relationship("Restaurante", back_populates="servicios")

Restaurante.servicios = relationship("ServicioRestaurante", back_populates="restaurante")


class ServicioSpa(Base):
    __tablename__ = 'servicio_spa'

    id = Column(Integer, primary_key=True, index=True)
    spa_id = Column(Integer, ForeignKey('spa.id'))
    tipo_servicio = Column(String(100), nullable=True)
    duracion = Column(Integer, nullable=True)

    spa = relationship("Spa", back_populates="servicios")

Spa.servicios = relationship("ServicioSpa", back_populates="spa")

# Reservas
class ReservaHotel(Base):
    __tablename__ = 'reservas_hotel'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    habitacion_id = Column(Integer, ForeignKey('habitaciones.id'))
    fecha_entrada = Column(Date, nullable=True)
    fecha_salida = Column(Date, nullable=True)

    socio = relationship("Socio", back_populates="reservas_hotel")
    habitacion = relationship("Habitacion", back_populates="reservas_hotel")

Socio.reservas_hotel = relationship("ReservaHotel", back_populates="socio")
Habitacion.reservas_hotel = relationship("ReservaHotel", back_populates="habitacion")

class ReservaPista(Base):
    __tablename__ = 'reservas_pistas'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    pista_id = Column(Integer, ForeignKey('pistas.id'))
    fecha = Column(Date, nullable=True)

    socio = relationship("Socio", back_populates="reservas_pistas")
    pista = relationship("Pista", back_populates="reservas_pistas")

Socio.reservas_pistas = relationship("ReservaPista", back_populates="socio")
Pista.reservas_pistas = relationship("ReservaPista", back_populates="pista")

class ReservaRestaurante(Base):
    __tablename__ = 'reservas_restaurante'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    restaurante_id = Column(Integer, ForeignKey('restaurantes.id'))
    fecha = Column(Date, nullable=True)
    hora = Column(Time, nullable=True)

    socio = relationship("Socio", back_populates="reservas_restaurante")
    restaurante = relationship("Restaurante", back_populates="reservas_restaurante")

Socio.reservas_restaurante = relationship("ReservaRestaurante", back_populates="socio")
Restaurante.reservas_restaurante = relationship("ReservaRestaurante", back_populates="restaurante")

class ReservaSpa(Base):
    __tablename__ = 'reservas_spa'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    spa_id = Column(Integer, ForeignKey('spa.id'))
    fecha = Column(Date, nullable=True)
    hora = Column(Time, nullable=True)

    socio = relationship("Socio", back_populates="reservas_spa")
    spa = relationship("Spa", back_populates="reservas_spa")

Socio.reservas_spa = relationship("ReservaSpa", back_populates="socio")
Spa.reservas_spa = relationship("ReservaSpa", back_populates="spa")

# Favoritos
class Favorito(Base):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey('socios.id'))
    tipo = Column(String(50), nullable=True)
    referencia_id = Column(Integer, nullable=True)
    fecha_agregado = Column(Date, nullable=True)

    socio = relationship("Socio", back_populates="favoritos")

Socio.favoritos = relationship("Favorito", back_populates="socio")
# Modelos de la tabla locales_populares

class LocalPopular(Base):
    __tablename__ = 'locales_populares'

    id = Column(Integer, primary_key=True, index=True)
    local_id = Column(Integer, nullable=False)
    popularidad = Column(Decimal(3, 2), nullable=False)  # Valor con 2 decimales

