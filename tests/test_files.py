import learn.files as f
import pytest

def test_sizeHumanReadable_o():
    size = 1000
    sizeHR = f.sizeHumanReadable(size)
    assert "1000.000 o" == sizeHR

def test_sizeHumanReadable_ko():
    size = 2048
    sizeHR = f.sizeHumanReadable(size)
    assert "2.000 Ko" == sizeHR

def test_sizeHumanReadable_mo(sizemo):
    size, sizeHrExpected = sizemo
    sizeHR = f.sizeHumanReadable(size)
    assert sizeHrExpected == sizeHR

def test_sizeHumanReadable_allUnits(size_sizeHR):
    size, sizeHrExpected = size_sizeHR
    sizeHR = f.sizeHumanReadable(size)
    assert sizeHrExpected == sizeHR

@pytest.mark.parametrize("size,sizeHrExpected", [
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
def test_sizeHumanReadable_allUnits2(size, sizeHrExpected):
    sizeHR = f.sizeHumanReadable(size)
    assert sizeHrExpected == sizeHR

# def test_other():
#     assert False