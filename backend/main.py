from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Location
from schemas import LocationData, AddLocationData
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewsData(BaseModel):
    title: str
    content: str
    location_id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/locations/")
def create_location(location_data: AddLocationData, db: Session = Depends(get_db)):
    location = Location(type=location_data.type, data=location_data.data)
    db.add(location)
    db.commit()
    db.refresh(location)
    return location

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")


@app.get("/locations/", response_model=List[LocationData])
def get_locations(db: Session = Depends(get_db)) -> list[LocationData]:
    locations = db.query(Location).all()
    return locations


@app.put("/locations/{location_id}", response_model=LocationData)
def update_location(location_id: int, location_data: AddLocationData, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    location.type = location_data.type or location.type
    location.data = location_data.data or location.data

    db.commit()
    db.refresh(location)

    return location


@app.delete("/locations/{location_id}", response_model=LocationData)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    db.delete(location)
    db.commit()

    return None