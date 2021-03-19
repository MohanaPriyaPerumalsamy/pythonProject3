#import pytest

#@pytest.fixture(scope="class")
#def setup2():
 #   print("Fixturesetup2")
  #  yield
  #  print("test_test1 will execute after setup")


import pytest

@pytest.fixture()
def setup2():
    print("Fixture - Setup - 2")
    yield
    print("Fixture - Yield Tear down - 2")

@pytest.fixture(scope="class")
def setup3():
    print("Fixture - setup Class - 3")
    yield
    print("Fixture - Yield Tear down Class - 3")

@pytest.fixture()
def dataParam():
    print("DataParam")
    return ["India","America"]
