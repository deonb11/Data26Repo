from deon_2_ships import *


# Test passed - data in list
def test_get_api():
    assert any(get_from_api())


# Test passed - urls in list
def test_collect_urls():
    assert any(collect_ships_url())
#
#
# Test passed - pilot name in list
def test_change_to_name():
    assert any(change_to_name())
#
#
# Test passed - collection data is a dictionary
def test_upload_collection():
    for i in sw_starships.find():
        assert type(i) is dict
# #
# #
# Test passed - Object in pilots is a dictionary or string
def test_pilot_id():
    for i in sw_starships.find():
        for j in i['pilots']:
            assert type(j) is dict or str
