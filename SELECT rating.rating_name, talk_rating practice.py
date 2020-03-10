SELECT rating.rating_name, talk_rating.rating_count FROM rating JOIN talk_rating ON (talk_rating.rating_id = rating.rating_id) 
WHERE (talk_rating.ted_talk_id = ted_talk)

db.session.query(Rating, Talk_Rating).filter(talk_rating.ted_talk_id == talk_id).all()
for r,t in db.session.query(Rating, Talk_Rating).filter(talk_rating.rating_id == rating.rating_id).filter(talk_rating.ted_talk_id == talk_id).all()