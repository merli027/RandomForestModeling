
import datetime
from sqlalchemy import func
import pandas as pd
import numpy as np
from model import Talk, Speaker, connect_to_db, db, Rating, Talk_Rating
from flask import Flask, render_template, request, flash, redirect, session
from server import app


talks=pd.read_csv("ted_main.csv")

def load_talk_rating():
    """Load relationships into the database ahhh."""

    print("Talk_Rating_Rel")

    new_talks=talks['ratings'].map(eval)

    i=1
    ted_id=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    row1=new_talks[0]
    rating=pd.DataFrame(row1)
    rating['ted_id'] = ted_id
    while i < new_talks.size:
        row1=new_talks[i]
        new_rating=pd.DataFrame(row1)
        ted_id=[i,i,i,i,i,i,i,i,i,i,i,i,i,i]
        new_rating['ted_id'] = ted_id
        rating=pd.concat([rating, new_rating], axis=0)
        i+=1

    #print(rating.head())
    #rating.shape[0]
    count=0
    while count < rating.shape[0]:
        rating_count = int(rating.iloc[count,2])
        rating_id = int(rating.iloc[count,0])
        ted_talk_id = int(rating.iloc[count,3])
        count+=1

        talk_rating = Talk_Rating(rating_id=rating_id, rating_count=rating_count, ted_talk_id=ted_talk_id)
        # We need to add to the session or it won't ever be stored
        db.session.add(talk_rating)

        # provide some sense of progress
        if count % 100 == 0:
            print(count)

    # Once we're done, we should commit our work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

load_talk_rating()