from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id      = Column(Integer, primary_key=True)
    name    = Column(String(250), nullable=False)
    email   = Column(String(250), nullable=False)
    picture = Column(String(250))

class Building(Base):
    __tablename__ = 'building'

    id      = Column(Integer, primary_key=True)
    name    = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user    = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'  : self.name,
            'id'    : self.id,
        }

class BuildingInfo(Base):
    __tablename__ = 'building_info'

    name                = Column(String(80), nullable=False)
    id                  = Column(Integer, primary_key=True)
    description         = Column(String(1000))
    year_completed      = Column(String(8))
    architect           = Column(String(250))
    continent           = Column(String(50))
    country             = Column(String(250))
    style               = Column(String(250))
    height              = Column(Integer)
    floors              = Column(Integer)
    tallest_world       = Column(Boolean, default=False)
    tallest_continent   = Column(Boolean, default=False)
    tallest_country     = Column(Boolean, default=False)
    building_id         = Column(Integer, ForeignKey('building.id'))
    building            = relationship(Building)
    user_id             = Column(Integer, ForeignKey('user.id'))
    user                = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'              : self.name,
            'description'       : self.description,
            'id'                : self.id,
            'year_completed'    : self.year_completed,
            'architect'         : self.architect,
            'continent'         : self.continent,
            'country'           : self.country,
            'style'             : self.style,
            'height'            : style.height,
            'floors'            : self.floors,
            'tallest_world'     : self.tallest_world,
            'tallest_continent' : self.tallest_continent,
            'tallest_country'   : self.tallest_country,
        }
engine = create_engine('sqlite:///buildinginfo1.db')


Base.metadata.create_all(engine)
