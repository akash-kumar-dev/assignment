from app.database.config import SessionLocal
from app.models.models import Location, Hotel, Activity, Itinerary, ItineraryDay, ItineraryDayActivity, Transfer, TransportationType

def seed_database():
    db = SessionLocal()

    # Create locations
    phuket = Location(
        name="Phuket",
        region="Phuket",
        description="Thailand's largest island with beautiful beaches",
        latitude=7.8804,
        longitude=98.3923
    )
    
    patong = Location(
        name="Patong",
        region="Phuket",
        description="Famous beach resort town in Phuket",
        latitude=7.8965,
        longitude=98.2935
    )

    krabi = Location(
        name="Krabi Town",
        region="Krabi",
        description="Gateway to Krabi's beautiful islands and beaches",
        latitude=8.0863,
        longitude=98.9063
    )

    ao_nang = Location(
        name="Ao Nang",
        region="Krabi",
        description="Popular beach destination in Krabi",
        latitude=8.0419,
        longitude=98.8185
    )

    db.add_all([phuket, patong, krabi, ao_nang])
    db.commit()

    # Create hotels
    hotels = [
        Hotel(
            name="Phuket Marriott Resort",
            location_id=phuket.id,
            rating=5,
            description="Luxury beachfront resort",
            price_per_night=250.0
        ),
        Hotel(
            name="Patong Beach Hotel",
            location_id=patong.id,
            rating=4,
            description="Central hotel near nightlife",
            price_per_night=150.0
        ),
        Hotel(
            name="Krabi Resort",
            location_id=krabi.id,
            rating=4,
            description="Comfortable resort with pool",
            price_per_night=180.0
        ),
        Hotel(
            name="Ao Nang Cliff Beach Resort",
            location_id=ao_nang.id,
            rating=4,
            description="Resort with stunning views",
            price_per_night=200.0
        )
    ]
    db.add_all(hotels)
    db.commit()

    # Create activities
    activities = [
        Activity(
            name="Phi Phi Islands Tour",
            location_id=phuket.id,
            duration_hours=8.0,
            description="Full-day tour of the famous Phi Phi Islands",
            price=100.0
        ),
        Activity(
            name="Old Town Walking Tour",
            location_id=phuket.id,
            duration_hours=3.0,
            description="Explore Phuket's historic old town",
            price=30.0
        ),
        Activity(
            name="Four Islands Tour",
            location_id=krabi.id,
            duration_hours=7.0,
            description="Visit four beautiful islands by boat",
            price=80.0
        ),
        Activity(
            name="Tiger Cave Temple",
            location_id=krabi.id,
            duration_hours=4.0,
            description="Visit the famous temple with 1237 steps",
            price=40.0
        )
    ]
    db.add_all(activities)
    db.commit()

    # Create sample itineraries
    itinerary = Itinerary(
        name="Phuket & Krabi Adventure",
        duration_nights=4,
        total_price=1200.0,
        is_recommended=True
    )
    db.add(itinerary)
    db.commit()

    # Create itinerary days
    days = [
        ItineraryDay(
            itinerary_id=itinerary.id,
            day_number=1,
            hotel_id=hotels[0].id
        ),
        ItineraryDay(
            itinerary_id=itinerary.id,
            day_number=2,
            hotel_id=hotels[0].id
        ),
        ItineraryDay(
            itinerary_id=itinerary.id,
            day_number=3,
            hotel_id=hotels[2].id
        ),
        ItineraryDay(
            itinerary_id=itinerary.id,
            day_number=4,
            hotel_id=hotels[2].id
        )
    ]
    db.add_all(days)
    db.commit()

    # Add activities to days
    day_activities = [
        ItineraryDayActivity(
            itinerary_day_id=days[0].id,
            activity_id=activities[0].id,
            start_time="09:00"
        ),
        ItineraryDayActivity(
            itinerary_day_id=days[1].id,
            activity_id=activities[1].id,
            start_time="14:00"
        ),
        ItineraryDayActivity(
            itinerary_day_id=days[2].id,
            activity_id=activities[2].id,
            start_time="09:00"
        ),
        ItineraryDayActivity(
            itinerary_day_id=days[3].id,
            activity_id=activities[3].id,
            start_time="10:00"
        )
    ]
    db.add_all(day_activities)
    db.commit()

    # Add transfers
    transfers = [
        Transfer(
            itinerary_day_id=days[2].id,
            from_location_id=phuket.id,
            to_location_id=krabi.id,
            transportation_type=TransportationType.BUS,
            duration_hours=3.0,
            price=20.0
        )
    ]
    db.add_all(transfers)
    db.commit()

if __name__ == "__main__":
    seed_database() 