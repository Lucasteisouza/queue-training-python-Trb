from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    mock1 = {"qtd_linhas": 1}
    mock2 = {"qtd_linhas": 7}
    mock3 = {"qtd_linhas": 2}
    mock4 = {"qtd_linhas": 12}

    queue.enqueue(mock1)
    queue.enqueue(mock2)
    queue.enqueue(mock3)
    queue.enqueue(mock4)

    assert queue.search(0) == mock1
    assert queue.search(1) == mock3
    assert queue.search(2) == mock2
    assert queue.search(3) == mock4

    with pytest.raises(IndexError):
        queue.search(4)

    with pytest.raises(IndexError):
        queue.search(-1)

    assert queue.dequeue() == mock1
    assert queue.dequeue() == mock3
