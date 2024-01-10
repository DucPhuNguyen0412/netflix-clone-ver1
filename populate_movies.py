import os
import django
import uuid
from datetime import date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netflix_site.settings')
django.setup()

from core.models import Movie

# Define your movie data
movies_data = [
    {
        "title": "A Fall From Grace",
        "description": "Disheartened since her ex-husband's affair, Grace Waters feels restored by a new romance. But when secrets erode her short-lived joy, Grace's vulnerable side turns violent.",
        "release_date": date(2023, 1, 1),
        "genre": "action",
        "length": 120,
        "image_card": "media/movie_images/card1.png",
        "image_cover": "media/movie_images/poster1.png",
        "video": "media/movie_videos/movie_clip.mp4",
    },
    {
        "title": "The Night Agent",
        "description": "While monitoring an emergency line, a vigilant FBI agent answers a call that plunges him into a deadly conspiracy involving a mole at the White House.",
        "release_date": date(2023, 1, 2),
        "genre": "comedy",
        "length": 95,
        "image_card": "media/movie_images/card2.jpg",
        "image_cover": "media/movie_images/poster2.jpg",
        "video": "media/movie_videos/movie_clip_BrNpigZ.mp4",
    },
    {
        "title": "Lupin",
        "description": "Inspired by the adventures of Arsène Lupin, gentleman thief Assane Diop sets out to avenge his father for an injustice inflicted by a wealthy family.",
        "release_date": date(2023, 1, 4),
        "genre": "horror",
        "length": 130,
        "image_card": "media/movie_images/card4.jpg",
        "image_cover": "media/movie_images/poster4.png",
        "video": "media/movie_videos/movie_clip_INcks3p.mp4",
    },
    {
        "title": "Blood & Water",
        "description": "After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth.",
        "release_date": date(2023, 1, 5),
        "genre": "romance",
        "length": 110,
        "image_card": "media/movie_images/card5.jpg",
        "image_cover": "media/movie_images/poster5.webp",
        "video": "media/movie_videos/movie_clip_okHtjGf.mp4",
    },
    {
        "title": "Suits",
        "description": "On the run from a drug deal gone bad, brilliant college dropout Mike Ross finds himself working with Harvey Specter, one of New York City's best lawyers.",
        "release_date": date(2023, 1, 5),
        "genre": "romance",
        "length": 110,
        "image_card": "media/movie_images/card6.jpg",
        "image_cover": "media/movie_images/poster6.webp",
        "video": "media/movie_videos/movie_clip_okHtjGf.mp4",
    },
    {
        "title": "Bodies",
        "description": "Four detectives. Four timelines. One body. To save Britain's future, they'll need to solve the murder that altered the course of history first.",
        "release_date": date(2023, 1, 5),
        "genre": "romance",
        "length": 110,
        "image_card": "media/movie_images/card7.jpg",
        "image_cover": "media/movie_images/poster7.webp",
        "video": "media/movie_videos/movie_clip_okHtjGf.mp4",
    },
    {
        "title": "Breaking Bad",
        "description": "A high school chemistry teacher dying of cancer teams with a former student to secure his family's future by manufacturing and selling crystal meth.",
        "release_date": date(2023, 1, 5),
        "genre": "romance",
        "length": 110,
        "image_card": "media/movie_images/card9.jpg",
        "image_cover": "media/movie_images/poster9.webp",
        "video": "media/movie_videos/movie_clip_okHtjGf.mp4",
    },
]

for movie in movies_data:
    m = Movie(
        uu_id=uuid.uuid4(),
        title=movie['title'],
        description=movie['description'],
        release_date=movie['release_date'],
        genre=movie['genre'],
        length=movie['length'],
        image_card=movie['image_card'],
        image_cover=movie['image_cover'],
        video=movie['video'],
        movie_views=0
    )
    m.save()
    print(f"Added: {m.title}")

print("Movie population complete!")
