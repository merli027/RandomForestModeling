"""Utility file to seed ted talk data into tables"""

import datetime
from sqlalchemy import func
import pandas as pd
import numpy as np
from model import Talk, Speaker, connect_to_db, db, Rating, Talk_Rating
from flask import Flask, render_template, request, flash, redirect, session
from server import app


talks=pd.read_csv("ted_main.csv")
for col in talks.columns:
    print(col)


print(1245/60)