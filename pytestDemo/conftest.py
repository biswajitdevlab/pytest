import pytest


@pytest.fixture(scope="class")
def setup():
    print("Run first")
    yield
#yield runs at the end of method
    print("Run last")
#def test_fixtureDemo(setup):
   # print("it depends on setup method")