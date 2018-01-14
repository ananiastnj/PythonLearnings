import Mathlib

def test_calc_total():
    total = Mathlib.calc_total(5,4)
    assert total ==9
    print("Addition : ")

def test_calc_multiply():
    res = Mathlib.calc_multiply(5,4)
    print("Multiplication : ")
    assert res == 20
