"""Utility file to seed ted talk data into tables"""

import datetime
from sqlalchemy import func
import pandas as pd
from model import Talk, connect_to_db, db
from flask import Flask, render_template, request, flash, redirect, session
from server import app

talks=pd.read_csv("ted_main.csv")

def load_talks():
    """Load users from u.user into database."""

    print("Talks")
    
    i=0
    while i < 2550:
        speaker_name=talks.iloc[i,6]
        speaker_job=talks.iloc[i,12]
        time=(datetime.datetime.fromtimestamp(int(talks.iloc[i][4])))
        published_month=int(time.strftime("%w"))
        published_day=int(time.strftime("%m"))
        published_year=int(time.strftime("%Y"))
        talk_name=talks.iloc[i,14]
        duration=int(talks.iloc[i,2])
        event=talks.iloc[i,3]
        languages=int(talks.iloc[5])
        talk_id=i
        i+=1
        talk = Talk(talk_id=talk_id,
                    speaker_name=speaker_name,
                    speaker_job=speaker_job, published_date=published_date, talk_name=talk_name,
                    duration = duration, event=event, languages=languages)

        # We need to add to the session or it won't ever be stored
        db.session.add(talk)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()

def load_outcomes():
    """Load users from u.user into database."""

    print("Outcomes")
    
    i=0
    while i < 2550:
        num_views=int(talks.iloc[i,0])
        num_comments=int(talks.iloc[i,16])
        outcome_id=i
        i+=1
        outcome = Outcome(num_views=num_views,
                    num_comments=num_comments,
                    outcome_id=outcome_id)

        # We need to add to the session or it won't ever be stored
        db.session.add(outcome)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

load_talks()
