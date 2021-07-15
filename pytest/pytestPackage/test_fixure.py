import pytest


@pytest.fixture()
def setup():
    print("First Line")
    yield
    print("Last Line")


def test_fixuredemo():
    print("Middle Line")
