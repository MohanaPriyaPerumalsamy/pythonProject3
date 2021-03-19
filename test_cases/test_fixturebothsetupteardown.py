import pytest
@pytest.fixture()
def setup():
    print("Fixture Setup")
    yield
    print("fixture_yield_teardown")
def test_test1(setup):
   print("test_test1 will executed after setup")