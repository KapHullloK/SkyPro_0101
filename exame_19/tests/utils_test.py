import utils
import pytest


class TestUtils:

    def test_load_data(self):
        load = utils.load_data()
        assert len(load) > 0
        assert type(load) == list
        assert set(load[0].keys()) == {'arrival', 'halt', 'departure', 'pk', 'days', 'station'}

    def test_data_trains(self):
        trains = utils.data_trains()
        assert len(trains) > 0
        assert type(trains) == list

    def test_filter_data(self):
        input_user = 1
        filter = utils.filter_data(input_user)
        assert len(filter) > 0
        assert type(filter) == dict
        assert set(filter.keys()) == {'halt', 'station', 'days', 'pk', 'arrival', 'departure'}
        assert type(input_user) == int
