import pytest


@pytest.fixture()
def set_up():
    print("Start TEST")
    yield
    print("Finish TEST")


@pytest.fixture(scope="module")
def set_group():
    print("Enter System")
    yield
    print("Exit System")

