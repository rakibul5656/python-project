from recommender import load_data, create_similarity_matrix, get_recommendations

def main():
    print("Welcome to the Movie Recommender System")
    df = load_data()
    cosine_sim = create_similarity_matrix(df)

    while True:
        title = input("\nEnter a movie title (or 'exit' to quit): ").strip()
        title = title.title()
        if title.lower() == 'exit':
            break

        recommendations = get_recommendations(title, df, cosine_sim)
        print("\nRecommended Movies:")
        for movie in recommendations:
            print(f"  - {movie}")

if __name__ == "__main__":
    main()
