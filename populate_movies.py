import os
import django
import uuid
from datetime import date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netflix_site.settings')
django.setup()

from core.models import Movie

# Define your media directories relative to the script location or provide absolute paths
movie_image_dir = 'path/to/media/movie_images'  # Update this path
movie_video_dir = 'path/to/media/movie_videos'  # Update this path

# Define your movie data
movies_data = [
    {
        "title": "Movie Title 1",
        "description": "Description for Movie 1",
        "release_date": date(2023, 1, 1),
        "genre": "action",
        "length": 120,
        "image_card": "movie_images/card1.png",
        "image_cover": "movie_images/poster1.png",
        "video": "movie_videos/movie_clip.mp4",
    },
    {
        "title": "Movie Title 2",
        "description": "Description for Movie 2",
        "release_date": date(2023, 1, 2),
        "genre": "comedy",
        "length": 95,
        "image_card": "movie_images/card2.jpg",
        "image_cover": "movie_images/poster2.jpg",
        "video": "movie_videos/movie_clip_BrNpigZ.mp4",
    },
    {
        "title": "Movie Title 3",
        "description": "Description for Movie 3",
        "release_date": date(2023, 1, 3),
        "genre": "drama",
        "length": 140,
        "image_card": "movie_images/card3.jpg",
        "image_cover": "movie_images/poster3.jpg",
        "video": "movie_videos/movie_clip_DwK6pEi.mp4",
    },
    {
        "title": "Movie Title 4",
        "description": "Description for Movie 4",
        "release_date": date(2023, 1, 4),
        "genre": "horror",
        "length": 130,
        "image_card": "movie_images/card4.jpg",
        "image_cover": "movie_images/poster4.png",
        "video": "movie_videos/movie_clip_INcks3p.mp4",
    },
    {
        "title": "Movie Title 5",
        "description": "Description for Movie 5",
        "release_date": date(2023, 1, 5),
        "genre": "romance",
        "length": 110,
        "image_card": "movie_images/card5.jpg",
        "image_cover": "movie_images/poster5.webp",
        "video": "movie_videos/movie_clip_okHtjGf.mp4",
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
        image_card=os.path.join(movie_image_dir, movie['image_card']),
        image_cover=os.path.join(movie_image_dir, movie['image_cover']),
        video=os.path.join(movie_video_dir, movie['video']),
        movie_views=0
    )
    m.save()
    print(f"Added: {m.title}")

print("Movie population complete!")
