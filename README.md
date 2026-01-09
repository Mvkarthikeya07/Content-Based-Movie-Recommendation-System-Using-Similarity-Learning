🎬 Content-Based Movie Recommendation System Using Similarity Learning

A Content-Based Movie Recommendation Web Application

📌 Overview

The Movie Recommendation System is a machine learning–powered web application that provides personalized movie recommendations based on content similarity. The system analyzes movie metadata and user rating information to suggest movies that are most relevant to a given input title.

This project demonstrates the practical application of recommender system concepts, data processing, and web-based deployment using a clean and modular Flask architecture.

🎯 Objectives

Build a content-based movie recommendation engine

Analyze movie metadata and rating data

Apply similarity-based recommendation techniques

Deploy the recommendation logic via a web interface

Maintain a modular, reproducible, and scalable project structure

🚀 Key Features

✔ Content-based movie recommendations
✔ Real-time recommendation generation
✔ Clean and simple user interface
✔ Efficient similarity computation
✔ Modular recommendation logic
✔ Lightweight and fast inference

🧠 Recommendation Approach

The system follows a Content-Based Filtering strategy.

Methodology

Dataset

Movie metadata (movies.csv)

User ratings (ratings.csv)

Feature Engineering

Movie attributes are processed to construct feature vectors

Similarity Computation

Similarity between movies is calculated using mathematical distance metrics

Recommendation Generation

The most similar movies are returned as recommendations

This approach ensures recommendations are interpretable, efficient, and scalable.

🏗️ Project Structure
movie_recommendation_system/
│
├── __pycache__/
│
├── data/
│   ├── movies.csv                  # Movie metadata
│   └── ratings.csv                 # User ratings
│
├── templates/
│   └── index.html                  # Web interface
│
├── app.py                          # Flask application entry point
├── recommender.py                  # Recommendation logic
│
├── requirements.txt                # Python dependencies
├── LICENSE
└── README.md                       # Project documentation

🔄 Application Workflow

User enters a movie title

Flask backend receives the request

Recommendation engine computes similarity scores

Recommended movies are displayed instantly

🖥️ Application Screenshots
Movie Search Interface

<img width="1366" height="653" alt="Screenshot (73)" src="https://github.com/user-attachments/assets/a221f64e-ec2d-40f6-a46f-452dce3d6610" />

Allows users to enter a movie title to get recommendations.

Recommendation Results

<img width="1366" height="649" alt="Screenshot (74)" src="https://github.com/user-attachments/assets/24e6d652-b715-4e47-a3b7-62d175f3440d" />

Displays a list of movies recommended based on similarity.

⚙️ Installation & Usage
1️⃣ Clone the Repository
git clone <your-repository-url>
cd movie_recommendation_system

2️⃣ Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Access the Web App
http://127.0.0.1:5000

🧪 Technologies Used

Python

Flask

Pandas

NumPy

Scikit-learn

HTML & CSS

🔬 Technical Highlights

Modular recommendation logic

Efficient similarity calculations

Clean separation of backend and frontend

Scalable structure for advanced recommender techniques

Practical implementation of recommendation system concepts

🔮 Future Enhancements

Collaborative filtering implementation

Hybrid recommendation models

User-based personalization

Recommendation evaluation metrics

REST API support

👤 Author

M V Karthikeya
Computer Science Engineer
Interests: Machine Learning, Recommender Systems, Data Science

GitHub: https://github.com/Mvkarthikeya07

📜 License

This project is licensed under the MIT License.

⭐ Final Remarks

This project demonstrates a well-structured recommendation system, combining machine learning techniques with web application deployment, suitable for academic, professional, and portfolio use.
