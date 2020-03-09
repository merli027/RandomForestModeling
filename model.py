"""Models and database functions for Ted Talk project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class Speaker(db.Model):
    """Speakers."""

    __tablename__ = "speakers"

    speaker_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    speaker_name = db.Column(db.String(200), nullable=True)
    speaker_job = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""< Speaker Speaker_id= {self.speaker_id} name= {self.speaker_name} job= {self.speaker_job} >"""


class Talk(db.Model):
    """Talk information."""

    __tablename__ = "talks"

    talk_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    duration = db.Column(db.Integer)
    speakerID=db.Column(db.Integer, db.ForeignKey('speakers.speaker_id'))
    languages = db.Column(db.Integer)
    published_month= db.Column(db.Integer)
    published_day= db.Column(db.Integer)
    published_year= db.Column(db.Integer)
    event = db.Column(db.String(60))
    talk_name= db.Column(db.String(200))
    num_comments = db.Column(db.Integer)
    num_views = db.Column(db.Integer)
    speaker = db.relationship("Speaker", backref='talks')

    def __repr__(self):
        """Provide helpful representation when printed."""
        return f"""< talk_name={self.talk_name} speaker_name={self.speaker_name} >"""
 
class Rating(db.Model):
    """Rating information."""

    __tablename__ = "rating"
    rating_id = db.Column(db.Integer,
                         autoincrement=False,
                         primary_key=True)
    rating_name =db.Column(db.String(75))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return f"""< rating_name={self.rating_name} rating_id={self.rating_id} >"""

class Talk_Rating(db.Model):
    """Rating and talk relationship."""

    __tablename__ = "talk_rating"

    rating_id = db.Column(db.Integer, autoincrement=False,
                         primary_key=True)
    rating_count = db.Column(db.Integer)
    ted_talk_id = db.Column(db.Integer, autoincrement=False,
                         primary_key=True)
    db.ForeignKeyConstraint(['rating_id', 'ted_talk_id'], ['rating.rating_id', 'talks.talk_id'])    
    #talk_rel = db.relationship("Talk", backref='talk_rating')
    #rate_rel = db.relationship("Rating", backref='talk_rating')

    def __repr__(self):
        """Provide helpful representation when printed."""
        return f"""< rating_id={self.rating_id} rating_count={self.rating_count} ted_talk_id = {self.ted_talk_id} >"""
#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tedtalks'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
