Methodology (15/09/2025 – 27/09/2025)


🔹 Methodology Overview

The methodology focuses on collecting, preprocessing, analyzing, and recommending colleges based on student preferences. The system uses a hybrid recommendation approach combining content-based and collaborative filtering, along with a scoring mechanism to rank colleges.


🔹 Steps Involved

1.Data Collection

College details such as courses offered, location,  admission criteria are collected from official college websites, educational portals, and government databases.

Data is stored in structured formats like CSV or databases for easy processing.

Example:

College Name	Location	Courses	Admission Criteria	Reviews


2.Data Preprocessing

Handle missing or inconsistent values.

Encode categorical features like courses and locations for computational processing.

Example: Convert "Computer Science" → 1, "Mechanical Engineering" → 2 for algorithm calculations.



3.Feature Selection & Weighting

Identify key features affecting recommendations:

Student preferences: course, location.

Assign weights to features based on importance (e.g., Course Match = 0.4 adn  Location Preference = 0.1).


4.Recommendation Algorithm

Content-Based Filtering: Matches student preferences with college attributes.

Collaborative Filtering: Recommends colleges preferred by similar students.


Example:

Score = (0.4 * Course Match)  +  (0.1 * Location Preference)



5.Evaluation & Validation
 calculate the MSE and MAE
Validate recommendations with historical admission data or student feedback.


6.Deployment

Build a user-friendly interface for students to enter preferences.

Display recommended colleges along with branch-wise cut-offs.



🔹 Applications of the Methodology

For Students → Provides personalized recommendations to save time and effort.
For Parents → Offers transparency regarding nearby colleges.
For Educational Counselors → Assists in giving reliable, data-driven guidance.
For Researchers → Provides a structured dataset for studying admission patterns and trends.

👉 Example:
If a student enters MHT-CET percentile = 88, Category = OBC, Branch = IT, Location = Mumbai, the system recommends a list of colleges in Mumbai with branch-wise cut-offs.


+----------------+       +--------------------+       +--------------------+
|   Student      |  -->  | Preprocessing &    |  -->  | Feature Selection  |
|   Inputs       |       | Data Cleaning      |       | & Weight Assignment|
+----------------+       +--------------------+       +--------------------+
                                                      |
                                                      v
                                             +--------------------+
                                             | Recommendation     |
                                             | Algorithm          |
                                             +--------------------+
                                                      |
                                                      v
                                             +--------------------+
                                             | Sorting preferences |
                                             +--------------------+
                                                      |
                                                      v
                                             +--------------------+
                                             | Recommended        |
                                             | Colleges Display   |
                                             +--------------------+
