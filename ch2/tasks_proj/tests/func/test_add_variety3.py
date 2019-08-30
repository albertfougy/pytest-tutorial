from tasks import Task
import tasks
import pytest


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()  

tasks_to_try=(Task('sleep', done=True),
           Task('wake', 'brian'),
           Task('breathe', 'albert'),
           Task('exercise', 'Tom', True),
           Task('floss', 'fOuGy', False))

task_ids = ['Task({},{},{})'.format(t.summary,t.owner,t.done)
            for t in tasks_to_try]


def equivalent(t1, t2):
    """Check two tasks for equivalence"""
    # Compare everything but the id field
    return ((t1.summary == t2.summary) and 
            (t1.owner == t2.owner) and 
            (t1.done == t2.done))


@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data for multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id




