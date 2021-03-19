import pytest
@pytest.fixture()
def setup():
    print("Fixture Setup")
def test_test1(setup):
   print("test_test1 will executed after setup")