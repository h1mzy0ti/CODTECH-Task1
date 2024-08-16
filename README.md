# Simple Flask RESTful API

## Objective

The objective of this project is to create a simple RESTful API using Flask (Python) that allows users to manage a collection of movies. The API supports basic CRUD (Create, Read, Update, Delete) operations, as well as a filtering mechanism to retrieve movies based on their genre. This project serves as an introductory exercise in understanding how to build and manage RESTful APIs using Flask.

## Key Activities

- **Setting Up the Flask Environment**:
  - Install Flask and set up a basic Flask application.
  - Configure routing and request handling.

- **Implementing CRUD Operations**:
  - **GET**: Retrieve all movies or a specific movie by ID.
  - **POST**: Add a new movie to the collection.
  - **PUT**: Update details of an existing movie by its ID.
  - **DELETE**: Remove a movie from the collection by its ID.

- **Filtering Movies by Genre**:
  - Implement a filter to retrieve movies based on their genre.

- **Running and Testing the API**:
  - Run the Flask application on a local server.
  - Test the API endpoints using tools like Postman or cURL.

## Technology Used

- **Python**: The primary programming language used for this project.
- **Flask**: A lightweight web framework used to create the RESTful API.
- **JSON**: Data format used for communication between the client and the server.

## Project Structure

"/simple-flask-rest-api
│
├── app.py # Main application file containing the API logic
├── requirements.txt # List of required Python packages
└── README.md # Project documentation (this file)
"
##API Endpoints
- GET /movies - Retrieve all movies.
- GET /movies/<int:movie_id> - Retrieve a movie by its ID.
- POST /movies - Add a new movie (requires a JSON body).
- PUT /movies/<int:movie_id> - Update an existing movie (requires a JSON body).
- DELETE /movies/<int:movie_id> - Delete a movie by its ID.
- GET /movies/genre/<string:genre> - Retrieve movies by genre.

## Example JSON Requests

- POST /movies:
{
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "genre": "Sci-Fi"
}

- PUT /movies/2:
{
    "title": "The Godfather (Updated Edition)",
    "director": "Francis Ford Coppola",
    "genre": "Crime"
}
