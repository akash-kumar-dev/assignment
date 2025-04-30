from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from app.models.models import TransportationType

class LocationBase(BaseModel):
    name: str
    region: str
    description: str
    latitude: float
    longitude: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        from_attributes = True

class HotelBase(BaseModel):
    name: str
    rating: int
    description: str
    price_per_night: float

class HotelCreate(HotelBase):
    location_id: int

class Hotel(HotelBase):
    id: int
    location: Location

    class Config:
        from_attributes = True

class ActivityBase(BaseModel):
    name: str
    duration_hours: float
    description: str
    price: float

class ActivityCreate(ActivityBase):
    location_id: int

class Activity(ActivityBase):
    id: int
    location: Location

    class Config:
        from_attributes = True

class TransferBase(BaseModel):
    transportation_type: TransportationType
    duration_hours: float
    price: float

class TransferCreate(TransferBase):
    from_location_id: int
    to_location_id: int
    itinerary_day_id: int

class Transfer(TransferBase):
    id: int
    from_location: Location
    to_location: Location

    class Config:
        from_attributes = True

class ItineraryDayActivityBase(BaseModel):
    start_time: str

class ItineraryDayActivityCreate(ItineraryDayActivityBase):
    activity_id: int
    itinerary_day_id: int

class ItineraryDayActivity(ItineraryDayActivityBase):
    id: int
    activity: Activity

    class Config:
        from_attributes = True

class ItineraryDayBase(BaseModel):
    day_number: int

class ItineraryDayCreate(ItineraryDayBase):
    hotel_id: int
    itinerary_id: int

class ItineraryDay(ItineraryDayBase):
    id: int
    hotel: Hotel
    activities: List[ItineraryDayActivity]
    transfers: List[Transfer]

    class Config:
        from_attributes = True

class ItineraryBase(BaseModel):
    name: str
    duration_nights: int
    total_price: float
    is_recommended: bool = False

class ItineraryCreate(ItineraryBase):
    pass

class Itinerary(ItineraryBase):
    id: int
    days: List[ItineraryDay]

    class Config:
        from_attributes = True

class ItineraryFilter(BaseModel):
    duration_nights: Optional[int] = None
    max_price: Optional[float] = None
    region: Optional[str] = None
