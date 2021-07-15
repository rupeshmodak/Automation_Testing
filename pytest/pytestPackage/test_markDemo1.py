import pytest


def test_firstdemo():
    print("Hello")


@pytest.mark.xfail
def test_seconddemocredit():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser)
