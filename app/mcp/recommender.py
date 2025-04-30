from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.models import Itinerary, ItineraryDay, Hotel, Location
from typing import List, Optional

def get_recommended_itineraries(
    db: Session,
    duration_nights: int,
    region: Optional[str] = None,
    max_price: Optional[float] = None
) -> List[Itinerary]:
    """
    Get recommended itineraries based on duration and optional filters.
    
    Args:
        db: Database session
        duration_nights: Number of nights for the itinerary
        region: Optional region filter
        max_price: Optional maximum price filter
    
    Returns:
        List of recommended itineraries
    """
    query = db.query(Itinerary).filter(
        and_(
            Itinerary.duration_nights == duration_nights,
            Itinerary.is_recommended == True
        )
    )

    # optional filters
    if region:
        query = (query
                .join(Itinerary.days)
                .join(ItineraryDay.hotel)
                .join(Hotel.location)
                .filter(Location.region == region)
                .distinct())

    if max_price:
        query = query.filter(Itinerary.total_price <= max_price)

    query = query.order_by(Itinerary.total_price)

    return query.all()