import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample dataset (can be replaced with a larger, real dataset)
data = {
    'Title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Matrix', 'Pulp Fiction', 
              'Forrest Gump', 'The Shawshank Redemption', 'The Godfather', 'The Lion King', 'Toy Story'],
    'Genre': ['Sci-Fi, Action', 'Action, Crime, Drama', 'Sci-Fi, Drama', 'Action, Sci-Fi', 'Crime, Drama', 
              'Drama, Romance', 'Drama, Crime', 'Crime, Drama', 'Animation, Adventure', 'Animation, Family'],
    'Rating': [8.8, 9.0, 8.6, 8.7, 8.9, 8.8, 9.3, 9.2, 8.5, 8.3]
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Content-based filtering function using genre similarity
def content_based_recommendation(input_movie, top_n=5):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['Genre'])
    
    # Calculate cosine similarity between the input movie and all movies in the dataset
    movie_index = df[df['Title'] == input_movie].index[0]
    cosine_similarities = cosine_similarity(tfidf_matrix[movie_index], tfidf_matrix).flatten()
    
    # Get indices of top similar movies, excluding the input movie itself
    similar_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]
    
    recommended_movies = df.iloc[similar_indices][['Title', 'Genre', 'Rating']]
    return recommended_movies

# Collaborative filtering placeholder function (this can be expanded later)
def collaborative_filtering_recommendation(user_preferences, top_n=5):
    # Placeholder logic: Simply suggest highly-rated movies from the dataset
    return df.sort_values(by='Rating', ascending=False).head(top_n)

# GUI Implementation
class RecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Movie Recommendation System")
        
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        ttk.Label(self.root, text="Movie Recommendation System", font=("Helvetica", 16)).pack(pady=10)
        
        # Dropdown for selecting a movie
        ttk.Label(self.root, text="Select a Movie for Content-based Recommendations:").pack(pady=5)
        self.movie_combobox = ttk.Combobox(self.root, values=list(df['Title']), width=30)
        self.movie_combobox.pack()
        
        # Button to get recommendations
        ttk.Button(self.root, text="Get Recommendations", command=self.get_recommendations).pack(pady=10)
        
        # Display results
        self.results_text = tk.Text(self.root, height=10, width=70)
        self.results_text.pack(pady=10)
        
        # Collaborative Filtering Section
        ttk.Label(self.root, text="Get Recommendations Based on Ratings:").pack(pady=5)
        ttk.Button(self.root, text="Show Top Movies", command=self.show_top_movies).pack(pady=10)

    def get_recommendations(self):
        selected_movie = self.movie_combobox.get()
        if not selected_movie:
            messagebox.showerror("Input Error", "Please select a movie.")
            return
        
        recommendations = content_based_recommendation(selected_movie)
        
        # Clear previous results and display the new ones
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, f"Recommended Movies Similar to '{selected_movie}':\n\n")
        for i, row in recommendations.iterrows():
            self.results_text.insert(tk.END, f"- {row['Title']} (Genre: {row['Genre']}, Rating: {row['Rating']})\n")

    def show_top_movies(self):
        recommendations = collaborative_filtering_recommendation(user_preferences=None)
        
        # Clear previous results and display the new ones
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "Top Recommended Movies Based on Ratings:\n\n")
        for i, row in recommendations.iterrows():
            self.results_text.insert(tk.END, f"- {row['Title']} (Genre: {row['Genre']}, Rating: {row['Rating']})\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecommendationApp(root)
    root.mainloop()