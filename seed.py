# seed.py
import csv
from app import app
from models import db, Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        with open('seed.csv', mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                episode_date = row['Show']
                guest_name = row['Raw_Guest_List']
                guest_occupation = row['GoogleKnowlege_Occupation']
                rating = 3  # Default rating

                episode = Episode.query.filter_by(date=episode_date).first()
                if not episode:
                    episode = Episode(date=episode_date, number=1)
                    db.session.add(episode)
                    db.session.commit()

                guest = Guest.query.filter_by(name=guest_name).first()
                if not guest:
                    guest = Guest(name=guest_name, occupation=guest_occupation)
                    db.session.add(guest)
                    db.session.commit()

                appearance = Appearance(
                    rating=rating,
                    episode_id=episode.id,
                    guest_id=guest.id,
                    air_date=episode_date
                )
                db.session.add(appearance)

            db.session.commit()

if __name__ == "__main__":
    seed_data()
