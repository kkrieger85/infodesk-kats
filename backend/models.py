from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)  # "Polygon", "Marker", "Circle"
    data = Column(String)  # JSON
    created_at = Column(DateTime, default=datetime.utcnow)