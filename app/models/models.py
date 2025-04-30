from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Enum, Boolean
from sqlalchemy.orm import relationship
from app.database.config import Base
import enum

class TransportationType(enum.Enum):
    CAR = "car"
    BUS = "bus"
    BOAT = "boat"
    FLIGHT = "flight"

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    rating = Column(Integer)
    description = Column(String)
    price_per_night = Column(Float)

    location = relationship("Location")

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    duration_hours = Column(Float)
    description = Column(String)
    price = Column(Float)

    location = relationship("Location")

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    duration_nights = Column(Integer)
    total_price = Column(Float)
    is_recommended = Column(Boolean, default=False)

class ItineraryDay(Base):
    __tablename__ = "itinerary_days"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    day_number = Column(Integer)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    itinerary = relationship("Itinerary", back_populates="days")
    hotel = relationship("Hotel")
    activities = relationship("ItineraryDayActivity")
    transfers = relationship("Transfer")

class ItineraryDayActivity(Base):
    __tablename__ = "itinerary_day_activities"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    start_time = Column(String)  # Format: "HH:MM"

    activity = relationship("Activity")

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    from_location_id = Column(Integer, ForeignKey("locations.id"))
    to_location_id = Column(Integer, ForeignKey("locations.id"))
    transportation_type = Column(Enum(TransportationType))
    duration_hours = Column(Float)
    price = Column(Float)

    from_location = relationship("Location", foreign_keys=[from_location_id])
    to_location = relationship("Location", foreign_keys=[to_location_id])

Itinerary.days = relationship("ItineraryDay", back_populates="itinerary") 