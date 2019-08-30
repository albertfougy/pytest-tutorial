import pytest
import tasks
from tasks import Task

# Version 1 of parametrize testing
# def test_add_1():
#     """tasks.get() using id returned from add() works."""
#     task = Task('breathe', 'BRIAN', True)
#     task_id = tasks.add(task)
#     t_from_db = tasks.get(task_id)
#     assert equivalent(t_from_db, task)


# def equivalent(t1, t2):
#     """Check two tasks for equivalence"""
#     # Compare everything but the id field
#     return ((t1.summary == t2.summary) and 
#             (t1.owner == t2.owner) and 
#             (t1.done == t2.done))


# Version 2 of parametrize testing
# @pytest.mark.parametrize('task',
# [Task('sleep', done=True),
# Task('wake', 'brian'),
# Task('dande', 'albert', True),
# Task('exercise', 'Tom', False)])
# def test_add_2(task):
#     """Demonstrate parametrize with one parameter"""
#     task_id = tasks.add(task)
#     t_from_db = tasks.get(task_id)
#     assert equivalent(t_from_db, task)


# Version 3 of parametrize testing with tuples
# @pytest.mark.parametrize('summary, owner, done',
#                         [('sleep', None, False),
#                         ('wake', 'brian', False),
#                         ('breathe', 'albert', True),
#                         ('exercise', 'Tom', False),
#                         ])
# def test_add_3(summary, owner, done):
#     """Demonstrate parametrize with one parameter"""
#     task = Task(summary, owner, done)
#     task_id = tasks.add(task)
#     t_from_db = tasks.get(task_id)
#     assert equivalent(t_from_db, task)

# Version 4 of parametrize testing with a list outside of function
# list can be added with or without brackets inside parens
tasks_to_try=(Task('sleep', done=True),
           Task('wake', 'brian'),
           Task('breathe', 'albert'),
           Task('exercise', 'Tom', True),
           Task('floss', 'fOuGy', False))
# task here is the same as in version 2 as beginning of list
@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """Demonstrate parametrize with one parameter"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Check two tasks for equivalence"""
    # Compare everything but the id field
    return ((t1.summary == t2.summary) and 
            (t1.owner == t2.owner) and 
            (t1.done == t2.done))

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

    



