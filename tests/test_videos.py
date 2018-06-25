from youtube.youtube import YoutubeAPI
from youtube.videos import Videos
import unittest


class TestVideos(unittest.TestCase):

    def setUp(self):
        self._video = Videos()
        self._user = YoutubeAPI()

    def test_has_activities(self):
        channel_id = 'UCj34AOIMl_k1fF7hcBkD_dw'
        max_results = '5'
        result = self._video.get_activity_info(channel_id, max_results)
        self.assertTrue(result['items'])

    def test_category_info(self):
        id = '28'
        result = self._video.get_category_info(id)
        self.assertEqual(result['items'][0]['snippet']['title'],
                         'Ciência e tecnologia')

    def test_has_search(self):
        related_to_video_id = 'Xx7bjU7gabM'
        max_results = '5'
        type = 'video'
        result = self._video.get_search_info(max_results, related_to_video_id,
                                             type)
        self.assertTrue(result['items'])

    def test_has_video(self):
        channel_id = 'V6OvM-0SGUU'
        max_results = '5'
        result = self._video.get_videos_info(channel_id, max_results)
        self.assertTrue(result['items'])

    def test_all_video_ids(self):
        user_id = 'UC9uefWa6TXIPDRWGZYMcTuA'
        max_results = '7'
        result = self._user.get_channel_info(user_id)
        channel_id = self._user.get_channel_id(result)
        result_activities = self._video.get_activity_info(channel_id,
                                                          max_results)
        video_ids = self._video.get_all_video_ids(result_activities)
        assert_list = ['FvNsjk62Xi8']
        self.assertEqual(video_ids[-1:], assert_list)

    def test_all_videos_count_user_id(self):
        user_id = 'UCsCI7wlAwbzTPK55yVaX2Ig'
        result = self._user.get_channel_info(user_id)
        max_results = 50
        video_views = self._video.get_all_video_views_user_id(result,
                                                              max_results, 0)
        video_title = video_views[-1]['title']
        self.assertEqual(video_title, 'Encontro Presencial - IAEaD 2018')
        video_view = int(video_views[-1]['views'])
        video_url = str(video_views[-1]['url'])
        video_likes = str(video_views[-1]['likes'])
        video_dislikes = str(video_views[-1]['dislikes'])
        video_comments = str(video_views[-1]['comments'])
        video_favorites = int(video_views[-1]['favorites'])
        self.assertGreater(video_view, 16)
        self.assertLess(video_view, 100)
        self.assertEqual(video_url,
                         'https://www.youtube.com/watch?v=B-5VHSKIuHw')

        self.assertEqual(video_likes, '1')
        self.assertEqual(video_dislikes, '0')
        self.assertEqual(video_comments, '0')
        self.assertGreaterEqual(video_favorites, 0)


if __name__ == '__main__':
    unittest.main()
