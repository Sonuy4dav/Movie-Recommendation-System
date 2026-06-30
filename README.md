# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python, Machine Learning, Flask, and TMDB API**. This project recommends movies similar to a user's selected movie by analyzing movie metadata and calculating similarity scores using **Cosine Similarity**. The application also displays movie posters fetched dynamically from the TMDB API.

---

## 🚀 Features

* 🔍 Search and select movies
* 🎥 Get top 5 similar movie recommendations
* 🖼️ Display movie posters using the TMDB API
* 🌐 Interactive web application built with Flask
* 🧠 Content-based recommendation using cosine similarity
* 🎨 Responsive and user-friendly interface

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Pandas**
* **Scikit-learn**
* **HTML/CSS**
* **TMDB API**
* **Pickle**

---

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

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git

cd Movie-Recommendation-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Extract the Similarity File

Extract:

```text
similarity.zip → similarity.pkl
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. Movie metadata is preprocessed and converted into feature vectors.
2. Cosine similarity is computed between all movies.
3. The user selects a movie from the search interface.
4. The system identifies and recommends the most similar movies.
5. Movie posters are retrieved dynamically using the TMDB API.

---

## ✨ Implemented Features

* Content-based recommendation engine
* Cosine similarity matrix
* Flask backend integration
* Interactive frontend UI
* Movie poster retrieval via TMDB API
* Search and recommendation functionality

---

## 🔮 Future Enhancements

* User authentication and profiles
* Collaborative filtering recommendations
* Hybrid recommendation system
* Movie ratings and reviews
* Recommendation history
* Cloud deployment and scalability improvements

---


---

## 👨‍💻 Author

**Sonu Yadav**

* Aspiring AI/ML Engineer
* B.Tech Student
* Passionate about Artificial Intelligence, Machine Learning, and Data Science

---

⭐ If you found this project useful, consider giving it a star!

