import pytest

@pytest.mark.usefixtures("setup2")
class testfixtureusingclass:
    def test_Test1(self):
        print("test_test1 will execute after setup")

    def test_Test2(self):
        print("test_test2 will execute after setup")