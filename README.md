# python-project

## Movie Recommendation System

A content-based movie recommender system built with Python that suggests similar movies based on your input using genres, keywords, and overviews.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Complete-brightgreen)

---

## Features

* Recommend top 5 similar movies based on input title
* Uses TF-IDF vectorization and cosine similarity
* Clean and interactive command-line interface
* Expandable to GUI or web interface (Flask/Streamlit)

---

## Dataset

A custom dataset (`movies.csv`) is used containing:

* `title`: Movie title
* `genres`: Genre tags
* `keywords`: Key themes or elements
* `overview`: Summary of the movie plot

> A sample dataset with 10 movies is included. You can expand it with TMDB or Kaggle datasets.

---

## Installation

### 1. Clone the repository:

```
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies:

```
pip install -r requirements.txt
```

### 3. Run the app:

```
python main.py
```

---

## File Structure

```
movie-recommender/
├── movies.csv            # Movie dataset
├── recommender.py        # Core logic for recommendation
├── main.py               # Command-line interface
└── requirements.txt      # Dependencies
```

---

## How It Works

1. Combines genres, keywords, and overview into a single text feature.
2. Uses `TfidfVectorizer` to convert text to vectors.
3. Calculates cosine similarity between all movie vectors.
4. Recommends top 5 most similar movies to the input title.

---

## Sample Usage

```
Welcome to the Movie Recommender System

Enter a movie title (or 'exit' to quit): Inception

Recommended Movies:
  - Interstellar
  - The Matrix
  - The Dark Knight
  - The Avengers
  - Avatar
```

---

## Example Technologies

* Python 3
* pandas
* scikit-learn
* TfidfVectorizer
* Cosine Similarity

---

## Future Enhancements

*  Web App using Flask or Streamlit
*  Collaborative filtering (Surprise or Deep Learning)
*  Movie poster integration using TMDB API
*  User login and favorites saving

---

##  License

This project is for educational and demonstration purposes.

---

##  Contribution

Contributions are welcome! Please fork the repo and submit a pull request. For major changes, open an issue first.

---

##  Connect

If you found this project helpful, give it a STAR and share!

> Created with ❤️ by Muhammad Rakib (https://github.com/rakibul5656)

