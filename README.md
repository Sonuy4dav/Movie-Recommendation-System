# Movie-Recommendation-System

A content-based Movie Recommendation System built using **Python, Machine Learning, Flask, and TMDB API**. This application recommends similar movies based on movie metadata and displays movie posters through the TMDB API.

## 🚀 Features

* Search and select movies
* Get top 5 similar movie recommendations
* Display movie posters using TMDB API
* Interactive web interface built with Flask
* Content-based filtering using cosine similarity

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* Scikit-learn
* HTML/CSS
* TMDB API
* Pickle

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movie_list.pkl
├── similarity.zip
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── README.md
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Extract the similarity file

Extract:

```text
similarity.zip → similarity.pkl
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🧠 How It Works

1. Movie metadata is processed and converted into feature vectors.
2. Cosine similarity is calculated between all movies.
3. When a user selects a movie, the system finds the most similar movies.
4. Movie posters are fetched dynamically using the TMDB API.

## ✨ Features Implemented

* Content-based recommendation engine
* Similarity matrix using cosine similarity
* Flask backend
* Responsive frontend
* Movie poster integration
* Search functionality

## 🔮 Future Improvements

* User authentication
* Collaborative filtering
* Hybrid recommendation system
* Movie ratings and reviews
* Recommendation history
* Deployment on cloud platforms

## ⭐ If you found this project useful, consider giving it a star!
