import pytest
import tasks

class TestRaises():
    """Test expected exceptions with tasks.update()."""
    
    def test_add_raises(self):
        """add() should raise and exception with wrong type param."""
        with pytest.raises(TypeError):
                tasks.add(task="not a Task object") 
    
    def test_start_tasks_db_raises(self):
        """Make sure unsupported db raises an exception."""
        with pytest.raises(ValueError) as execinfo:
            tasks.start_tasks_db('some/great/path', 'mysql')
            exception_msg = execinfo.value.args[0]
            assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

    @pytest.mark.smoke
    def test_list_raises(self):
        """list() should raise an exception with wrong type of params"""
        with pytest.raises(TypeError):
            tasks.list_tasks(owner=123)

    @pytest.mark.get
    @pytest.mark.smoke
    def test_get_raises(self):
        """get() should raise an exception with wrong type param."""
        with pytest.raises(TypeError):
            tasks.get(task_id="string")
