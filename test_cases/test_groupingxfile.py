import pytest
@pytest.mark.Regression
@pytest.mark.xfail
def test_login1():
    print("test_login Regression")
@pytest.mark.Smoke
@pytest.mark.xfail
def test_login2():
    print("test_login Smoke")
@pytest.mark.Functional
@pytest.mark.xfail
def test_login3():
    print("test_login Functional")