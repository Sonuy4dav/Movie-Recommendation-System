from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "Your_tmdb_api_key"


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        data = requests.get(url).json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']

        return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']

        recommendations.append({
            "title": movies.iloc[i[0]]['title'],
            "poster": fetch_poster(movie_id)
        })

    return recommendations


@app.route('/')
def home():
    return render_template(
        'index.html',
        movies=movies['title'].values
    )


@app.route('/recommend', methods=['GET', 'POST'])
def recommend_movie():

    if request.method == 'GET':
        return render_template(
            'index.html',
            movies=movies['title'].values
        )

    selected_movie = request.form.get('movie')

    recommendations = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=movies['title'].values,
        selected_movie=selected_movie,
        recommendations=recommendations
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)