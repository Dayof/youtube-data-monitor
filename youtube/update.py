from core.actors_info import scrap_basic_actors_info, insert_actors_info
from youtube.youtube import YoutubeAPI
from core.output import FileOutput
from youtube.videos import Videos
from server.models import Actor, db
from server.models import Videos as VideosDB, Relationship_Actor
from server.queries import DBYouTube
from server.main import app
import time
import os
import json

# scrap_basic_actors_info()
youtube_user = insert_actors_info()
video = Videos()
app.app_context().push()
db.create_all()  # create the tables and database


# def insert_video_db(item):
#     if DBYouTube.is_not_video_in_db(video_id=item['id'],
#                                     date=YoutubeAPI.start_time):
#         item['collected_date'] = YoutubeAPI.start_time
#         item['channel_id'] = channel_id
#         DBYouTube.add_videos(item)


# def insert_video_db(item):
#     if DBYouTube.is_not_video_in_db(video_id=item['id'],
#                                     date=YoutubeAPI.start_time):
#         video_db = VideosDB(views=item['views'],
#                             title=item['title'],
#                             likes=item['likes'],
#                             dislikes=item['dislikes'],
#                             comments=item['comments'],
#                             favorites=item['favorites'],
#                             url=item['url'],
#                             publishedAt=item['publishedAt'],
#                             description=item['description'],
#                             tags=item['tags'],
#                             embeddable=item['embeddable'],
#                             duration=item['duration'],
#                             thumbnail=item['thumbnail'],
#                             category=item['video_category'],
#                             collected_date=YoutubeAPI.start_time,
#                             channel_id=item['channel_id'],
#                             video_id=item['id'])
#         db.session.add(video_db)
#         db.session.commit()


# def insert_actor_video_relationship(video_id, channel_id, collected_date):
#     relationship_actor_db = Relationship_Actor(
#         video_id=video_id,
#         channel_id=channel_id,
#         collected_date=collected_date
#     )
#     db.session.add(relationship_actor_db)
#     db.session.commit()


with open('config/actors.json') as data_file:
    actors = json.load(data_file)
    actors_dict = actors['channels']
    no_video_actors = []

    for actor in actors_dict:            # get ID from youtube.csv
        channel_id = actor['id']
        channel_username = actor['username']
        channel_actor = actor['actor']
        if channel_id != 'null' and channel_id:
            directory = 'data/' + YoutubeAPI.start_time
            # get all info from channel
            response = youtube_user.get_channel_info(channel_id)
            title = youtube_user.get_channel_title(response)
            subscribers = youtube_user.get_channel_subscribers(response)
            video_count = youtube_user.get_channel_video_count(response)
            view_count = youtube_user.get_channel_total_view_count(response)
            comment_count = youtube_user.get_channel_total_comment_count(
             response)
            creation_date = youtube_user.get_channel_creation_date(
             response)
            channel_thumbnail = youtube_user.get_channel_thumbnail(response)
            description = youtube_user.get_channel_description(response)
            keywords = youtube_user.get_channel_keywords(response)
            banner_thumbnail = youtube_user.get_channel_banner(response)
            hundred_thousand = youtube_user.check_above_one_hundred_thousand(
             subscribers)

            actor_db = Actor(actor_name=channel_actor,
                             actor_username=channel_username,
                             channel_id=channel_id,
                             title=title,
                             subscribers=subscribers,
                             video_count=video_count,
                             view_count=view_count,
                             created_date=creation_date.split("T")[0],
                             collected_date=YoutubeAPI.start_time,
                             thumbnail_url=channel_thumbnail,
                             description=description,
                             keywords=keywords,
                             banner_url=banner_thumbnail,
                             above_one_hundred_thousand=hundred_thousand)

            db.session.add(actor_db)
            db.session.commit()
            print(actor_db)
            videos_views = video.get_all_video_views_user_id(response, 5)

            if videos_views:
                for item in videos_views:
                    related_videos = item['related_to_video']
                    item['collected_date'] = YoutubeAPI.start_time
                    item['channel_id'] = channel_id
                    DBYouTube.add_videos(item)
                    DBYouTube.insert_actor_video_relationship(
                        item['id'],
                        channel_id,
                        YoutubeAPI.start_time
                    )
                    for related_video in related_videos:
                        related_video['collected_date'] = YoutubeAPI.start_time
                        related_video['channel_id'] = channel_id
                        DBYouTube.add_videos(related_video)
                        DBYouTube.add_relationship_videos(
                            child_video_id=related_video['id'],
                            parent_date=YoutubeAPI.start_time,
                            parent_id=item['id']
                        )
