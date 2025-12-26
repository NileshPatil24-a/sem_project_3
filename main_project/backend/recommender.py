import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

class CollegeRecommendationSystem:
    def __init__(self, data_path):
        """
        Initialize the recommendation system with college data
        """
        try:
            self.df = pd.read_csv(data_path)
        except FileNotFoundError:
            # Fallback to a sample dataset if the file is not found
            self.df = pd.DataFrame({
                'college_name': ['Sample College 1', 'Sample College 2', 'Sample College 3'],
                'course': ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering'],
                'location': ['Mumbai', 'Pune', 'Delhi'],
                'cutoff': [95.5, 92.1, 89.7],
                'fees': [200000, 180000, 150000]
            })
        
        # Preprocess the data
        self.preprocess_data()
    
    def preprocess_data(self):
        """
        Preprocess the data for better recommendations
        """
        # Fill any missing values
        self.df = self.df.fillna('')
        
        # Create a combined feature column for better matching
        if 'course' in self.df.columns and 'location' in self.df.columns:
            self.df['combined_features'] = (
                self.df['course'].astype(str) + ' ' + 
                self.df['location'].astype(str)
            ).apply(lambda x: re.sub(r'[^\w\s]', ' ', x.lower()))
    
    def get_recommendations(self, user_score, preferred_location='', preferred_course='', top_n=10):
        """
        Get college recommendations based on user score and preferences
        """
        # Filter colleges based on cutoff score (with some tolerance)
        score_filtered = self.df[self.df['cutoff'] <= user_score + 5]  # Allow 5% buffer
        
        if preferred_course:
            # Use TF-IDF and cosine similarity for course matching
            if 'combined_features' in self.df.columns:
                tfidf = TfidfVectorizer()
                tfidf_matrix = tfidf.fit_transform(score_filtered['combined_features'])
                
                # Create a query vector for the preferred course
                query_vector = tfidf.transform([re.sub(r'[^\w\s]', ' ', preferred_course.lower())])
                
                # Calculate cosine similarity
                similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
                
                # Add similarity scores to the dataframe
                score_filtered = score_filtered.copy()
                score_filtered['similarity_score'] = similarity_scores
                
                # Sort by similarity score
                score_filtered = score_filtered.sort_values('similarity_score', ascending=False)
        
        if preferred_location:
            # Filter by location if specified
            if 'location' in score_filtered.columns:
                location_filtered = score_filtered[
                    score_filtered['location'].str.contains(preferred_location, case=False, na=False)
                ]
                if not location_filtered.empty:
                    score_filtered = location_filtered
        
        # Return top N recommendations
        recommendations = score_filtered.head(top_n)
        
        result = []
        for _, row in recommendations.iterrows():
            college_info = {
                'college_name': row['college_name'],
                'course': row['course'] if 'course' in row else 'N/A',
                'location': row['location'] if 'location' in row else 'N/A',
                'cutoff': row['cutoff'],
                'fees': row['fees'] if 'fees' in row else 'N/A'
            }
            result.append(college_info)
        
        return result
    
    def get_all_colleges(self):
        """
        Get a list of all available colleges
        """
        if 'college_name' in self.df.columns:
            return self.df['college_name'].unique().tolist()
        return []
    
    def get_all_courses(self):
        """
        Get a list of all available courses
        """
        if 'course' in self.df.columns:
            return self.df['course'].unique().tolist()
        return []
    
    def get_all_locations(self):
        """
        Get a list of all available locations
        """
        if 'location' in self.df.columns:
            return self.df['location'].unique().tolist()
        return []

# Example usage
if __name__ == "__main__":
    # Initialize the recommendation system
    # Note: You'll need to specify the correct path to your data file
    recommender = CollegeRecommendationSystem("raw_Data/cuttoff AI 2025.csv")
    
    # Example recommendation
    recommendations = recommender.get_recommendations(
        user_score=90.0,
        preferred_location="Mumbai",
        preferred_course="Computer Science",
        top_n=5
    )
    
    for rec in recommendations:
        print(f"College: {rec['college_name']}, Course: {rec['course']}, Cutoff: {rec['cutoff']}")