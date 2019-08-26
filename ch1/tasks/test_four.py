"""Test the Task data type """
from collections import namedtuple
import pytest
import time

Task = namedtuple('Task',['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = ('None', 'False', 'None', 'None')

def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'fougy', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary':'do something',
        'owner'  : 'fougy',
        'done'   : True,
        "id"     : 21,
    }
    assert t_dict == expected

@pytest.mark.run_these_please
def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish pytest', 'Albert', False)
    t_after = t_before._replace(id=10, done=True)
    time.sleep(0.1)
    t_expected = Task('finish pytest', 'Albert', True,10)
    assert t_after == t_expected