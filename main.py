from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.config import get_db
from app.models import models
from app.schemas import schemas
from app.database.config import engine
from app.mcp.recommender import get_recommended_itineraries


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Itinerary API")

@app.post("/itineraries/", response_model=schemas.Itinerary)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    db_itinerary = models.Itinerary(**itinerary.dict())
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary

@app.get("/itineraries/", response_model=List[schemas.Itinerary])
def get_itineraries(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    itineraries = db.query(models.Itinerary).offset(skip).limit(limit).all()
    return itineraries

@app.get("/itineraries/{itinerary_id}", response_model=schemas.Itinerary)
def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    itinerary = db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()
    if itinerary is None:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary

@app.get("/recommended-itineraries/", response_model=List[schemas.Itinerary])
def get_recommendations(
    duration_nights: int,
    region: str = None,
    max_price: float = None,
    db: Session = Depends(get_db)
):
    return get_recommended_itineraries(db, duration_nights, region, max_price)

@app.post("/itineraries/{itinerary_id}/days/", response_model=schemas.ItineraryDay)
def add_itinerary_day(
    itinerary_id: int,
    day: schemas.ItineraryDayCreate,
    db: Session = Depends(get_db)
):
    itinerary = db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    
    db_day = models.ItineraryDay(**day.dict())
    db.add(db_day)
    db.commit()
    db.refresh(db_day)
    return db_day

@app.post("/itinerary-days/{day_id}/activities/", response_model=schemas.ItineraryDayActivity)
def add_day_activity(
    day_id: int,
    activity: schemas.ItineraryDayActivityCreate,
    db: Session = Depends(get_db)
):
    day = db.query(models.ItineraryDay).filter(models.ItineraryDay.id == day_id).first()
    if not day:
        raise HTTPException(status_code=404, detail="Itinerary day not found")
    
    db_activity = models.ItineraryDayActivity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity 