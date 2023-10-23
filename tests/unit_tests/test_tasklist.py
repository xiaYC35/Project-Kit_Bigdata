from tasks.tasklist import TaskList

import pytest


class TestCodeUnderTest:

    # add_task adds a new task to the tasks list
    def test_add_task_adds_new_task_to_tasks_list(self):
        """
        Test the addition of a new task to the tasks list.
        Verifies that the name and description are correctly set.
        """
        task_list = TaskList()
        task_list.add_task("Task 1", "Description 1")
        assert len(task_list.tasks) == 1
        assert task_list.tasks[0].name == "Task 1"
        assert task_list.tasks[0].description == "Description 1"

    # remove_task removes a task from the tasks list
    def test_remove_task_removes_task_from_tasks_list(self):
        """
        Test the removal of a task from the tasks list.
        Verifies that the task is removed from the list.
        """
        task_list = TaskList()
        task_list.add_task("Task 1", "Description 1")
        task_list.remove_task("Task 1")
        assert len(task_list.tasks) == 0

    # mark_task_completed marks a task as completed and moves it to the archived tasks list
    def test_mark_task_completed_marks_task_as_completed_and_moves_to_archived_tasks_list(self):
        """
        Test marking a task as completed and moving it to the archived tasks list.
        Verifies that the task is no longer in the tasks list and is in the archived tasks list.
        """
        task_list = TaskList()
        task_list.add_task("Task 1", "Description 1")
        task_list.mark_task_completed("Task 1")
        assert len(task_list.tasks) == 0
        assert len(task_list.archived_tasks) == 1
        assert task_list.archived_tasks[0].name == "Task 1"
        assert task_list.archived_tasks[0].completed is True

    # add_task with empty name raises ValueError
    def test_add_task_with_empty_name_raises_value_error(self):
        """
        Test adding a task with an empty name.
        Verifies that a ValueError is raised.
        """
        task_list = TaskList()
        with pytest.raises(ValueError):
            task_list.add_task("", "Description 1")

    # add_task with empty description raises ValueError
    def test_add_task_with_empty_description_raises_value_error(self):
        """
        Test adding a task with an empty description.
        Verifies that a ValueError is raised.
        """
        task_list = TaskList()
        with pytest.raises(ValueError):
            task_list.add_task("Task 1", "")

    # remove_task with non-existent task name prints error message
    def test_remove_task_with_non_existent_task_name_prints_error_message(self, capsys):
        """
        Test removing a task with a non-existent task name.
        Verifies that an error message is printed.
        """
        task_list = TaskList()
        task_list.remove_task("Task 1")
        captured = capsys.readouterr()
        assert captured.out == "Tâche 'Task 1' introuvable dans la liste.\n"
