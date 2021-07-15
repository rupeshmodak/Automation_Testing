import pytest


@pytest.mark.skip
def test_thirddemo():
    greed = "Hi"
    assert "Hello" == greed, "Test failed due to string doesn't match"


def test_fourthdemocredit():
    a = 4
    assert a+2 == 6
