"""Utility file to seed ted talk data into tables"""

import datetime
from sqlalchemy import func
import pandas as pd
from model import Speaker, connect_to_db, db
from flask import Flask, render_template, request, flash, redirect, session
from server import app

talks=pd.read_csv("ted_main.csv")

def load_speakers():
    """Load users from u.user into database."""

    print("Speakers")

    dropped_speakers=talks.drop_duplicates(subset="main_speaker")
    i=0
    while i < dropped_speakers.shape[0]:
        speaker_name=dropped_speakers.iloc[i,6]
        speaker_job=dropped_speakers.iloc[i,12]
        speaker_id=i
        i+=1
        speaker = Speaker(speaker_name=speaker_name,
                    speaker_job=speaker_job,
                    speaker_id=speaker_id)

        # We need to add to the session or it won't ever be stored
        db.session.add(speaker)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

load_speakers()

