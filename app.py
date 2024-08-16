from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - Movie collection
movies = [
    {'id': 1, 'title': 'Inception', 'director': 'Christopher Nolan', 'genre': 'Sci-Fi'},
    {'id': 2, 'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'genre': 'Crime'},
    {'id': 3, 'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'genre': 'Action'}
]

# GET method to retrieve all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'movies': movies})

# GET method to retrieve a movie by ID
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)
    if movie is not None:
        return jsonify(movie)
    return jsonify({'message': 'Movie not found'}), 404

# POST method to add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = request.get_json()
    new_movie['id'] = movies[-1]['id'] + 1 if movies else 1
    movies.append(new_movie)
    return jsonify(new_movie), 201

# PUT method to update a movie by ID
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    updated_movie = request.get_json()
    for movie in movies:
        if movie['id'] == movie_id:
            movie['title'] = updated_movie.get('title', movie['title'])
            movie['director'] = updated_movie.get('director', movie['director'])
            movie['genre'] = updated_movie.get('genre', movie['genre'])
            return jsonify(movie)
    return jsonify({'message': 'Movie not found'}), 404

# DELETE method to delete a movie by ID
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [movie for movie in movies if movie['id'] != movie_id]
    return jsonify({'message': 'Movie deleted'}), 204

# GET method to filter movies by genre
@app.route('/movies/genre/<string:genre>', methods=['GET'])
def get_movies_by_genre(genre):
    filtered_movies = [movie for movie in movies if movie['genre'].lower() == genre.lower()]
    if filtered_movies:
        return jsonify({'movies': filtered_movies})
    return jsonify({'message': 'No movies found in this genre'}), 404

if __name__ == '__main__':
    app.run(debug=True)
