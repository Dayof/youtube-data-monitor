from server.models import Actor, Videos
from server.models import Relationship_Actor_Videos, Relationship_Videos
from server.queries import DBYouTube
from flask import Flask
import unittest
from datetime import datetime
from server import app, db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db.init_app(app)


class TestFlask(unittest.TestCase):

    def setUp(self):
        app.app_context().push()
        db.create_all()
        collected_date_value = datetime.strptime('2018-06-14',
                                                 '%Y-%m-%d').date()
        actor_db = {
                'actor_name': 'Marina Silva',
                'actor_username': 'msilvaonline',
                'channel_id': 'channel_id_value',
                'title': 'Marina Silva',
                'subscribers': 13515,
                'video_count': 876,
                'view_count': 4307555,
                'created_date': '2010-01-26',
                'keywords': 'keywords_value',
                'collected_date': collected_date_value,
                'thumbnail_url': 'thumbnail_url_value',
                'description': 'description_value',
                'banner_url': 'banner_url_value',
                'hundred_thousand': False}

        DBYouTube.add_actor(actor_db)

        video_db = {
              'views': '1',
              'title': 'Video Marina Silva',
              'likes': '1',
              'dislikes': '1',
              'comments': '1',
              'favorites': '1',
              'url': 'url Marina Silva',
              'publishedAt': 'data publicação',
              'description': 'descrição',
              'tags': 'tags',
              'embeddable': 'embeddable',
              'duration': 'duration',
              'thumbnail': 'thumbnail',
              'category': 'category',
              'collected_date': collected_date_value,
              'channel_id': 'channel_id_value',
              'video_id': '1'
        }

        DBYouTube.add_videos(video_db)

        related_video_db = {
            'title': 'Related title',
            'likes': '34',
            'views': '8234',
            'dislikes': '3',
            'comments': '2',
            'favorites': '10',
            'url': 'https://www.youtube.com/watch?v=hFc_scYRasdY',
            'publishedAt': '2015-12-13T17:37:01.000Z',
            'description': '',
            'tags': 'disabled',
            'embeddable': 'True',
            'duration': 'PT4H24M20S',
            'thumbnail': 'https://i.ytimg.com/vi/hFc_sasdRpQY/hqdefault.jpg',
            'category': 'Entretenimento',
            'video_id': '2',
            'collected_date': collected_date_value,
            'channel_id': 'channel_id_value'
        }

        DBYouTube.add_videos(related_video_db)

        DBYouTube.add_relationship_videos('2', collected_date_value, '1')
        DBYouTube.add_actor_video_relationship(
            '1',
            'channel_id_value',
            collected_date_value)

        self.app = app.test_client()
        # Propaga as exceções para o cliente de teste
        self.app.testing = True

    def test_db_get_dates(self):
        dates = DBYouTube.get_dates()
        self.assertEqual(dates['dates'], ['2018-06-14'])

    def test_db_get_dates_error(self):
        dates = DBYouTube.get_dates()
        self.assertNotEqual(dates['dates'], ['2019-07-14'])

    def test_db_get_info_actor_name(self):
        actor = DBYouTube.get_info_actor('2018-06-14', 'Marina Silva')
        self.assertEqual(actor['actor_name'], 'Marina Silva')

    def test_db_get_info_actor_name(self):
        actor = DBYouTube.get_info_actor('2018-06-14', 'Marina Silva')
        self.assertEqual(actor['subscribers'], 13515)

    def test_db_get_info_actor_none(self):
        actor = DBYouTube.get_info_actor('2018-06-14', 'Bolsonaro')
        self.assertEqual(actor, None)

    def test_db_get_actor_videos(self):
        videos = DBYouTube.get_actor_videos('2018-06-14', 'channel_id_value')
        self.assertEqual(videos[0]['title'], 'Video Marina Silva')

    def test_db_get_actor_videos_empty(self):
        videos = DBYouTube.get_actor_videos('2018-06-15', 'channel_id_value')
        self.assertEqual(videos, [])

    def test_db_get_actor_videos(self):
        videos = DBYouTube.get_actor_videos('2018-06-14', 'channel_id_value')
        self.assertEqual(videos[0]['views'], '8234')

    def test_db_get_actor_videos(self):
        videos = DBYouTube.get_actor_videos('2018-06-14', 'channel_id_value')
        self.assertEqual(videos[0]['likes'], '1')

    def test_is_not_video_in_db_true_by_id(self):
        bool = DBYouTube.is_not_video_in_db('fake_id', '2018-06-14')
        self.assertEqual(bool, True)

    def test_is_not_video_in_db_false_by_id(self):
        bool = DBYouTube.is_not_video_in_db('1', '2018-06-14')
        self.assertEqual(bool, False)

    def test_is_not_video_in_db_true_by_date(self):
        bool = DBYouTube.is_not_video_in_db('1', '2018-06-01')
        self.assertEqual(bool, True)

    def test_is_not_video_in_db_false_by_date(self):
        bool = DBYouTube.is_not_video_in_db('1', '2018-06-14')
        self.assertEqual(bool, False)

    def test_get_video_by_actor(self):
        video = DBYouTube.get_video_by_actor('2018-06-14',
                                             'channel_id_value', '1')
        self.assertNotEqual(video, None)

    def test_get_video_by_actor_date_error(self):
        video = DBYouTube.get_video_by_actor('2018-06-10',
                                             'channel_id_value', '1')
        self.assertEqual(video, None)

    def test_get_video_by_actor_channel_error(self):
        video = DBYouTube.get_video_by_actor('2018-06-14',
                                             'fake_channel_id', '1')
        self.assertEqual(video, None)

    def test_get_video_by_actor_video_error(self):
        video = DBYouTube.get_video_by_actor('2018-06-14',
                                             'channel_id_value', 'fake_id')
        self.assertEqual(video, None)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
