import pytest
@pytest.mark.Regression
def test_login1():
    print("test_login Regression")
@pytest.mark.Smoke
def test_login2():
    print("test_login Smoke")
@pytest.mark.Functional
def test_login3():
    print("test_login Functional")