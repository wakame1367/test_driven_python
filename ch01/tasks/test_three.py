from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    task_1 = Task()
    task_2 = Task(None, None, None, None)
    assert task_1 == task_2


def test_member_access():
    task = Task("buy milk", "brian")
    assert task.summary == "buy milk"
    assert task.owner == "brian"
    assert (task.done, task.id) == (False, None)
