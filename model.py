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

        return f"<Speaker Speaker_id={self.speaker_id} name={self.speaker_name} job={self.speaker_job}>"


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
        return f"""<Talk talk_id={self.talk_id} duration={self.duration} languages={self.languages} 
                    published_date={self.published_date} event={self.event} talk_name={self.talk_name}
                    speaker_name={self.speaker_name} speaker_job = {self.speaker_job} num_comments={self.num_comments}
                    num_views={self.num_views}>"""

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
