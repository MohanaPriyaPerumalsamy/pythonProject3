import pytest

@pytest.mark.usefixtures("setup3")
class TestClassUsingFixtureExample:
    def test_Test1(self):
        print("test_Test1 will execute after Setup")

    def test_Test2(self):
        print("test_Test2 will execute after Setup")
