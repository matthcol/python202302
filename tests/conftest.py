import pytest

@pytest.fixture
def sizemo():
    return 2.25*2**20, "2.250 Mo"

@pytest.fixture(params=[
    (2**10, "1.000 Ko"),
    (2**20, "1.000 Mo"),
    (2**30, "1.000 Go"),
    (2**40, "1.000 To"),
    (2**50, "1.000 Po"),
    (2**60, "1.000 Eo"),
    (2**70, "1.000 Zo"),
    (2**80, "1.000 Yo"),
    (2**90, "1024.000 Yo"),
])
def size_sizeHR(request):
    # setup
    return request.param
    # teardown (yield instead of return)
