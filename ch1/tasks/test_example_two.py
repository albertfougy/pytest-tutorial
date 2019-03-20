import pytest 

def test_a_number():
    a_list = [3,4,5,6,7]
    a_number = [x for x in a_list if x == a_list[1]]
    assert [4]== a_number 