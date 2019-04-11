'''Use the Task type to show test failures'''
from tasks import Task

def test_task_equality():
    """Different tasks should not be equal."""
    t1 = Task('sit at my chair', 'albert')
    t2 = Task('going to bathroom', 'fougy')

    assert t1 == t2

def test_task_are_equal():
    """Different tasks should not be equal."""
    t1 = Task('sit at my chair', 'albert')
    t1 = Task('sit at my chair', 'albert')


def test_task_dict():
    """Different tasks compared as dicts should not be equal."""
    t1_dict = Task('sit on my desk', 'albert')._asdict()
    t2_dict = Task('sit at my desks', 'albert')._asdict()
    
    assert t1_dict == t2_dict
