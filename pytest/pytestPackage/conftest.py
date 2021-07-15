import pytest


@pytest.fixture(scope="class")
def setup():
    print("First Line")
    yield
    print("Last Line")


@pytest.fixture
def datafixture():
    print("Personal Info is being stored...")
    return ["Rupesh", "Modak", "rupeshmodak@gmail.com"]


@pytest.fixture(params=[("chrome", "Rupesh"), ("firefox", "Modak"), ("IE", "RM")])
def crossbrowser(request):
    return request.param
