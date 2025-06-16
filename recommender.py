import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
def load_data(filepath='movies.csv'):
    df = pd.read_csv(filepath)
    df['combined'] = df['genres'].fillna('') + ' ' + df['keywords'].fillna('') + ' ' + df['overview'].fillna('')
    return df


# Create similarity matrix
def create_similarity_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


# Get recommendations
def get_recommendations(title, df, cosine_sim):
    if title not in df['title'].values:
        return [f"❌ '{title}' not found in database."]

    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()
