from server.models import Actor, Videos
from server.models import Relationship_Videos, Relationship_Actor_Videos
from datetime import datetime
from sqlalchemy import func
from server import db
import json


class DBYouTube:

    def get_all_actors_name():
        with open('config/actors.json') as data_file:
            actors_json = json.load(data_file)
            actors_name = [name['actor'] for name in actors_json['channels']]
        return actors_name

    def get_dates():
        dates = db.session.query(Actor.collected_date).\
            order_by(Actor.collected_date.desc()).\
            distinct()
        all_dates = [item[0].strftime('%Y-%m-%d') for item in dates]

        return {'dates': all_dates}

    def get_info_actor(date, actor):
        format_date = datetime.strptime(date, '%Y-%m-%d').date()
        actor = db.session.query(Actor).filter(
            Actor.collected_date == format_date,
            func.lower(Actor.actor_name) == func.lower(actor)
        ).first()

        if actor is not None:
            del actor.__dict__['_sa_instance_state']
            return actor.__dict__
        else:
            return None

    def get_actor_videos(date, channel_id):
        format_date = datetime.strptime(date, '%Y-%m-%d').date()
        videos = db.session.query(Videos).join(
            Relationship_Actor_Videos
            ).filter(Relationship_Actor_Videos.collected_date == format_date,
                     Relationship_Actor_Videos.channel_id == channel_id).all()

        all_videos = []
        if videos is not None:
            for item in videos:
                del item.__dict__['_sa_instance_state']
                if item.__dict__['tags'] != 'disabled':
                    item.__dict__['tags'] = parser_tags(item.__dict__['tags'])
                all_videos.append(item.__dict__)

            return all_videos
        else:
            return None

    def is_not_video_in_db(video_id, date):
        format_date = datetime.strptime(date, '%Y-%m-%d').date()
        video = db.session.query(Videos).filter(
            Videos.collected_date == format_date,
            Videos.video_id == video_id
        ).first()
        return video is None

    def get_video_by_actor(date, channel_id, video_id):
        format_date = datetime.strptime(date, '%Y-%m-%d').date()

        # check if relation between given actor and given video exists in DB
        actor = db.session.query(
            Relationship_Actor_Videos).filter(
                Relationship_Actor_Videos.collected_date == format_date,
                Relationship_Actor_Videos.video_id == video_id,
                Relationship_Actor_Videos.channel_id == channel_id
            ).first()

        related_videos_results = None
        video_info = None
        if actor is not None:
            # select in DB video info
            video_info = db.session.query(
                Videos).filter(
                    Videos.collected_date == format_date,
                    Videos.video_id == video_id
                ).first()

            if video_info is not None:
                del video_info.__dict__['_sa_instance_state']
                if video_info.__dict__['tags'] != 'disabled':
                    video_info.__dict__['tags'] = parser_tags(
                        video_info.__dict__['tags']
                    )
                video_info = video_info.__dict__
                original_video_id = video_info['video_id']

                # select in DB related videos info
                related_videos_results = db.session.query(
                        Videos
                    ).join(
                        Relationship_Videos
                    ).filter(
                        Relationship_Videos.collected_date == format_date,
                        Relationship_Videos.original_video_id ==
                        original_video_id
                    ).all()

                related_videos = []
                if related_videos_results is not None:
                    for item in related_videos_results:
                        del item.__dict__['_sa_instance_state']
                        if item.__dict__['tags'] != 'disabled':
                            item.__dict__['tags'] = parser_tags(
                                item.__dict__['tags']
                            )
                        related_videos.append(item.__dict__)

        if related_videos_results is None or video_info is None:
            result = None
        else:
            result = {'video': video_info, 'related_videos': related_videos}

        return result

    def get_all_videos(date):
        videos_db = db.session.query(Videos).filter(
            Videos.collected_date == date
        ).all()
        videos = []
        if videos_db is not None:
            for item in videos_db:
                del item.__dict__['_sa_instance_state']
                if item.__dict__['tags'] != 'disabled':
                    item.__dict__['tags'] = parser_tags(item.__dict__['tags'])
                videos.append(item.__dict__)

        return videos

    def add_actor(item):

        actor_db = Actor(actor_name=item['actor_name'],
                         actor_username=item['actor_username'],
                         channel_id=item['channel_id'],
                         title=item['title'],
                         subscribers=item['subscribers'],
                         video_count=item['video_count'],
                         view_count=item['view_count'],
                         created_date=item['created_date'],
                         keywords=item['keywords'],
                         collected_date=item['collected_date'],
                         thumbnail_url=item['thumbnail_url'],
                         description=item['description'],
                         banner_url=item['banner_url'],
                         above_one_hundred_thousand=item['hundred_thousand'])

        db.session.add(actor_db)
        db.session.commit()

    def add_videos(item):
        if DBYouTube.is_not_video_in_db(video_id=item['video_id'],
                                        date=str(item['collected_date'])):
            video_db = Videos(views=item['views'],
                              title=item['title'],
                              likes=item['likes'],
                              dislikes=item['dislikes'],
                              comments=item['comments'],
                              favorites=item['favorites'],
                              url=item['url'],
                              publishedAt=item['publishedAt'],
                              description=item['description'],
                              tags=item['tags'],
                              embeddable=item['embeddable'],
                              duration=item['duration'],
                              thumbnail=item['thumbnail'],
                              category=item['category'],
                              collected_date=item['collected_date'],
                              channel_id=item['channel_id'],
                              video_id=item['video_id'])
            db.session.add(video_db)
            db.session.commit()

    def add_relationship_videos(child_video_id,
                                parent_date, parent_id):
        relationship = Relationship_Videos(
                                            video_id=child_video_id,
                                            collected_date=parent_date,
                                            original_video_id=parent_id
        )

        db.session.add(relationship)
        db.session.commit()

    def add_actor_video_relationship(video_id, channel_id, collected_date):
        relationship_actor_db = Relationship_Actor_Videos(
            video_id=video_id,
            channel_id=channel_id,
            collected_date=collected_date
        )
        db.session.add(relationship_actor_db)
        db.session.commit()


def parser_tags(tags):
    tags = tags.replace('"', '')
    tags = '["' + tags[1:]
    tags = tags[:-1] + '"]'
    tags = tags.replace(',', '","')
    tags = tags.replace(':', '')
    return json.loads(tags)
