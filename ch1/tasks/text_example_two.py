import pytest 


@pytest.mark.mark_this_my_gee
def test_a_number():
    a_list = [3,4,5,6,7]
    a_number = [x for x in a_list if x == 4 ]
    assert a_number == 4