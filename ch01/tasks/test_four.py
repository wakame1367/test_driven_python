from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, None, None)


def test_as_dict():
    task_1 = Task("do something", "okken", True, 21)
    task_1_dict = task_1._asdict()
    expected = {"summary": "do something",
                "owner": "okken",
                "done": True,
                "id": 21}
    assert task_1_dict == expected


def test_replace():
    task_before = Task("finish book", "brian", False)
    task_after = task_before._replace(id=10, done=True)
    task_expected = Task("finish book", "brian", True, 10)
    assert task_after == task_after
