from flask import render_template
from WebHostLib import app, cache
from .models import *
from datetime import timedelta

@app.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=300)  # cache has to appear under app route for caching to work
def landing():
    rooms = count(room for room in Room if room.creation_time >= datetime.utcnow() - timedelta(days=7))
    seeds = count(seed for seed in Seed if seed.creation_time >= datetime.utcnow() - timedelta(days=7))
    return render_template("landing.html", rooms=rooms, seeds=seeds)
