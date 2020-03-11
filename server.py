"""Ted Talks"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Talk, Speaker, Rating, Talk_Rating


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route("/talks")
def talk_list():
    """Show list of talks."""

    talks = Talk.query.all()
    
    return render_template("talk_list.html", talks=talks)

@app.route("/speakers")
def speaker_list():
    """Show list of speakers."""

    speakers = Speaker.query.all()
    return render_template("speaker_list.html", speakers=speakers)

@app.route("/talks/<int:talk_id>", methods=['GET'])
def talk_detail(talk_id):
    """Show information of ."""

    rating_list=[]
    talk=Talk.query.get(talk_id)
    for r, t in db.session.query(Rating, Talk_Rating).filter(Talk_Rating.rating_id == Rating.rating_id).filter(Talk_Rating.ted_talk_id == talk_id).all():
        rating_dict={}
        rating_name=r.rating_name
        rating_count=t.rating_count
        rating_dict['name']=rating_name
        rating_dict['count']=rating_count
        rating_list.append(rating_dict)

    return render_template("talk.html", talk=talk, rating_list=rating_list)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
