from flask import Flask, render_template, request
from recommender import recommend_movies, ratings

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_id = None
    recommendations = []
    users = sorted(ratings['userId'].unique())[:100]  # show first 100 users

    if request.method == "POST":
        user_id = int(request.form["user_id"])
        recommendations = recommend_movies(user_id)

    return render_template("index.html", users=users, recommendations=recommendations, user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)
