import pytest
from task1.solution import strict


def test_correct_args_types():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    assert sum_two(2, 3) == 5


def test_incorrect_args_types():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    with pytest.raises(TypeError):
        sum_two(2, "3")


def test_func_without_args():
    @strict
    def say_dragons() -> int:
        return 'Here be dragons!'

    assert say_dragons() == 'Here be dragons!'


def test_unannotated_args():
    @strict
    def sum_two(a, b: int) -> int:
        return a + b

    with pytest.raises(TypeError):
        sum_two(2, "3")
