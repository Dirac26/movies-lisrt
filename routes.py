from app import app, db
from forms import MovieForm
from models import MovieTable
from flask import request, render_template, flash, redirect, url_for

@app.route('/', methods=["GET", "POST"])
def index():
    movie = MovieForm()
    if movie.validate_on_submit():
        new_movie = MovieTable(title=movie.name.data, rating=int(movie.rating.data))
        db.session.add(new_movie)
        db.session.commit()
    return render_template("index.html", movie_form=movie)