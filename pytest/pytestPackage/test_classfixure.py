import pytest


@pytest.mark.usefixtures("setup")
class TestFixure:

    def test_fixuredemo1(self):
        print("Demo 1")

    def test_fixuredemo2(self):
        print("Demo 2")

    def test_fixuredemo3(self):
        print("Demo 3")

    def test_fixuredemo4(self):
        print("Demo 4")
