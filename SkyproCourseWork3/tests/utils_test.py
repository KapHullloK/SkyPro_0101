import utils
import pytest


class TestUtils:

    def test_get_posts_all(self):
        posts_all = utils.get_posts_all()
        assert len(posts_all) > 0
        assert type(posts_all) == list
        assert set(posts_all[0].keys()) == {'pic', 'pk', 'views_count', 'content',
                                            'likes_count', 'poster_name', 'poster_avatar'}

    def test_get_posts_by_user(self):
        input_user = "leo"
        posts_by_user = utils.get_posts_by_user(input_user)
        assert len(posts_by_user) > 0
        assert type(posts_by_user) == list
        assert set(posts_by_user[0].keys()) == {'pic', 'pk', 'views_count', 'content',
                                                'likes_count', 'poster_name', 'poster_avatar'}
        assert type(input_user) == str

    def test_get_comments_by_post_id(self):
        input_user = 1
        comments_by_post_id = utils.get_comments_by_post_id(input_user)
        assert len(comments_by_post_id) > 0
        assert type(comments_by_post_id) == list
        assert set(comments_by_post_id[0].keys()) == {'commenter_name', 'post_id', 'comment', 'pk'}
        assert type(input_user) == int

    def test_search_for_posts(self):
        input_user = "Ага"
        search_for_posts = utils.search_for_posts(input_user)
        assert len(search_for_posts) > 0
        assert type(search_for_posts) == list
        assert set(search_for_posts[0].keys()) == {'pic', 'pk', 'views_count', 'content',
                                                   'likes_count', 'poster_name', 'poster_avatar'}
        assert type(input_user) == str

    def test_get_post_by_pk(self):
        input_user = 1
        get_post_by_pk = utils.get_post_by_pk(input_user)
        assert len(get_post_by_pk) > 0
        assert type(get_post_by_pk) == dict
        assert set(get_post_by_pk.keys()) == {'pic', 'pk', 'views_count', 'content',
                                              'likes_count', 'poster_name', 'poster_avatar'}
        assert type(input_user) == int
