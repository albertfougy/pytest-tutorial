import pytest
import tasks
from tasks import Task

tasks_to_try=(Task('sleep', done=True),
           Task('wake', 'brian'),
           Task('breathe', 'albert'),
           Task('exercise', 'Tom', True),
           Task('floss', 'fOuGy', False))

task_ids = ['Task({},{},{})'.format(t.summary,t.owner,t.done)
            for t in tasks_to_try]

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db= tasks.get(task_id)
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
