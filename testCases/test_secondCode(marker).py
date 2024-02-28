import pytest

#annotation for regression- select test cases
@pytest.mark.login
@pytest.mark.regression
def test_regression1():
    print("i am reg1")

#annotation for expected dfailure
@pytest.mark.xfail
def test_regression2():
    print("i am reg2")
    assert 4 == 5

@pytest.mark.smoke
def test_regression3():
    print("i am reg3")
