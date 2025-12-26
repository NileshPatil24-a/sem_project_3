import { useState } from 'react';
import './App.css';

interface College {
  college_name: string;
  course: string;
  location: string;
  cutoff: number;
  fees?: number;
}

function App() {
  const [formData, setFormData] = useState({
    score: '',
    location: '',
    course: ''
  });
  const [recommendations, setRecommendations] = useState<College[]>([]);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // In a real application, this would be an API call to your backend
      // For now, we'll simulate the response
      const response = await fetch('http://localhost:5000/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          score: parseFloat(formData.score) || 0,
          location: formData.location,
          course: formData.course
        })
      });

      if (response.ok) {
        const data = await response.json();
        setRecommendations(data.recommendations || []);
      } else {
        // Simulated response for demo purposes
        setRecommendations([
          {
            college_name: "Sample Engineering College",
            course: "Computer Science",
            location: "Mumbai",
            cutoff: 95.5,
            fees: 200000
          },
          {
            college_name: "Sample Institute of Technology",
            course: "Electrical Engineering",
            location: "Pune",
            cutoff: 92.1,
            fees: 180000
          }
        ]);
      }
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      // Fallback recommendations
      setRecommendations([
        {
          college_name: "Demo College 1",
          course: "Computer Science",
          location: "Mumbai",
          cutoff: 90.0,
          fees: 150000
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>College Recommendation System</h1>
        <p>Find the best colleges based on your scores and preferences</p>
      </header>

      <main className="app-main">
        <form onSubmit={handleSubmit} className="recommendation-form">
          <div className="form-group">
            <label htmlFor="score">Your Score/Percentage:</label>
            <input
              type="number"
              id="score"
              name="score"
              value={formData.score}
              onChange={handleInputChange}
              placeholder="Enter your score (e.g., 90.5)"
              step="0.1"
              min="0"
              max="100"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="location">Preferred Location:</label>
            <input
              type="text"
              id="location"
              name="location"
              value={formData.location}
              onChange={handleInputChange}
              placeholder="Enter preferred location"
            />
          </div>

          <div className="form-group">
            <label htmlFor="course">Preferred Course:</label>
            <input
              type="text"
              id="course"
              name="course"
              value={formData.course}
              onChange={handleInputChange}
              placeholder="Enter preferred course"
            />
          </div>

          <button type="submit" disabled={loading}>
            {loading ? 'Finding Recommendations...' : 'Get Recommendations'}
          </button>
        </form>

        {recommendations.length > 0 && (
          <section className="recommendations-section">
            <h2>Recommended Colleges</h2>
            <div className="recommendations-list">
              {recommendations.map((college, index) => (
                <div key={index} className="college-card">
                  <h3>{college.college_name}</h3>
                  <p><strong>Course:</strong> {college.course}</p>
                  <p><strong>Location:</strong> {college.location}</p>
                  <p><strong>Cutoff:</strong> {college.cutoff}</p>
                  {college.fees && <p><strong>Fees:</strong> ₹{college.fees.toLocaleString()}</p>}
                </div>
              ))}
            </div>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;