# Travel Itinerary Management System

A backend system for managing travel itineraries with FastAPI and SQLAlchemy.

## Features

- Database architecture for trip itineraries using SQLAlchemy
- RESTful API endpoints for creating and viewing itineraries
- MCP server that provides recommended itineraries based on duration
- Sample data for Phuket and Krabi regions in Thailand

## Requirements

- Python 3.8+
- PostgreSQL

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a PostgreSQL database named `travel_itinerary`

4. Update the database URL in `app/database/config.py` if needed

5. Run the database seeder:
```bash
python main.py # for creating the database tables)
python -m app.utils.seed_data
```

6. Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative documentation: `http://localhost:8000/redoc`

### Available Endpoints

#### 1. Create New Itinerary
```
POST /itineraries/
Request body:
{
  "name": "Weekend in Phuket",
  "duration_nights": 2,
  "total_price": 500.0,
  "is_recommended": true
}
```

#### 2. List All Itineraries
```
GET /itineraries/
```

#### 3. Get Specific Itinerary
```
GET /itineraries/{itinerary_id}
Path parameters:
- itinerary_id: ID of the itinerary to retrieve
```

#### 4. Get Recommended Itineraries
```
GET /recommended-itineraries/
Query parameters:
- duration_nights (required): Number of nights
- region (optional): Filter by region (e.g., "Phuket", "Krabi")
- max_price (optional): Maximum price filter
```

#### 5. Add Day to Itinerary
```
POST /itineraries/{itinerary_id}/days/
Request body:
{
  "day_number": 1,
  "hotel_id": 1,
  "itinerary_id": 1
}
```

#### 6. Add Activity to Itinerary Day
```
POST /itinerary-days/{day_id}/activities/
Request body:
{
  "start_time": "09:00",
  "activity_id": 1,
  "itinerary_day_id": 1
}
```

### Example Usage

1. Create a new itinerary:
```bash
curl -X POST "http://localhost:8000/itineraries/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Weekend in Phuket",
    "duration_nights": 2,
    "total_price": 500.0,
    "is_recommended": true
  }'
```

2. Get recommended itineraries for 4 nights in Phuket:
```bash
curl "http://localhost:8000/recommended-itineraries?duration_nights=4&region=Phuket&max_price=2000"
```

## Database Schema

The system uses the following main entities:

- Location: Stores information about destinations
- Hotel: Accommodation options in each location
- Activity: Available activities/excursions
- Itinerary: Main trip plan
- ItineraryDay: Day-wise breakdown of the itinerary
- Transfer: Transportation between locations
- ItineraryDayActivity: Activities scheduled for each day

## Sample Data

The seeder provides sample data for:
- Locations in Phuket and Krabi
- Hotels in different price ranges
- Popular activities and tours
- Sample 4-day itinerary

## MCP (Master Control Program)

The MCP server component provides recommended itineraries based on:
- Duration (number of nights)
- Optional region filter
- Optional maximum price filter 