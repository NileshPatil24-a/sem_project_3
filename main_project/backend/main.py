from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# Load the dataset
try:
    df = pd.read_csv('raw_Data/cuttoff AI 2025.csv')  # Using one of the data files
except:
    # If the specific file doesn't exist, try another one
    try:
        df = pd.read_csv('raw_Data/2024ENGG_CAP1_AI_CutOff.csv')
    except:
        # Create a minimal dataframe as fallback
        df = pd.DataFrame({
            'college_name': ['Sample College 1', 'Sample College 2'],
            'course': ['Computer Science', 'Electrical Engineering'],
            'cutoff': [95.5, 92.1]
        })

def preprocess_text(text):
    """Preprocess text for matching"""
    if pd.isna(text):
        return ""
    return re.sub(r'[^\w\s]', ' ', str(text).lower())

@app.route('/recommend', methods=['POST'])
def recommend_colleges():
    try:
        data = request.json
        user_score = data.get('score', 0)
        preferred_location = data.get('location', '').lower()
        preferred_course = data.get('course', '').lower()
        
        # Filter colleges based on user score (with some tolerance)
        filtered_df = df[df['cutoff'] <= user_score + 5]  # Allow some buffer
        
        # Calculate similarity scores if course/location filtering is needed
        if preferred_course:
            df['course_similarity'] = df['course'].apply(
                lambda x: cosine_similarity(
                    TfidfVectorizer().fit_transform([preprocess_text(preferred_course), preprocess_text(x)]
                ).reshape(1, -1)[0][1] if not pd.isna(x) else 0
            )
            filtered_df = filtered_df.nlargest(10, 'course_similarity')
        
        if preferred_location:
            if 'location' in df.columns:
                df['location_similarity'] = df['location'].apply(
                    lambda x: 1 if preferred_location in preprocess_text(x) else 0
                )
                filtered_df = filtered_df[filtered_df['location_similarity'] > 0.5]
        
        # Return top recommendations
        recommendations = filtered_df.head(10)[['college_name', 'course', 'cutoff']].to_dict('records')
        
        return jsonify({
            'success': True,
            'recommendations': recommendations
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/colleges', methods=['GET'])
def get_colleges():
    """Get list of all colleges"""
    try:
        colleges = df['college_name'].unique().tolist() if 'college_name' in df.columns else []
        return jsonify({
            'colleges': colleges
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)