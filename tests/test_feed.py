from alt_side_parking.feed import (
    get_nyc_alt_side_parking_tweets,
    is_suspended_tomorrow,
)
from automock import swap_mock


@swap_mock("alt_side_parking.feed.TwitterBot", failed_response=True)
def test_failed_fetch():
    tweets = get_nyc_alt_side_parking_tweets()
    assert [] == tweets


def test_get_tweets():
    tweets = get_nyc_alt_side_parking_tweets()
    assert [
        "#NYCASP rules will be in effect tomorrow, Monday, September 21",
        "#NYCASP rules are suspended today, September 20",
        "#NYCASP rules will be suspended tomorrow, Sunday, September 20",
    ] == tweets


def test_is_suspended_failed(freezer):
    freezer.move_to("2020-09-23 16:00:00")
    assert not is_suspended_tomorrow()


def test_is_suspended_success(freezer):
    freezer.move_to("2020-09-19 16:00:00")
    assert is_suspended_tomorrow()
