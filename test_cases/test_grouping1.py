import pytest
@pytest.mark.Regression
def test_login11():
    print("test_login Regression")
@pytest.mark.Smoke
def test_login12():
    print("test_login Smoke")
@pytest.mark.Functional
def test_login13():
    print("test_login Functional")