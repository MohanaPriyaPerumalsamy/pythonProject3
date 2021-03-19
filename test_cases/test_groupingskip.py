import pytest
@pytest.mark.Regression
@pytest.mark.skip
def test_login1():
    print("test_login Regression")
@pytest.mark.Smoke
@pytest.mark.skip
def test_login2():
    print("test_login Smoke")
@pytest.mark.Functional
@pytest.mark.skip
def test_login3():
    print("test_login Functional")