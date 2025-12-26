# College Recommendation System

This is a college recommendation system that helps students find suitable colleges based on their scores and preferences.

## Project Structure

- `backend/` - Contains the Flask API and recommendation engine
- `frontend/` - Contains the React frontend application

## Backend Setup

1. Navigate to the backend directory: `cd backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Frontend Setup

1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the development server: `npm run dev`

## Features

- College recommendations based on user scores
- Location and course preferences
- Cutoff-based filtering
- Responsive web interface

## API Endpoints

- `POST /recommend` - Get college recommendations based on user preferences
- `GET /colleges` - Get list of all colleges
- `GET /health` - Health check endpoint